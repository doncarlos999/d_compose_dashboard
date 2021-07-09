FROM httpd:2.4.48
EXPOSE 79
EXPOSE 80
COPY httpd.conf /usr/local/apache2/conf/httpd.conf
RUN mkdir -p /usr/local/apache2/conf/sites/
RUN mkdir -p /etc/httpd
RUN htpasswd -bc /etc/httpd/htpasswd.users test_user test_password
COPY streamlit.conf /usr/local/apache2/conf/sites/streamlit.conf
COPY cellxgene.conf /usr/local/apache2/conf/sites/cellxgene.conf
