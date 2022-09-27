import requests, time, re
from math import trunc

# - - - - - - - - - #
main_TOKEN = ""
TOKENS = [""]
NAME = ""
# - - - - - - - - - #

all_options = []
apiv = str(re.search(re.compile("(?<=API_VERSION: ')([0-9]|[1-9][0-9])(?=')"), requests.get("https://discord.com/").text).group())

def addF(name, tag, token):
    headers = { "Accept": "*/*", "Content-Type": "application/json", "Authorization": token }
    res = requests.post("https://discord.com/api/"+apiv+"/users/@me/relationships", headers=headers, json={"username": name, "discriminator": tag})

    if(res.status_code == 429): #if program is sending too many requests to discord sleep for 20s and call recursion
        time.sleep(20)
        addF(name, tag, token)
    else:
        return res

def addFrom(x, z, name, token):
    for i in range(x, z): #tag is between x and y
        res = addF(name=name, tag=i, token=token) # send a friend request
        if(res.status_code == 204): #if request response code returns 204 no content
            print(NAME+"#"+str(i))
            all_options.append(NAME+"#"+str(i)) #save newly found user to the list of all users found

        time.sleep(5)

def main():
    if(len(main_TOKEN) < 1 and len(NAME) < 1 and len("".join(TOKENS)) < 1): #if config is valid
        print("Main Token or Tokens or Name missing!")
        return None

    #Split tags to all available tokens
    perToken = trunc(10000/len(TOKENS))
    left = 10000 - perToken
    last=1

    for token in TOKENS:
        x=last
        z=last+perToken
        last=z

        if(token==TOKENS[len(TOKENS)-1]):   #if the token is the last token in the token list, add the remaining tags to it
            z+=left

        addFrom(x, z, NAME, token)

    #Add every user in list of found users
    for user in all_options:
        usrname, tag = user.split("#")
        addF(usrname, tag, main_TOKEN)
        time.sleep(4)


if(__name__ == "__main__"):
    main()
