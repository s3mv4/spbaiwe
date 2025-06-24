import json

with open("data.json") as file:
    data = json.load(file)

for season in data["seasons"]:
    for episode in season:
        url = episode["url"]
        ep_num = episode["episode"]
        ep_url = url[url.rfind("-") + 1:]

        if ep_url == "":
            print(f"season {episode["season"]} episode {ep_num}: {episode["title"]} not available!")
        elif ep_url != ep_num:
            print(f"season {episode["season"]} episode {ep_num}: {episode["title"]} out of order!")

