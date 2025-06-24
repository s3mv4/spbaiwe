import json
import requests
import subprocess
import sys

season = int(sys.argv[1])
episode = int(sys.argv[2])

with open("data.json") as file:
    data = json.load(file)

if season < 1 or season > len(data["seasons"]):
    print(f"season {season} episode {episode} does not exist!")
    sys.exit()

if episode < 1 or episode > len(data["seasons"][season - 1]):
    print(f"season {season} episode {episode} does not exist!")
    sys.exit()

title = data["seasons"][season - 1][episode - 1]["title"]

print(f"Playing season {season} episode {episode}: {title}...")

mediagen = data["seasons"][season - 1][episode - 1]["mediagen"] 

if mediagen == "":
    print(f"season {season} episode {episode}: {title} not available!")
    sys.exit()

mediagen_data = requests.get(mediagen).json() 

m3u8 = mediagen_data["stitchedstream"]["source"]

subprocess.run(["mpv", m3u8], stdout = subprocess.DEVNULL, stderr = subprocess.STDOUT)

sys.exit()
