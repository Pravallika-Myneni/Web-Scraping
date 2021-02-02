from bs4 import BeautifulSoup
from selenium import webdriver
import csv

def write_to_csv(funda):
    with open('Funda.csv','w') as csvfile:
        writer= csv.DictWriter(csvfile,fieldnames= columns)
        writer.writeheader()
        writer.writerows(funda)


def find_values(url):
    driver = webdriver.Chrome('C:\Program Files\chromedriver_win32\chromedriver.exe')
    #url=input('Enter url:  ')
    #url = 'https://www.funda.nl/koop/eindhoven/huis-41126640-waterwereld-120/'
    driver.maximize_window()
    driver.get(url)

    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content,"html.parser")
    a = soup.findAll("dd",{'class':'fd-flex--bp-m fd-align-items-center'})
    driver.quit()

    mapp={0:'cost',1:'Offered Since',8:'Living Usable Area',10:'total plot'}
    df={}
    l=[0,1,8,10]
    for i in l:
        df[mapp[i]]=a[i].text.strip()
    return df


columns = ['cost','Offered Since','Living Usable Area','total plot']
funda=[]
n=int(input())
for i in range(n):
    url=input("Enter URL: ")
    k=find_values(url)
    funda.append(k)
    print("completed",i,"th url")
write_to_csv(funda)
print("CSV file created Successfully")