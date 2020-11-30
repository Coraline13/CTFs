import requests
import urllib.request

opener = urllib.request.FancyURLopener({})
url = 'http://52.43.11.239:5553/{}/{}/{}/{}/'

for i in range(10):
	for j in range(10):		
		for k in range(10):		
			for l in range(10):
				f = opener.open(url.format(i, j, k, l))
				content = f.read()				
				file = open(f'Poland{i}{j}{k}{l}.out', 'wb')
				file.write(content)
				file.close()
				