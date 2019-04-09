FROM nickistre/centos-lamp:latest

COPY src/ /var/www/html/

RUN rm /var/www/html/phpinfo.php \
    && chmod -R 755 /var/www/html \
	&& sed -i 's/allow_url_include = Off/allow_url_include = On/g' /etc/php.ini