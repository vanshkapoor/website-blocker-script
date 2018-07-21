import time
from datetime import datetime as dt
host_tmp = "hosts"
host_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites=["facebook.com","youtube.com","www.facebook.com","www.youtube.com"]

while True:
    if (dt(dt.now().year,dt.now().month,dt.now().day,1) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,2)):
        with open(host_tmp,'r+') as file:
            content = file.read()
            for i in websites:
                if i in host_tmp:
                    pass
                else:
                    file.write(redirect + "  " + i + "\n")
    else: 
        with open(host_tmp,"r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("fun hours") 
        time.sleep(5)