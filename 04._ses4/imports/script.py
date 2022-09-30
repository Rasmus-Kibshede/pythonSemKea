import sys
import os
import subprocess

#pip install requests i en docker container
import requests

def greeting(x):
    print(x)


greeting(sys.argv)

# os
# os.listdir()
# os.mkdir('Test')

# subprosess
# subprocess.run(['ls'])
# subprocess.run(['git', 'clone', 'github repo link'])

res = requests.get('http://kea.dk')
print(res.text)

f = open('api.json', 'w')
f.write(res)




