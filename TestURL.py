import urllib.request
with urllib.request.urlopen('http://hillapp-env.eba-pwi4s6pp.us-east-1.elasticbeanstalk.com/users') as response:
#with urllib.request.urlopen('https://jsonplaceholder.typicode.com/users') as response:
   html = response.read()
   header=response.headers
   print(html)
   print(header)


   # Always start with
   #source venv/bin/activate
   # export FLASK_APP="application.py"  
   #flask run