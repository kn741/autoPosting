import json
def save_credentials(fbUsername="", fbPassword="", 
                     threadsUsername="", threadsPassword="",
                     twitterUsername="",twitterPassword="",twitterVerify=""):
    credentials = {
        "fbUsername": fbUsername,
        "fbPassword": fbPassword,
        "threadsUsername": threadsUsername,
        "threadsPassword": threadsPassword,
        "twitterUsername": twitterUsername,
        "twitterPassword": twitterPassword,
        "twitterVerify":twitterVerify
    }
    with open('credentials.json', 'w') as file:
        json.dump(credentials, file)

def load_credentials():
    try:
        with open('credentials.json', 'r') as file:
            credentials = json.load(file)
            return credentials
    except FileNotFoundError:
        return {"fbUsername": "", "fbPassword": "", "threadsUsername": "", "threadsPassword": "", "twitterUsername": "", "twitterPassword": "", "twitterVerify": ""}

if __name__ == '__main__':
    credentials = load_credentials()
    if credentials:
        print(credentials)
    else:
        print("找不到儲存的檔案")