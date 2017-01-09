#!/bin/bash
YESTERDAY=`date +"%Y%m%d" -d "-1 days"`
tar -zcf /opt/script/bak/api.zpchefang-access_"$YESTERDAY".tar.gz /opt/www/logs/api.zpchefang-access_"$YESTERDAY"_log
tar -zcf /opt/script/bak/ht.zpchefang-access_"$YESTERDAY".tar.gz /opt/www/logs/ht.zpchefang-access_"$YESTERDAY"_log
tar -zcf /opt/script/bak/img.zpchefang-access_"$YESTERDAY".tar.gz /opt/www/logs/img.zpchefang-access_"$YESTERDAY"_log
tar -zcf /opt/script/bak/www.zpchefang-access_"$YESTERDAY".tar.gz /opt/www/logs/www.zpchefang-access_"$YESTERDAY"_log
ftp -n<<!
open 101.200.143.101
user logs Zhong123pu$
binary
cd 182.92.103.63
lcd /opt/script/bak
put api.zpchefang-access_"$YESTERDAY".tar.gz
put ht.zpchefang-access_"$YESTERDAY".tar.gz
put img.zpchefang-access_"$YESTERDAY".tar.gz
put www.zpchefang-access_"$YESTERDAY".tar.gz
close
bye
!
rm -rf /opt/script/bak/api.zpchefang-access_"$YESTERDAY".tar.gz
rm -rf /opt/script/bak/ht.zpchefang-access_"$YESTERDAY".tar.gz
rm -rf /opt/script/bak/img.zpchefang-access_"$YESTERDAY".tar.gz
rm -rf /opt/script/bak/www.zpchefang-access_"$YESTERDAY".tar.gz