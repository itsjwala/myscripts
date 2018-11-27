# X-rayed https://compressor.io/compress 
# image format supported jpeg, png, gif, jpeg

import requests
import json
from os import path


def compress(file_path,lossy = True):
	url = "https://compressor.io/server/Lossy.php" if lossy else "https://compressor.io/server/Lossless.php" 
	session = requests.Session()
	file_name = path.split(file_path)[-1]

	response = session.post(url,files ={"files" :  (file_name,open(file_path,"rb"))})
	response = json.loads(response.content)
	res = session.get(response["files"][0]["url"])
	with open(f"compressed-{file_name}","wb") as f:
	    f.write(res.content)



compress("sample.png")	
