
from bs4 import BeautifulSoup
import requests
import re
import json
rego= "CD63WB"
rego_url= "https://nt.gov.au/driving/rego/check,-renew-or-transfer-your-registration/rego-check/_rest/rego-checkaccess-token"
s = requests.Session()
resp = s.get(rego_url)
y = json.loads(resp.content)
print(y["payload"]["access_token"])
token = y["payload"]["access_token"]
new_url="https://nt.gov.au/driving/rego/check,-renew-or-transfer-your-registration/rego-check/_rest/rego-checksearch?q="+rego+"&access_token="+token
s2 = requests.Session()
page2 = requests.get(new_url)
resp2 = s2.get(new_url)
print(resp2.content)
