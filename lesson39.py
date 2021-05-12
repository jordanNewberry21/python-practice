# Downloading from the Web with the Requests Module

import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(res.status_code)

# print(len(res.text))

# print(res.text[:500])

# badRes = requests.get('http://atuomatetheboringstuff.com/sdghfsdhfgsdhf')
# badRes.raise_for_status()

# 'wb' stands for write-binary mode
playFile = open('RomeoAndJuliet.txt', 'wb')
# even if the file is in plain text, you still need to open the file 
# in write-binary mode to preserve the Unicode encoding for Python
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()

# the requests module is a third-party module for downloading web pages and files.
# requests.get() returns a response object
# the raise_for_status() response method will raise an exception if the download failed
# you can save a downloaded file to your hard drive with calls to the iter_content() method.

