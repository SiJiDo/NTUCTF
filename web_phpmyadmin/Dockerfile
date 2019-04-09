FROM nickistre/centos-lamp:latest

COPY src/ /var/www/html/
COPY flag/ /var/

RUN /etc/init.d/mysqld start \
    && mysqladmin -uroot password 'root' \
    && chmod -R 777 /var/www/html/
