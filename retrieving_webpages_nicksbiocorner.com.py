import urllib.request
fhand = urllib.request.urlopen('http://nicksbiocorner.com')
for line in fhand:
    print(line.decode().strip())