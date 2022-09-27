import os
from datetime import datetime
from pytz import timezone
from datetime import time
import time as sleepy
import json

tz = timezone('Africa/Johannesburg')
kp = "wallet.json"
rpc = "https://ssc-dao.genesysgo.net"

f = open('app.json')
data=json.load(f)

os.system("chmod +x ./sugar")

f='%H:%M:%S'

while True:
  now_time = datetime.now(tz)

  t = now_time.strftime(f)
  tt = str(t)
  for d in data:
    settime = time(hour =d["hour"] , minute =d["minute"], second = d["second"])
    stime = str(settime)
    if tt == stime:
      print("loading... "+d["config"])
      print("running command: ./sugar update -k "+kp+" -c "+d["config"]+" -r "+rpc)
      os.system("./sugar update -k "+kp+" -c "+d["config"]+" -r "+rpc)
      sleepy.sleep(2)