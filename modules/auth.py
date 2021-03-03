import requests, sys, subprocess


class auth():
    def __init__(self):
        self.base = "https://discord-haxx.herokuapp.com/api"


    def hwid(self):
        cmd = 'wmic csproduct get uuid'
        uuid = str(subprocess.check_output(cmd))
        pos1 = uuid.find("\\n")+2
        uuid = uuid[pos1:-15]
        return uuid

    
    def Login(self, user, password):
        hwid = self.hwid()
        url = f"{self.base}/login/{user}/{password}/{hwid}"
        r = requests.get(url, headers={"Content-Type": "application/json"})
        if "Successfuly logged in." in r.json()["message"]:
            return True
        elif "Username or password or hwid are inccorect!" in r.json()["message"]:
            return False
        else:
            print("[ERROR] Error in login! Please contact support.")
            sys.exit(0)
        