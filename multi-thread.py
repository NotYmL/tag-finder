import requests, time, threading, re
from math import trunc

# - - - - - - - - - #
main_TOKEN = ""
TOKENS = [""]
NAME = ""
# - - - - - - - - - #

all_options = []
threads=[]
regex = re.compile("(API_VERSION: '.',)")
isnum = re.compile('[0-9]')
res = requests.get("https://discord.com/").text
apiv = str(re.search(isnum, re.search(regex, res).group()).group())

def addF(name, tag, token):
    headers = { "Accept": "*/*", "Content-Type": "application/json", "Authorization": token }
    res = requests.post("https://discord.com/api/"+apiv+"/users/@me/relationships", headers=headers, json={"username": name, "discriminator": tag})
    if(res.status_code == 429):
        time.sleep(20)
        addF(name, tag, token)
    else:
        return res

def addFrom(x, z, name, token):
    for i in range(x, z):
        res = addF(name=name, tag=i, token=token)
        if(res.status_code == 204):
            print(NAME+"#"+str(i))
            all_options.append(NAME+"#"+str(i))

        time.sleep(5)

def main():
    if(len(main_TOKEN) < 1 and len(NAME) < 1 and len("".join(TOKENS)) < 1):
        print("Main Token or Tokens or Name missing!")
        return None

    perToken = trunc(10000/len(TOKENS))
    left = 10000 - perToken
    last=1

    for token in TOKENS:
        x=last
        z=last+perToken
        last=z

        if(token==TOKENS[len(TOKENS)-1]):
            z+=left

        x = threading.Thread(target = addFrom, args = (x, z, NAME, token, ))
        threads.append(x)

    for x in threads:
        x.start()

    for x in threads:
        x.join()

    for user in all_options:
        usrname, tag = user.split("#")
        addF(usrname, tag, main_TOKEN)
        time.sleep(4)

if(__name__ == "__main__"):
    main()
