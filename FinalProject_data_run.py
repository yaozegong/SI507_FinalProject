import sqlite3 as sqlite
import json
import codecs
import sys
import unittest
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.offline as offline
from plotly import __version__
import statsmodels.api as sm
import numpy as np
from statsmodels.stats.outliers_influence import summary_table
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)



####'-----Data Processing-----'
#### extract the data from SQL####

conn = sqlite.connect('stock.db')
cur = conn.cursor()
cur.execute('SELECT * FROM table1')
Stock_information1=[]
Stock_number=[]
list_of_dic1=[]
for i in cur:
    Stock_information1.append(i)
conn.close()
for i in Stock_information1:
    dic={'Stock_number':i[1],'Circulation_market_value':float(i[2]),'Stock_price':float(i[3]),'PE_ratio':float(i[4]),'Earnings_per_share':float(i[5]),'Total_share':float(i[6]),'Total_market_value':float(i[7]),'PB_ratio':float(i[8]),'Net_asset_per_share':float(i[9]),'Circulating_share_capital':float(i[10])}
    list_of_dic1.append(dic)




conn = sqlite.connect('stock.db')
cur = conn.cursor()
cur.execute('SELECT * FROM table2')
Stock_information2=[]
list_of_dic2=[]
for i in cur:
    Stock_information2.append(i)
    dic={'Stock_number':i[1],'Volume':float(i[2]),'Turnover':float(i[3]),'Commission':i[4],'Hand_turnover_rate':i[5],'Amplitude':i[6],'Volume_ratio':i[7]}
    list_of_dic2.append(dic)

conn.close()


####create the class stock1 to save the information from table1 for each stock####

class stock1(object):
    def __init__(self,stock_diction):
        self.Stock_number =stock_diction['Stock_number']
        self.Circulation_market_value = stock_diction['Circulation_market_value']
        self.Stock_price=stock_diction['Stock_price']
        self.PE_ratio =stock_diction['PE_ratio']
        self.Earnings_per_share =stock_diction['Earnings_per_share']
        self.Total_share =stock_diction['Total_share']
        self.Total_market_value =stock_diction['Total_market_value']
        self.PB_ratio =stock_diction['PB_ratio']
        self.Net_asset_per_share =stock_diction['Net_asset_per_share']
        self.Circulating_share_capital =stock_diction['Circulating_share_capital']

    def __str__(self):
    	return "{}: The price is {}, Total market value is {} hundred million, PE_ratio is {},Earnings_per_share is {}.".format(self.Stock_number,self.Stock_price,self.Total_market_value, self.PE_ratio,self.Earnings_per_share)


####create the class stock2 to save the information from table2 for each stock####
class stock2(object):
    def __init__(self,stock_diction):
        self.Stock_number =stock_diction['Stock_number']
        self.Volume = stock_diction['Volume']
        self.Turnover =stock_diction['Turnover']
        self.Commission =stock_diction['Commission']
        self.Hand_turnover_rate =stock_diction['Hand_turnover_rate']
        self.Amplitude =stock_diction['Amplitude']
        self.Volume_ratio =stock_diction['Volume_ratio']

    def __str__(self):
    	return "{}: The volume is {} ten thousand,The Turnover is {} ten thousand,The Turnover_rate is {}.".format(self.Stock_number,self.Volume,self.Turnover,self.Hand_turnover_rate)


