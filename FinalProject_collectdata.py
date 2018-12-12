from bs4 import BeautifulSoup
import requests
import sqlite3
import json
import codecs
import re
import sys
import unittest
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)



CACHE_FNAME = 'data_cache.json'
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    CACHE_DICTION = json.loads(cache_contents)
    cache_file.close()
    print(type(CACHE_DICTION))
    print("CACHE_DICTION has some data")

# if there was no file, no worries. There will be soon!
except:
    CACHE_DICTION = {}
    print("CACHE_DICTION is empty")

def get_unique_key(url):
    return url


def make_request_using_cache(url):
    unique_ident = get_unique_key(url)
    print(type(CACHE_DICTION))
    if unique_ident in CACHE_DICTION:
        print("Getting cached data...")
        return CACHE_DICTION[unique_ident]
    else:
        print("Making a request for new data...")
        # Make the request and cache the new data
        resp = requests.get(url)
        CACHE_DICTION[unique_ident] = resp.text
        dumped_json_cache = json.dumps(CACHE_DICTION)
        fw = open(CACHE_FNAME,"w")
        fw.write(dumped_json_cache)
        fw.close() # Close the open file
        return CACHE_DICTION[str(unique_ident)]


def get_stocknumber(url):
    baseurl=url
    page_text=make_request_using_cache(baseurl)
    page_soup = BeautifulSoup(page_text, 'html.parser')
    content = page_soup.find_all('a')
    url_text=[]
    for i in content:
        url_text.append(i.get('href'))
    stock_number=[]
    for i in url_text:
        if i!=None:
            id=i.find('sz')
            if id != -1:
                stock_number.append(i[id:id+8])
    stock_number.remove(stock_number[1])
    stock_number.remove(stock_number[0])

    return stock_number



def get_stockinf(stock_number,total_number):
    factor1=[]
    factor2=[]
    factor3=[]
    factor4=[]
    factor5=[]
    factor6=[]
    factor7=[]
    factor8=[]
    factor9=[]
    factor10=[]
    factor11=[]
    factor12=[]
    factor13=[]
    factor14=[]
    price=[]
    count=0
    stocknumber=[]
    for i in stock_number:
        detailUrl = 'https://gupiao.baidu.com/stock/'
        stockUrl = detailUrl + i + '.html'
        stock_text=make_request_using_cache(stockUrl)
        if stock_text==None:
            continue
        stock_soup = BeautifulSoup(stock_text, 'html.parser')
        if stock_soup==None:
            continue
        stock_content1=stock_soup.find(class_ = "line1")
        if stock_content1==None:
            continue
        stock_content2=stock_soup.find(class_ = "line2")
        if stock_content2==None:
            continue
        stock_content3=stock_soup.find(class_ = "_close")
        if stock_content3==None:
            continue
        data1=stock_content1.find_all('dd')
        if data1==None:
            continue
        data2=stock_content2.find_all('dd')
        if data2==None:
            continue
        if data1[8].string=='--':
            continue

        if data1[0].string=='--':
            continue
        count+=1
        #print(stockUrl)
        #print(i)
        stocknumber.append(i)
        factor1.append(re.findall("\d+.\d",data1[7].string)[0])
        factor2.append(re.findall("\d+.\d",data1[8].string)[0])
        factor3.append(re.findall("\d+.\d",data1[9].string)[0])
        factor4.append(re.findall("\d+.\d",data1[10].string)[0])
        factor5.append(re.findall("\d+.\d",data2[7].string)[0])
        factor6.append(re.findall("\d+.\d",data2[8].string)[0])
        factor7.append(re.findall("\d+.\d",data2[9].string)[0])
        factor8.append(re.findall("\d+.\d",data2[10].string)[0])
        factor9.append(re.findall("\d+.\d",data1[1].string)[0])
        factor10.append(re.findall("\d+.\d",data1[5].string)[0])
        factor11.append(data1[6].string)
        factor12.append(data2[1].string)
        factor13.append(data2[5].string)
        factor14.append(data2[6].string)
        price.append(stock_content3.string)

        if count>(total_number-1):
            list1=[factor1,factor2,factor3,factor4,factor5,factor6,factor7,factor8,price]
            list2=[factor9,factor10,factor11,factor12,factor13,factor14]
            break
    return list1, list2,stocknumber


