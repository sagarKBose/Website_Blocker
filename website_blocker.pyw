import time
import datetime
from datetime import datetime as dt
website_list=["www.facebook.com", "facebook.com", "www.youtube.com","youtube.com"]
host_file_path_original=r"C:\Windows\System32\drivers\etc\hosts"
host_file_path_temp=r"E:\Python programs\PYTHON_with_ardit\project_websiteblocker\hosts"
redirect_ip="127.0.0.1"

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,0) < (dt.now()) < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working hours...")
        with open(host_file_path_original, 'r+') as file:
            content=file.read()
            for i in website_list:
                if i in content:
                    pass
                else:
                    file.write(redirect_ip + ' ' + i+"\n" )
            
        
    else: 
        with open(host_file_path_original,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
                    file.truncate()
        print("FUN time...")
    
    time.sleep(5)