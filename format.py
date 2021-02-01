#python3 format.py

with open('pass') as f:
   for line in f:
       hashedpwd = line.split(":")[0] 
       password = line.split(":")[1]

       with open('hash') as g:
          for hashline in g:
          	username = hashline.split(":")[0]
          	hashedpwdhash = hashline.split(":")[3]
          	if (hashedpwd == hashedpwdhash):
          		print("| " + username + " | " + password, end = '')
