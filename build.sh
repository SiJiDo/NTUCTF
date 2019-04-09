#! /usr/bin/env bash

docker pull nickistre/centos-lamp:latest
docker pull eboraas/apache-php:latest

cd /web_sql1/
docker build -t ntuctf:web_sql1 .
cd ../web_sql2/
docker build -t ntuctf:web_sql2 .
cd ../web_ying/
docker build -t ntuctf:web_ying .
cd ../web_phpmyadmin/
docker build -t ntuctf:web_phpmyadmin .
cd ../web_easy/
docker build -t ntuctf:web_easy .
cd ../web_file/
docker build -t ntuctf:web_file .