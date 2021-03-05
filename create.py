import requests, json

site_key = '6Lef5iQTAAAAAKeIvIY-DeexoO3gj7ryl9rLMEnn'

headers1 = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'
}

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36',
    "content-type": "application/json"
}
# reg = s.get("https://discord.com/register", headers=headers, verify=False)
# print(reg.headers)
# js = s.get("https://discord.com/assets/f01b80e4cdfb11614b33.js", headers=headers1, verify=False)

# since = s.post("https://discord.com/api/v8/science")

"""data = json.dumps({
    "captcha_key": None,
    "consent": True,
    "date_of_birth": "2002-04-04",
    "email": "jhfemjr@web.de",
    "fingerprint": "816979893711536148.bUcfEWIpfmbazkP4oBB-o6EC4q8",
    "gift_code_sku_id": None,
    "invite": None,
    "password": "Doggy1234f",
    "username": "ewgewg"
    })"""

data = json.dumps({"fingerprint":"806273921443430461.lswF1ZT5opBd - fzZyN3N4HWOxbM","email":"ggwegahjk@web.de","username":"Danton","password":"greg!@tgg","invite":None,"consent":True,"date_of_birth":"2003-05-05","gift_code_sku_id":None,"captcha_key":None})
reqister = requests.post("https://discord.com/api/v6/auth/register", data=data, headers=headers)
print(reqister.text)
