FROM nickistre/centos-lamp:latest

COPY src/ /var/www/html/

RUN /etc/init.d/mysqld start \
    && mysqladmin -uroot password 'root' \
    && mysql -e "CREATE DATABASE sql_test2 DEFAULT CHARACTER SET utf8;" -uroot -proot \
    && mysql -e "use sql_test2;source /var/www/html/sql_test2.sql;" -uroot -proot \
    && rm /var/www/html/sql_test2.sql \
    && rm /var/www/html/phpinfo.php \
    && chmod -R 655 /var/www/html/
