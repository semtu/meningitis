import requests

url = "https://www.plugai.xyz/inference/integer/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiT2d1bl9SdXJhbF81MCJ9.XloM9ZumfC4MRCFZGWpPIl2hYKRPZJaB1LPxZeJKJ98"

payload = {'fig': '1,0,0,0,0,0,0,0,0,0,0,0,1,0.1,1,0,0,1,1'}
files = [

]
headers = {
  'Cookie': '__cfduid=dff1fabb883912efdce5fe0da9af16c871603217819'
}

response = requests.request("POST", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8')['0'])
