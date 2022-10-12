import requests, time, threading, re, sys
from math import trunc

# - - - - - - - - - #
main_TOKEN = ""
TOKENS = [
    "",
]
NAME = ".YmL"
# - - - - - - - - - #

all_options = []
threads=[]
apiv = str(re.search(re.compile("(?<=API_VERSION: ')([0-9]|[1-9][0-9])(?=')"), requests.get("https://discord.com/").text).group())
last_tag=1

def addF(name, tag, token):
    headers = { "Accept": "*/*", "Content-Type": "application/json", "Authorization": token }
    res = requests.post("https://discord.com/api/"+apiv+"/users/@me/relationships", headers=headers, json={"username": name, "discriminator": tag})
    if(res.status_code == 429):
        time.sleep(20)
        addF(name, tag, token)
    else:
        global last_tag
        last_tag+=1
        return res

def status():
    while True:
        if(trunc(last_tag/9999*100) == 100):
            break
        time.sleep(0.001)
        sys.stdout.write("\r")
        sys.stdout.flush()
        sys.stdout.write(str(trunc(last_tag/9999*100))+"%"+" ["+"█"*trunc(last_tag/9999*100)+" "*(100-trunc(last_tag/9999*100))+"]")
    return 0

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

    print(
        "\n"+("-"*__import__("os").get_terminal_size()[0])+"\n",
        "API version:", apiv,
        "\nWorst Time:", str((9999/5*len(TOKENS))/3600)+"h",
        "\n"+("-"*__import__("os").get_terminal_size()[0])+"\n"
    )

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

    statusT = threading.Thread(target = status, args = ())
    statusT.start()

    for x in threads:
        x.join()

    for user in all_options:
        usrname, tag = user.split("#")
        addF(usrname, tag, main_TOKEN)
        time.sleep(4)

if(__name__ == "__main__"):
    main()