#### Create the function to rank the stock by different factors####
def rank_stock(list_of_dic1,type):
    lst_objects1=[stock1(elem) for elem in list_of_dic1]
    if type=='Circulation_market_value':
        sorted_by_Circulation_market_value = sorted(lst_objects1, key=lambda obj: obj.Circulation_market_value, reverse=True)
        print('ranked by Circulation_market_value')
        for i in sorted_by_Circulation_market_value:
            print(i,end="")
            print(' ',end="")
            print('Circulation_market_value is',end="")
            print(' ',end="")
            print(i.Circulation_market_value)
        return sorted_by_Circulation_market_value
    if type=='Stock_price':
        sorted_by_Stock_price = sorted(lst_objects1, key=lambda obj: obj.Stock_price, reverse=True)
        print('ranked by Stock_price')
        for i in sorted_by_Circulation_market_value:
            print(i,end="")
            print(' ',end="")
            print('Stock_price is',end="")
            print(' ',end="")
            print(i.Stock_price)
        return sorted_by_Stock_price

    elif type=='PE_ratio':
        sorted_by_PE_ratio = sorted(lst_objects1, key=lambda obj: obj.PE_ratio, reverse=True)
        print('ranked by PE_ratio')
        for i in sorted_by_PE_ratio:
            print(i,end="")
            print(' ',end="")
            print('PE_ratio',end="")
            print(' ',end="")
            print(i.PE_ratio)
        return sorted_by_PE_ratio
    elif type=='Earnings_per_share':
        sorted_by_Earnings_per_share = sorted(lst_objects1, key=lambda obj: obj.Earnings_per_share, reverse=True)
        print('ranked by Earnings_per_share')
        for i in sorted_by_Earnings_per_share:
            print(i,end="")
            print(' ',end="")
            print('Earnings_per_share',end="")
            print(' ',end="")
            print(i.Earnings_per_share)
        return sorted_by_Earnings_per_share
    elif type=='Total_share':
        sorted_by_Total_share = sorted(lst_objects1, key=lambda obj: obj.Total_share, reverse=True)
        print('ranked by Total_share')
        for i in sorted_by_Total_share:
            print(i,end="")
            print(' ',end="")
            print('Total_share',end="")
            print(' ',end="")
            print(i.Total_share)
        return sorted_by_Total_share
    elif type=='Total_market_value':
        sorted_by_Total_market_value = sorted(lst_objects1, key=lambda obj: obj.Total_market_value, reverse=True)
        print('ranked by Total_market_value')
        for i in sorted_by_Total_market_value:
            print(i,end="")
            print(' ',end="")
            print('Total_market_value',end="")
            print(' ',end="")
            print(i.Total_market_value)
        return sorted_by_Total_market_value
    elif type=='PB_ratio':
        sorted_by_PB_ratio = sorted(lst_objects1, key=lambda obj: obj.PB_ratio, reverse=True)
        print('ranked by sorted_by_PB_ratio')
        for i in sorted_by_PB_ratio:
            print(i,end="")
            print(' ',end="")
            print('PB_ratio',end="")
            print(' ',end="")
            print(i.PB_ratio)
        return sorted_by_PB_ratio
    elif type=='Net_asset_per_share':
        sorted_by_Net_asset_per_share = sorted(lst_objects1, key=lambda obj: obj.Net_asset_per_share, reverse=True)
        print('ranked by sorted_by_Net_asset_per_share')
        for i in sorted_by_Net_asset_per_share:
            print(i,end="")
            print(' ',end="")
            print('Net_asset_per_share',end="")
            print(' ',end="")
            print(i.Net_asset_per_share)
        return sorted_by_Net_asset_per_share
    elif type=='Circulating_share_capital':
        sorted_by_Circulating_share_capital = sorted(lst_objects1, key=lambda obj: obj.Circulating_share_capital, reverse=True)
        print('ranked by sorted_by_Circulating_share_capital')
        for i in sorted_by_Circulating_share_capital:
            print(i,end="")
            print(' ',end="")
            print('Circulating_share_capital',end="")
            print(' ',end="")
            print(i.Circulating_share_capital)
        return sorted_by_Circulating_share_capital



#### get the basic information about each stock by its stocknumber####
def basic_inf_for_each_stock(stocknumber,list1,list2):
    for i in list1:
        if i['Stock_number']==stocknumber:
            print(i)
    for i in list2:
        if i['Stock_number']==stocknumber:
            print(i)

    return i




####----Data Presentation----####

####create a function to plot the top10 stock's barchart ranked by their total market value####
def plot_barchart_by_top10_Total_market_value(list_of_dic1):
    list_of_Total_market_value=[]
    list_of_stocknumber=[]
    list_of_stockprice=[]
    list_of_PE_ratio=[]
    average_of_PE_ratio_for_allstock=0
    sum=0
    count=0
    lst_objects1=[stock1(elem) for elem in list_of_dic1]
    for i in lst_objects1:
        sum+=i.PE_ratio
    average_of_PE_ratio_for_allstock=(sum/len(lst_objects1))


    sorted_by_Total_market_value = sorted(lst_objects1, key=lambda obj: obj.Total_market_value, reverse=True)
    for i in sorted_by_Total_market_value:
        #print(i)
        a=i.Stock_price
        b=i.PE_ratio
        list_of_stockprice.append('stockprice:'+ str(a)+'Chinese yuan'+'    '+'PE_ratio:'+ str(b)+'   '+'Average_of_PE_ratio_for_allstock:'+str(average_of_PE_ratio_for_allstock))
        list_of_Total_market_value.append(i.Total_market_value)
        list_of_stocknumber.append(i.Stock_number)
        count+=1
        if count>=10:
            break
    trace1 = {"x":list_of_stocknumber,
              "y": list_of_Total_market_value,
             "marker": {
             "color": "rgb(158,202,225)",
             "line": {
                "color": "rgb(8,48,107)",
                "width": 1.5
                 }
               },
              "opacity": 0.6,
              "text":list_of_stockprice,
              "type": "bar"
              }
    data = Data([trace1])
    layout = {"title": "Top_10"}
    fig = Figure(data=data, layout=layout)
    offline.plot(fig)


