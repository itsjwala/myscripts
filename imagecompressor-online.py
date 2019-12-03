# X-rayed https://compressor.io/compress
# image format supported jpeg, png, gif, jpeg

import requests
import json
from os import path
import sys

def usage():
	u = f"""
python3 {__file__} FILEPATH [lossy|notlossy]
	"""
	print(u)

def compress(file_path,lossy = True):

	url = "https://compressor.io/server/Lossy.php" if lossy else "https://compressor.io/server/Lossless.php"
	session = requests.Session()
	file_name = path.split(file_path)[-1]
	response = session.post(url,files ={"files" :  (file_name,open(file_path,"rb"))})
	response = json.loads(response.content)
	res = session.get(response["files"][0]["url"])
	with open(path.join(path.dirname(file_path),f"compressed-{file_name}"),"wb") as f:
	    f.write(res.content)


try:
	filepath = sys.argv[1]

	lossy = True if sys.argv[2] == "lossy" else False

	print("Processing...")
	compress(file_path=filepath,lossy=lossy)
	print("Done!")
except IndexError:
	usage()
except Exception as e:
	print(e)


