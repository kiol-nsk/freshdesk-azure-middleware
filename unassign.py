import pymysql
import subprocess
import sys
import time


#Checking if we are logged in
subid = subprocess.getoutput("az account show | grep id")
error = "Please run 'az login' to setup account."
active = "VM deallocated"
today = time.strftime("%Y%m%d")
sys.stdout = open('/home/username/az-log/unassign.log-'+ today, 'w')

#Permanent data
gid = 'dc_cb_jumpbox'
subid = (subid[9:-2])
db_ip = "127.0.0.1"
db_user = "hardcoded_user"
db_pass = "hardcoded_password"
db_name = "hardcoded_dbname"
fd_key = "hardcoded_API-key"


#Day 'shift' for a night 'shift'
if sys.argv[1] == 'D':
  dow = int(subprocess.getoutput("date +%u"))
  print (dow)
elif sys.argv[1] == 'N':
  dow = int(subprocess.getoutput("date +%u")) - 1
#  '-1' because we are running script the next day, when shift is over 
  if dow ==0:
    dow = 7
  else:
    dow == dow
  print (dow)
else:
  print ('Error')
  exit()

#date to track execution time
print('Script execution start time:',subprocess.getoutput("date"))

go = subid == error
if go == False:

  #work with DB
  db = pymysql.connect(str(db_ip),str(db_user),str(db_pass),str(db_name) )
  cursor = db.cursor()
  #we are gerring ONLY engineers from the last shift
  #preliminary schedule 11:30PM after DayShift, 9AM after Night shift
  cursor.execute("select s1.vm_name, s1.flag from staff as s1 join schedule as s2 on s1.team_name = s2.team_name where s2.dow = "+str(dow)+" and s2.shift ='"+sys.argv[1]+"'")
  db.close()


  #Here we go
  data = cursor.fetchall()
  print (data)
  for row in data:
    #first we need the list of VMs that runnung after shift-end
    query = ('''az vm list -g '''+str(gid) + ''' -d --query "[?name==\'''' +str(row[0]) + '''\']" | egrep \'powerState\' ''')   
    print (query)  
    execution = subprocess.getoutput(query)
    print(execution)
    if execution == '''    "powerState": "VM deallocated",''':
      print('VM deallocated')
      fresh_call = ('''curl -s -u '''+str(fd_key)+''':X -H \'authority: domain.freshdesk.com\' \"https://domain.freshdesk.com/api/v2/search/tickets?query=%22agent_id:'''+str(row[1]) +'''%20AND%20(status:2%20OR%20status:8)%22\" --compressed | grep -E -o \"\\"id\\":.{0,5}\"''')
      print(fresh_call)
      fresh_execution = subprocess.getoutput(fresh_call)
      if fresh_execution is None:
        print('no tickets') #this part does not work preperly, but anyway - result is expected
      else:
        print(fresh_execution)
        ticket_list = [y[5:] for y in (x.strip() for x in fresh_execution.splitlines()) if y]
        print(ticket_list)
        for ticket in ticket_list:
          ticket_update = ('''curl -s -u '''+str(fd_key)+''':X -H 'Content-Type: application/json' -H 'authority: domain.freshdesk.com' -X PUT -d \'{ \"responder_id\":null,\"group_id\":null }\' \'https://domain.freshdesk.com/api/v2/tickets/'''+str(ticket)+'\'')
          print(ticket_update)
          ticket_result = subprocess.getoutput(ticket_update)
          print(ticket_result)
          print('Done')
    else:
      print('online')
  print('Script execution end time:',subprocess.getoutput("date"))
