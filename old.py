import requests, time, re

TOKEN = ""
NAME = ""

all_options = []
apiv = str(re.search(re.compile("(?<=API_VERSION: ')([0-9]|[1-9][0-9])(?=')"), requests.get("https://discord.com/").text).group())

Blazarw_mi_daje_head= {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Authorization": TOKEN,
}

for i in range(1, 10000):
    res = requests.post("https://discord.com/api/v"+apiv+"/users/@me/relationships", headers=Blazarw_mi_daje_head, json={"username": NAME, "discriminator": i})
    if(str(res.status_code) == "204"):
        print(NAME+"#"+str(i))
        all_options.append(NAME+"#"+str(i))

    time.sleep(5)

    print(all_options)
