import pymysql
import subprocess
import sys
import time

#Checking if we are logged in
subid = subprocess.getoutput("az account show | grep id")
error = "Please run 'az login' to setup account."
today = time.strftime("%Y%m%d")
sys.stdout = open('/home/username/az-log/azire-as.log-'+ today, 'w')

go = subid == error
if go == True:
  print(subid)
else:
  #find some permanent values
  dow = subprocess.getoutput("date +%u")
  gid = 'dc_cb_jumpbox'
  subid = (subid[9:-2])

  #Work with DB
  db = pymysql.connect("127.0.0.1","<db_user>","<db_password>,"<db_name>" )
  cursor = db.cursor()
  cursor.execute("select s1.vm_name, s1.email, s2.as_time from staff as s1 join schedule as s2 on s1.team_name = s2.team_name where s2.dow = "+str(dow)+" and s2.shift !='0'")
  db.close()

  #Here we go
  data = cursor.fetchall()
  print (data)
  for row in data:
    #In the request below timezone is "Singapore Standard Time", set requried one                   
    query = ('''az resource create -g '''+str(gid) + ''' -n shutdown-computevm-'''+str(row[0]) + ''' --resource-type microsoft.devtestlab/schedules --properties \"{\\"status\\":\\"Enabled\\",\\"timeZoneId\\":\\"Singapore Standard Time\\",\\"taskType\\":\\"ComputeVmShutdownTask\\",\\"notificationSettings\\":{\\"status\\":\\"Enabled\\",\\"timeInMinutes\\":30,\\"webhookUrl\\":\\"\\",\\"emailRecipient\\":\\"'''+str(row[1]) + '''\\",\\"notificationLocale\\":\\"en\\"},\\"targetResourceId\\":\\"/subscriptions/'''+str(subid) + '''/resourceGroups/'''+str(gid) + '''/providers/Microsoft.Compute/virtualMachines/'''+str(row[0]) + '''\\",\\"DailyRecurrence\\":{\\"time\\":\\"'''+str(row[2]) + '''\\"}}\"''')
    print (query)  
    execution = subprocess.getoutput(query)
    time.sleep(2)
    print(execution)
