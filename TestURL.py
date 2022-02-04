import urllib.request
#with urllib.request.urlopen('http://hillapp-env.eba-pwi4s6pp.us-east-1.elasticbeanstalk.com') as response:
with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users') as response:
   html = response.read()
   print(html)