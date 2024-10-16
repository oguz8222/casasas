import requests
from bs4 import BeautifulSoup
email = input(" Email Yada id gir   :")
password = input(" Şifre  gir:")
session = requests.Session()
response = session.get("https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&locale2=ar_AR&refid=8")
soup = BeautifulSoup(response.text, 'html.parser')
Mahos = soup.find_all("input", type="hidden")
data = {input.get('name'): input.get('value') for input in Mahos}
data['email'] = email
data['pass'] = password
Facebook = session.post("https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&locale2=ar_AR&refid=8", data=data)
if "m_page_voice" in Facebook.cookies:
    Id = Facebook.cookies["m_page_voice"]
    print(" Başarılı Giriş ✅:", Id)
else:
    print(Facebook.text)
