import psutil
import datetime as dt

pid = psutil.pids()

all_process = []
for i in pid:
    
    process = psutil.Process(i)
    cmd = process.cmdline()
    
    if cmd:
        prop = {
            'pid': process.pid,
            'user': process.username(),
            'cmdline' : {
                'cmd': cmd[0],
                'pname': cmd[-1]
                },
            'ptype': process.name(),
            'status': process.status(),
            'time': dt.datetime.fromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')
        }
    
    else:

        prop = {
            'pid': process.pid,
            'user': process.username(),
            'ptype': process.name(),
            'status': process.status(),
            'time': dt.datetime.fromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')
        }
    
    all_process.append(prop)
    #print(f"User: {process.username()} ran {process.cmdline()}  -->  {process} \n")


for i in all_process:
	
	key = 'cmdline'
	if key in i:
		if i['cmdline']['pname'] == 'logger.py':
			print(f"Found keylogger: '{i['cmdline']['pname']}' at -> {i['pid']}")
			psutil.Process(i['pid']).kill()
			print(f"Process {i['pid']} was killed!")
