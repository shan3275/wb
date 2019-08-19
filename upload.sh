#!/bin/sh
LOCATION="/root/work/wb"
python ${LOCATION}/rdup.py 	-i ${LOCATION} -o ${LOCATION}
python ${LOCATION}/upload_v3.py -i ${LOCATION} -o ${LOCATION}
