import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
from datetime import date
file = open('Stock Prices.csv','w+')
csv_writer= csv.writer(file)
csv_writer.writerow(['Stock Code','Code name','Current time','Price','Full Date'])
stock_codes=['MRNA','MSFT','AAPL','NKE','SQ','CRM','V','WMT','FB','TSLA','NVDA']
cols=[]
for stock_code in stock_codes:
    link = 'https://finance.yahoo.com/quote/'+stock_code+'?p='+stock_code
    page = requests.get(link).text
    soup = BeautifulSoup(page,'lxml')
    name = soup.find('h1',class_='D(ib) Fz(18px)').text
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    price = soup.find('div',class_='D(ib) Mend(20px)').span.text
    cols.append([stock_code,name,current_time,price,date.today()])
for col in cols:
    csv_writer.writerow(col)
    print('Stock code : ',col[0],'\nStcok Full name : ',col[1],'\nTime Checked: ',col[2],'\nStock Price : ',col[3],'\nFull date : ',col[4],'\n')
    