# 监控odoo是否正常运行
不正常立即重启

```
# coding: utf-8
import commands
import os
import datetime,time

restart_cmd_kill = "ps -aux | grep odoo_cw.conf |awk '{print $2}' |xargs kill -9"

restart_cmd_sleep = "sleep 5"

restart_cmd_start = "nohup python /usr/bin/odoo --config /etc/odoo/odoo_cw.conf  --logfile /var/log/odoo/odoo-server_cw.log  &"

cmd = "wget http://127.0.0.1:8069"                                                                                                                                  
return_mes =  commands.getoutput(cmd)                                                                                                                                   

while True:
    date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())                                                                                                                                                       
    if "OK" in return_mes and "index.html" in return_mes:                                                                                                                   
        fw = open("log.log","a")
        fw.write(date+"    service ok !\n")
        fw.close()
    else:
        fw = open("log.log","a")
        fw.write(date+"  restart  service!\n")
        fw.close()
        os.system(restart_cmd_kill)
        os.system(restart_cmd_sleep)
        os.system(restart_cmd_start)
    time.sleep( 10 )
```