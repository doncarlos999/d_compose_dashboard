FROM nginx:1.21.1
EXPOSE 8082
EXPOSE 8081
RUN apt update && apt install -y apache2-utils
RUN mkdir -p /etc/httpd
RUN htpasswd -bc /etc/httpd/htpasswd.users test_user test_password
COPY ./nginx.conf /etc/nginx/nginx.conf
