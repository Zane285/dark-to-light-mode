import requests, os
req = requests.Session()
token = input("Enter authorization token: ").strip('""')
os.system("cls")
headers = {
         'Authorization': token,
         'accept':'*/*', 
         'accept-language':'en-US', 
         'connection':'keep-alive', 
         'cookie': f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US', 
         'DNT':'1', 
         'origin':'https://discord.com', 
         'sec-fetch-dest':'empty', 
         'sec-fetch-mode':'cors', 
         'sec-fetch-site':'same-origin', 
         'TE':'Trailers', 
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36', 
         'X-Super-Properties':'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
}
payload = {'theme':'light'}
payload2 = {'theme':'dark'}
counter = 0
while True:
    light = req.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)
    dark = req.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload2)
    counter += 1
    print(f"Changed from light to dark {counter} time(s)")
