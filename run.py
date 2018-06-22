import subprocess
import requests
import time

print("\nStarting Ajantala", flush=True)

try:
    r =  requests.get('http://127.0.0.1:8000')
except:
    subprocess.call(['pip3', 'install', '-r', 'requirements.txt'])
    
    proc = subprocess.Popen(['python', 'ajantala/manage.py', 'runserver'])
    
    while True:
        try:
            r =  requests.get('http://127.0.0.1:8000')
            break
        except:
            time.sleep(1)

    

subprocess.call(['python', 'app.py'])

proc.kill()
time.sleep(5)
print("killed!")
