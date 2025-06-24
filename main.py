import json
import requests
import subprocess
import sys

season = int(sys.argv[1])
episode = int(sys.argv[2])

with open("data.json") as file:
    data = json.load(file)

title = data["seasons"][season - 1][episode - 1]["title"]

print(f"Playing season {season} episode {episode}: {title}...")

mediagen = data["seasons"][season - 1][episode - 1]["mediagen"] 

mediagen_data = requests.get(mediagen).json() 

m3u8 = mediagen_data["stitchedstream"]["source"]

subprocess.run(["mpv", m3u8], stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)

sys.exit()
