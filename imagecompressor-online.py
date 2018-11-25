import requests
import json

url = "https://compressor.io/server/Lossless.php"

file_name = "sample.png"

session = requests.Session()

response = session.post(url,files ={"files" :  (file_name,open(file_name,"rb"))})

response = json.loads(response.content)

res = session.get(response["files"][0]["url"])

with open(f"compressed-{file_name}","wb") as f:
    f.write(res.content)
