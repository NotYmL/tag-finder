import requests, time

TOKEN = ""
NAME = ""

all_options = []

Blazarw_mi_daje_head= {
    "Accept": "*/*",
    "Content-Type": "application/json",
    "Authorization": TOKEN,
}

for i in range(1, 10000):
    res = requests.post("https://discord.com/api/v9/users/@me/relationships", headers=Blazarw_mi_daje_head, json={"username": NAME, "discriminator": i})
    # print(res)
    if(str(res.status_code) == "204"):
        print(NAME+"#"+str(i))
        all_options.append(NAME+"#"+str(i))

    time.sleep(5)

    print(all_options)
