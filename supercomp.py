from bs4 import BeautifulSoup
import requests,openpyxl

excel=openpyxl.Workbook()
print(excel.sheetnames)
sheet=excel.active
sheet.title="supercomputers"
print(excel.sheetnames)

sheet.append(["rank","sys","processor","country","cores","rmax","rpeak","power"])

url = requests.get("https://top500.org/statistics/sublist/")
doc = BeautifulSoup(url.content, 'html.parser')


for tr in doc.find_all('tr')[1:]:
    tds = tr.find_all('td')
    rank=tds[0].text
    s1=tds[1].a.text.split(',')
    sys=tds[1].a.text.split(',')[0]
    processor=tds[1].a.text.split(',')[1]
    country=tds[1].find_all('br')[-1].next_sibling
    cores=tds[2].text
    rmax=tds[3].text
    rpeak=tds[4].text
    power=tds[5].text
    sheet.append([rank,sys,processor,country,cores,rmax,rpeak,power])
excel.save("D:\Jupyter\Python\Web Scraping\supercomputers.xlsx")