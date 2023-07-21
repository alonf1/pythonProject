import requests
from time import sleep
while True:
    r = open("url.txt")
    url = r.readline()
    i = requests.get(url.rstrip())
    if i.status_code != 200:
      print(url + " is dead")
    sleep(5)
    r.close()