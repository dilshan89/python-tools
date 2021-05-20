import json
import requests

url = "https://query1.finance.yahoo.com/v8/finance/chart/SGD=X?symbol=SGD%3DX&period1=1425368108&period2" \
      "=1586080675&interval=1wk&includePrePost=true&events=div|split|earn&lang=en-SG&region=SG&crumb=9KSKugdThER&corsDomain=sg.finance.yahoo.com"

response = requests.get(url)
dic = json.loads(response.text)
json_obj = json.dumps(dic, indent=2)

with open("output.txt", "w") as f:
    f.write(json_obj)