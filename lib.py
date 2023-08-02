from urllib.request import urlopen


f = urllib.request.urlopen('https://jsonplaceholder.typicode.com/posts')

p = f.read().decode()
print(p)
