#!/usr/bin/env bash
set -e

SLEEP=120

for file in ${TABLES_BACKUP_LIST[@]}; do
  echo Downloading "${file}"
  aria2c https://flibusta.is/sql/"${file}"
done

gzip -d *.gz
cat *sql > full.sql

cat > ~/.my.cnf <<EOF
[client]
user=root
password=root
EOF

echo Sleeping 10 secs before importing to MySQL...
echo Uploading to MySQL strarting...
mysql -h mysql-db -e "create database books"
mysql -h mysql-db books < full.sql
echo Uploading to MySQL finished.

touch /KHUI # it's a healthcheck file.

echo Sleeping "${SLEEP}" seconds before shutting down MySQL.
sleep $SLEEP
mysqladmin -u root -h mysql-db shutdown