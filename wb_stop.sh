#!/usr/bin/env bash
procID=`ps -aux |grep "python udp_server.py" |grep -v grep|awk '{ print $2}'`
if [ "" != "$procID" ];
then
	cd /root/work/wb/
	date >> reboot.log
	echo 'task is alive, kill it --->' >> reboot.log
	kill -9 $procID
fi
