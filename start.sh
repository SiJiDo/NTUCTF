#! /usr/bin/env bash

docker run -i -d -p 10001:80 ntuctf:web_sql1
docker run -i -d -p 10002:80 ntuctf:web_ying
docker run -i -d -p 10003:80 ntuctf:web_file
docker run -i -d -p 10004:80 ntuctf:web_sql2
docker run -i -d -p 10005:80 ntuctf:web_phpmyadmin
docker run -i -d -p 10006:80 ntuctf:web_easy

