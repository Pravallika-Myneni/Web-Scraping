from bs4 import BeautifulSoup
import urllib.request,urllib.parse,urllib.error
import ssl

ctx=ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode=ssl.CERT_NONE

url = 'https://www.funda.nl/koop/eindhoven/huis-41134687-waterfront-459/'
response = urllib.request.urlopen(url,context= ctx).read()
#soup = BeautifulSoup(response,'html.parser')
#print(soup.prettify())

#a=soup.find_all('div',class_='object-kenmerken-body')
print(response)