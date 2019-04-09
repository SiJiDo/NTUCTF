FROM nickistre/centos-lamp:latest

COPY src/ /var/www/html/

RUN /etc/init.d/mysqld start \
    && mysqladmin -uroot password 'sijidou' \
    && mysql -e "CREATE DATABASE sql_test DEFAULT CHARACTER SET utf8;" -uroot -psijidou \
    && mysql -e "use sql_test;source /var/www/html/sql_test.sql;" -uroot -psijidou \
    && rm /var/www/html/sql_test.sql \
    && rm /var/www/html/phpinfo.php \
    && chmod -R 655 /var/www/html/