####create a function to plot the stock's piechart ranked by their total market value####
def plot_piechart_by_Circulation_market_value(list_of_dic1):
    list_of_Total_market_value=[]
    list_of_stocknumber=[]
    list_of_stockprice=[]
    count=0
    lst_objects1=[stock1(elem) for elem in list_of_dic1]
    sorted_by_Total_market_value = sorted(lst_objects1, key=lambda obj: obj.Total_market_value, reverse=True)
    for i in sorted_by_Total_market_value:
        a=i.Stock_price
        c=i.Total_market_value
        list_of_Total_market_value.append(i.Total_market_value)
        list_of_stocknumber.append(i.Stock_number)
        list_of_stockprice.append('Total_market_value:'+str(c)+'bn'+'  '+'stockprice:'+ str(a)+'Chinese yuan')
        #if count>=5:
        #    break
    trace1 = {
      "hoverinfo": ["text", "text", "text", "text", "text"],
      "insidetextfont": {"color": "#FFFFFF"},
      "labels": list_of_stocknumber,
      "marker": {
        "colors": ["rgb(211,94,96)", "rgb(128,133,133)", "rgb(144,103,167)", "rgb(171,104,87)", "rgb(114,147,203)"],
        "line": {
          "color": "#FFFFFF",
          "width": 1
        }
      },
      "showlegend": False,
      "text": list_of_stockprice,
      "textinfo": "label+percent",
      "textposition": ["inside", "inside", "inside", "inside", "inside"],
      "type": "pie",
      "values": list_of_Total_market_value
    }
    data = Data([trace1])
    layout = {
      "hovermode": "closest",
      "margin": {
        "r": 10,
        "t": 25,
        "b": 40,
        "l": 60
      },
      "showlegend": False,
      "title": "United States Personal Expenditures by Categories in 1960",
      "xaxis": {
        "showgrid": False,
        "showticklabels": False,
        "zeroline": False
      },
      "yaxis": {
        "showgrid": False,
        "showticklabels": False,
        "zeroline": False
      }
    }
    fig = Figure(data=data, layout=layout)
    offline.plot(fig)





####create a function do see more information about to10 stock####
def present_top10stock_details(list_of_dic1,list_of_dic2):
    list_of_Total_market_value=[]
    list_of_stocknumber=[]
    list_of_stockprice=[]
    list_of_PE_ratio=[]
    list_of_Earnings_per_share=[]
    list_of_Net_asset_per_share=[]
    list_of_Volume=[]
    list_of_Turnover=[]
    list_of_Commission=[]
    list_of_Hand_turnover_rate=[]
    count=0
    lst_objects1=[stock1(elem) for elem in list_of_dic1]
    lst_objects2=[stock2(elem) for elem in list_of_dic2]
    sorted_by_Total_market_value = sorted(lst_objects1, key=lambda obj: obj.Total_market_value, reverse=True)
    for i in sorted_by_Total_market_value:
        for a in lst_objects2:
            if a.Stock_number==i.Stock_number:
                list_of_Volume.append(a.Volume)
                list_of_Turnover.append(a.Turnover)
                list_of_Commission.append(a.Commission)
                list_of_Hand_turnover_rate.append(a.Hand_turnover_rate)

        list_of_stocknumber.append(i.Stock_number)
        list_of_Total_market_value.append(i.Total_market_value)
        list_of_stockprice.append(i.Stock_price)
        list_of_PE_ratio.append(i.PE_ratio)
        list_of_Earnings_per_share.append(i.Earnings_per_share)
        list_of_Net_asset_per_share.append(i.Net_asset_per_share)

        count+=1
        if count>=10:
            break
    trace1 = {
      "cells": {
        "align": ["left", "center"],
        "fill": {"color": ["rgb(245,245,245)", "rgb(245,245,245)", "rgb(245,245,245)", ["#FF0000", "#FF0000", "#008000", "#008000", "#008000", "#008000", "#008000"]]},
        "font": {
          "color": ["black", "black", "black", ["white", "white", "white", "white", "white", "white", "white"]],
          "size": 20
        },
        "height": 30,
        "line": {"color": "#506784"},
        "values": [
          list_of_stocknumber, list_of_stockprice, list_of_Total_market_value,list_of_PE_ratio,list_of_Earnings_per_share,list_of_Net_asset_per_share,list_of_Volume,list_of_Turnover,list_of_Commission,list_of_Hand_turnover_rate]},
      "columnorder": [1, 2, 3, 4,5,6,7,8,9,10],
      "columnwidth": [200, 200, 200, 200,200,200,200,200,200,200],
      "header": {
        "align": ["left", "center"],
        "fill": {"color": "#119DFF"},
        "font": {
          "color": "white",
          "size": 16
        },
        "height": 35,
        "line": {"color": "black"},
        "values": ["<b>stock_number</b>", "<b>stock_price</b>", "<b>Total_market_value </b>", "<b>PE_ratio</b>", "<b>Earnings_per_share</b>", "<b>Net_asset_per_share</b>", "<b>Volume</b>", "<b>Turnover</b>", "<b>Commission</b>", "<b>list_of_Hand_turnover_rate</b>"]
      },
      "type": "table"
    }
    data = Data([trace1])
    layout = {"margin": {
        "r": 0,
        "t": 0,
        "autoexpand": True,
        "b": 0,
        "l": 0,
        "pad": 0
      }}
    fig = Figure(data=data, layout=layout)
    offline.plot(fig)