DBNAME = 'stock.db'

data_stock = []
conn = sqlite3.connect('stock.db')
cur = conn.cursor()

def create_table1(var1,price,var2,var3,var4,var5,var6,var7,var8,var9):
    statement = '''
    DROP TABLE IF EXISTS 'table1';
    '''
    cur.execute(statement)
    statement = '''
            CREATE TABLE 'table1' (
                'ID' INTEGER PRIMARY KEY AUTOINCREMENT,
                'Stock_number' TEXT NOT NULL,
                'Circulation_market_value' TEXT NOT NULL,
                'Stock_price'TEXT NOT NULL,
                'PE_ratio' TEXT NOT NULL,
                'Earnings_per_share' TEXT NOT NULL,
                'Total_share' TEXT NOT NULL,
                'Total_market_value' TEXT NOT NULL,
                'PB_ratio' TEXT NOT NULL,
                'Net_asset_per_share' TEXT NOT NULL,
                'Circulating_share_capital' TEXT NOT NULL

            );
        '''

    cur.execute(statement)

    for i in range(len(var1)):
        insertion = (i+1, var1[i],price[i],var2[i],var3[i],var4[i], var5[i], var6[i],var7[i],var8[i],var9[i])
        statement = 'INSERT INTO "table1"'
        statement += 'VALUES (?, ?, ?, ?, ?, ?, ?, ?,?,?,?)'
        cur.execute(statement,insertion)

    conn.commit()
    pass

def create_table2(var1,var2,var3,var4,var5,var6,var7):
    statement = '''
    DROP TABLE IF EXISTS 'table2';
    '''
    cur.execute(statement)
    statement = '''
            CREATE TABLE 'table2' (
                'ID' INTEGER PRIMARY KEY AUTOINCREMENT,
                'Stock_number' TEXT NOT NULL,
                'Volume' TEXT NOT NULL,
                'Turnover' TEXT NOT NULL,
                'Commission' TEXT NOT NULL,
                'Hand_turnover_rate' TEXT NOT NULL,
                'Amplitude' TEXT NOT NULL,
                'Volume_ratio' TEXT NOT NULL);
        '''
    cur.execute(statement)

    for i in range(len(var1)):
        insertion = (i+1, var1[i], var2[i],var3[i],var4[i], var5[i], var6[i],var7[i])
        statement = 'INSERT INTO "table2"'
        statement += 'VALUES (?, ?, ?, ?, ?, ?, ?,?)'
        cur.execute(statement,insertion)

    conn.commit()
    pass





####running part####

print('-----Data Access and Storage-----')
total_stock_number=get_stocknumber('http://quote.eastmoney.com/stocklist.html')
print('Get stcok number from ShenZhen Security Market ')
a=input('tpye yes to check whole stock number:')
if a=='yes':
    for i in total_stock_number:
        print(i)
count=input('number of stocks you want to get:')
print('start getting data from website')
stock_inf=get_stockinf(total_stock_number,200)
create_table1(stock_inf[2], stock_inf[0][0],stock_inf[0][8],stock_inf[0][1],stock_inf[0][2], stock_inf[0][3], stock_inf[0][4],stock_inf[0][5],stock_inf[0][6],stock_inf[0][7])
create_table2(stock_inf[2], stock_inf[1][0],stock_inf[1][1],stock_inf[1][2], stock_inf[1][3], stock_inf[1][4],stock_inf[1][5])
print('finish data Data Access and Storage, run the FinalProject_dataprocessing_presentation.py file ')
