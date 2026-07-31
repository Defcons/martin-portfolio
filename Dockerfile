FROM nginx:alpine

# Remove default nginx page
RUN rm -rf /usr/share/nginx/html/*

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

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
