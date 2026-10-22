FROM nginxinc/nginx-unprivileged:alpine

# Not root: this image runs nginx as uid 101 (pid file and temp paths in /tmp) and listens on 3040, the published host
# port. Clearing the stock page needs root, so only that step runs as root; the compose file pins the user too.
USER root
# Remove default nginx page
RUN rm -rf /usr/share/nginx/html/*
USER 101

# Copy nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy static site files
COPY index.html /usr/share/nginx/html/
COPY styles.css /usr/share/nginx/html/
COPY script.js /usr/share/nginx/html/
COPY robots.txt /usr/share/nginx/html/
COPY favicon.svg /usr/share/nginx/html/
COPY favicon.ico /usr/share/nginx/html/
COPY favicon-32.png /usr/share/nginx/html/
COPY apple-touch-icon.png /usr/share/nginx/html/
COPY fonts/ /usr/share/nginx/html/fonts/
COPY images/ /usr/share/nginx/html/images/

EXPOSE 3040

CMD ["nginx", "-g", "daemon off;"]
