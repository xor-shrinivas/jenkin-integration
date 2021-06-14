import sys, select, os
from time import sleep
from json import dumps
from kafka import KafkaProducer
from datetime import datetime, date, time
import pytz
from pytz import timezone
from dateutil.tz import gettz
import time
import re
data = []
file_position = 0

producer = KafkaProducer(bootstrap_servers=['192.168.56.110:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))
ts = time.time()
substring='New smtp Connection'
substring1='New http Connection'
while True:
    with open('/var/log/iptables.log', 'r') as f:
        f.seek(file_position)  # fast forward beyond content read previously
        for line in f:
             if substring in line or substring1 in line:
                print(line);
                str=re.sub(r"(\[(\s)*)+","[",line);
                print(str)
                str2=str.replace("  "," ")
                print(str2)
                #str=line;
                parts = str2.split(" ")
                month=parts[0]
                date=parts[1]
                _time=parts[2]
                #print(_time);
                times=_time.split(":")
                hour=times[0]
                minute=times[1]
                second=times[2]
                timestamp=month+' '+' '+date+' '+_time
                host=parts[3]
                kernal=parts[5]
                details=parts[6]+'-'+parts[7]+'-'+parts[8]
                interface=parts[9].replace('IN=', '')
                src=parts[12].replace('SRC=', '')
                dst=parts[13].replace('DST=', '')
                spt=parts[21].replace('SPT=', '')
                dpt=parts[22].replace('DPT=', '')
                datetime_object =datetime.strptime(month, "%b")
                month_number = datetime_object.month
                now = datetime.now()
                #my_date = datetime(now.year, month_number, int(date), int(hour), int(minute), int(second), tzinfo=timezone('Asia/Kolkata'))
                sys_date = datetime(now.year, month_number, int(date), int(hour), int(minute), int(second), tzinfo=gettz('Asia/Kolkata'))   
                utc_date=sys_date.astimezone(timezone('UTC'))
                _format = "%Y-%m-%d %H:%M:%S %Z%z"
                #_format = "%Y-%m-%d %H:%M:%S.%f"
                sys_time=sys_date.strftime(_format)
                print(sys_time)
                sys_time_stamp=time.mktime(datetime.strptime(sys_time,_format).timetuple())
                print(sys_time_stamp)
                utc_time=utc_date.strftime(_format)
                print(utc_time)
                utc_time_stamp=time.mktime(datetime.strptime(utc_time,_format).timetuple())
                print(utc_time_stamp)
                #dt2 = eval(format(float(utc_time_stamp), '.3f'))
                dt2 = eval(format(float(sys_time_stamp), '.3f'))
                dt_object = datetime.fromtimestamp(dt2)
                print(dt_object)
                iptables=[{"values":[1.62,details,interface,src,dst,spt,dpt],"dstypes":["derive","derive","derive","derive","derive","derive","derive"],"dsnames":["value","details","interface","src","dst","spt","dpt"],"time":dt2, "interval":10,"host":"2253de2c-a56c-db42-aaaf-919f0ae40490","plugin":"kernel4","plugin_instance":"filterAccounting","type":"ipt-packets","type_instance":""}]
                print(iptables)
                producer.send('collectd', value=iptables)
                sleep(1)
        file_position = f.tell()  # store position at which to resume