####Use liner_regression_model to analyze the relationship bewteen stockprice and other 4 parameters####
def liner_regression_model(list_of_dic1):
    list_of_Total_market_value=[]
    list_of_stockprice=[]
    list_of_PE_ratio=[]
    list_of_Earnings_per_share=[]
    list_of_Net_asset_per_share=[]
    lst_objects1=[stock1(elem) for elem in list_of_dic1]
    for i in lst_objects1:
        list_of_Total_market_value.append(i.Total_market_value)
        list_of_stockprice.append(i.Stock_price)
        list_of_PE_ratio.append(i.PE_ratio)
        list_of_Earnings_per_share.append(i.Earnings_per_share)
        list_of_Net_asset_per_share.append(i.Net_asset_per_share)

    y=np.array(list_of_stockprice)
    print(len(y))
    x1=np.array(list_of_Total_market_value)
    x2=np.array(list_of_PE_ratio)
    x3=np.array(list_of_Earnings_per_share)
    x4=np.array(list_of_Net_asset_per_share)
    x= np.column_stack((x1,x2,x3,x4))


    regr=sm.OLS(y,x)
    gls_results = regr.fit()
    print(gls_results.summary())
    trace1 = {
      "x": list_of_PE_ratio,
      "y":list_of_stockprice,
      "name": "2008",
      "type": "scatter",
      "uid": "f907e8"
    }

    data = Data([trace1])
    layout = {
      "autosize": True,
      "height": 454,
      "title": "Linear Regression",
      "width": 964,
      "xaxis": {
        "autorange": True,
        "range": [0, 5000],
        "title": "PE_ratio",
        "type": "linear"
      },
      "yaxis": {
        "autorange": True,
        "range": [0, 150],
        "title": "stockprice",
        "type": "linear"
      }
    }


    fig = Figure(data=data, layout=layout)
    offline.plot(fig)







print('----Data Processing----')
print('input the parameter and the stock will be ranked by that parameter,type exit to quit')
print('Parameter:Total_market_value Total_share Earnings_per_share PE_ratio Stock_price Circulation_market_value')
type=input('Parameter:')
while(type!='exit'):
    result1=rank_stock(list_of_dic1,'Circulation_market_value')
    a=input('type yes to check the stock number:')
    if a=='yes':
        for i in result1:
            print(i.Stock_number)

    number=input('input a stock_number to see more information about that stock:')
    result2=basic_inf_for_each_stock(number,list1=list_of_dic1,list2=list_of_dic2)

    print('input the parameter and the stock will be ranked by that parameter,type exit to quit')
    print('Parameter:Total_market_value Total_share Earnings_per_share PE_ratio Stock_price Circulation_market_value')
    type=input('Parameter:')

print('----Data Presentation----')
print('input the following 4 key words to check the different type of data presentation')
print('key words:pie,bar,details,regression')
print('input exit to stop')
key=input('input the key words:')
while(key!='exit'):
    if key=='pie':
        plot_piechart_by_Circulation_market_value(list_of_dic1)
    elif key=='bar':
        plot_barchart_by_top10_Total_market_value(list_of_dic1)
    elif key=='details':
        present_top10stock_details(list_of_dic1,list_of_dic2)
    elif key=='regression':
        liner_regression_model(list_of_dic1)
    
    print('input the following 4 key words to check the different type of data presentation')
    print('key words:pie,bar,details,regression')
    print('input exit to stop')
    key=input('input the key words:')



print('run the FinalProject_unittest.py')
