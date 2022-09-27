import requests, time, re

# - - - - - - - - - #
TOKEN = ""
NAME = ""
# - - - - - - - - - #

all_options = []
regex = re.compile("(API_VERSION: '.',)")
isnum = re.compile('[0-9]')
res = requests.get("https://discord.com/").text
apiv = str(re.search(isnum, re.search(regex, res).group()).group())

def addF(name, tag, token):
    headers = { "Accept": "*/*", "Content-Type": "application/json", "Authorization": token }
    res = requests.post("https://discord.com/api/"+apiv+"/users/@me/relationships", headers=headers, json={"username": name, "discriminator": tag}) #send a friend request

    if(res.status_code == 429): #if program is sending too many requests to discord sleep for 20s and call recursion
        time.sleep(20)
        addF(name, tag, token)
    else:
        return res

def main():
    for i in range(1, 10000):   #for every tag option
        res = addF(NAME, i, TOKEN)

        if(str(res.status_code) == "204"): #if request response code returns 204 no content
            print(NAME+"#"+str(i))
            all_options.append(NAME+"#"+str(i))     #save newly found user to the list of all users found

        time.sleep(5)


if(__name__ == "__main__"):
    main()
