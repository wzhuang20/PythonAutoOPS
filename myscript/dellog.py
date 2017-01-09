#!/bin/bash

LASTMONTH=`date +%Y%m -d "-1 month"`
find /opt/www/logs/ -type f -name "*$LASTMONTH*" -delete