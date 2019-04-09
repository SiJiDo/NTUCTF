FROM nickistre/centos-lamp:latest

COPY src/ /var/www/html/

RUN rm /var/www/html/phpinfo.php \
    && chmod -R 655 /var/www/html/