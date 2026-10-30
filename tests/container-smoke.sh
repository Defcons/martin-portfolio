#!/usr/bin/env bash
# The production container in its real shape (docker-compose.yml and the Dockerfile, as the box runs them): the page is
# served by nginx as uid 101 on a read-only filesystem, on 3040 (the published host port). A directory URL without its
# trailing slash redirects with a relative Location (no host, no ":3040"), no process in the container runs as root,
# all capabilities are dropped, and the image cannot be written.
# Needs Docker with compose v2 and curl, as on CI's runner:
#   bash tests/container-smoke.sh
set -euo pipefail
cd "$(dirname "$0")/.."
PORT=3040
C="docker compose -p martin-portfolio-smoke"
fail() { echo "FAIL: $*" >&2; exit 1; }
trap 'rc=$?; [ "$rc" -eq 0 ] || $C logs --tail 80 >&2 || true; $C down -v >/dev/null 2>&1 || true' EXIT

$C up -d --build
base="http://127.0.0.1:$PORT"
curl -s -o /dev/null --retry 30 --retry-delay 1 --retry-all-errors "$base/" || fail "nothing answers on $base"

status() { curl -s -o /dev/null -w '%{http_code}' "$base$1"; }
location() { curl -s -o /dev/null -D - "$base$1" | tr -d '\r' | sed -n 's/^[Ll]ocation: //p'; }
redirects_to() { # path expected-Location
  [ "$(status "$1")" = 301 ] || fail "$base$1 does not answer 301"
  loc="$(location "$1")"
  [ "$loc" = "$2" ] || fail "$base$1 redirects to '$loc', not '$2' (a Location with a host or ':$PORT' breaks behind the proxy)"
}

for path in / /styles.css /script.js /robots.txt /favicon.svg /fonts/inter-latin-var.woff2 /some/deep/route; do
  s="$(status "$path")"
  [ "$s" = 200 ] || fail "$base$path answers $s, not 200"
done

# Versioned assets, webp pictures included, get the long immutable cache; the HTML does not.
# The headers are read whole first: with pipefail, grep -q quitting early can break tr's pipe and fail the check.
for path in /styles.css /images/aurly-1.webp; do
  h="$(curl -s -o /dev/null -D - "$base$path" | tr -d '\r')"
  printf '%s\n' "$h" | grep -qi '^cache-control:.*immutable' || fail "$base$path is not served immutable"
done
h="$(curl -s -o /dev/null -D - "$base/" | tr -d '\r')"
if printf '%s\n' "$h" | grep -qi '^cache-control:.*immutable'; then fail "$base/ is served immutable"; fi

# The security headers reach the assets too, not only the HTML (an add_header in a location drops the server's).
for path in / /styles.css /script.js /images/aurly-1.webp /fonts/inter-latin-var.woff2; do
  h="$(curl -s -o /dev/null -D - "$base$path" | tr -d '\r')"
  for want in 'x-content-type-options: nosniff' 'x-frame-options: sameorigin' 'referrer-policy: strict-origin-when-cross-origin'; do
    printf '%s\n' "$h" | grep -qi "^$want\$" || fail "$base$path lacks '$want'"
  done
done

# Directory URLs without the slash: relative Location, never the host or the port.
redirects_to /fonts /fonts/
redirects_to /images /images/

uids="$(docker top martin-portfolio -o pid,uid | awk 'NR>1{print $2}' | sort -u | tr '\n' ' ')"
[ "$uids" = "101 " ] || fail "the container's processes run as uid(s) $uids, not 101 alone"
$C exec -T martin-portfolio grep -q '^CapBnd:[[:space:]]*0000000000000000$' /proc/1/status || fail "capabilities are not all dropped"
$C exec -T martin-portfolio grep -q '^NoNewPrivs:[[:space:]]*1$' /proc/1/status || fail "no-new-privileges is not set"
if $C exec -T martin-portfolio sh -c 'touch /usr/share/nginx/html/written' 2>/dev/null; then fail "the files in the image are writable"; fi
$C exec -T martin-portfolio sh -c 'touch /tmp/ok' || fail "/tmp is not writable"
echo "container smoke: PASS (uid 101, read-only, caps dropped, page served, redirects stay relative)"
