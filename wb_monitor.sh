#!/usr/bin/env bash
procID=`ps -aux |grep "python udp_server.py" |grep -v grep`
if [ "" == "$procID" ];
then
	cd /root/work/wb/
	date >> reboot.log
	echo '启动task' >> reboot.log
	nohup python udp_server.py >> /root/work/wb/info.log 2>&1 &
fi