###Description
I will use my code to crawl multiple web pages and get the basic stock information for Chinese ShenZhen Security Market.


Using the git bush to run my code.
### File  Run FinalProject_collectdata.py
Input the number(1-1500),you could get the exact number of stock¡¯s information. The number <400 will be better, or it could cost so much time.Then, the information will be saved into a SQL file named stock.db.It includes two tables,table1 and table2.
###Detail about FinalProject_collectdata.py
1.Crawling the page:http://quote.eastmoney.com/stocklist.html to get the stock number.
2. Combing the stock with the Url:https://gupiao.baidu.com/stock/stocknumber.htlm to get more information about each stock.
###File Run FinalProject_data_run.py

###Detail about  FinalProject_data_run.py
Data Process
1.Getting the data from SQL, and saving as a list of dictionaries.
The key of the dictionaries should be the stock factor, like Stock_number,Stock_price,ect. We could check the key in line 30 and line 43. 
2.Creating two class to save more information about each stock from the dictionary, and return a standard str as the stock information by def __str__(self)
3.Function rank_stock. It will rank the stock by the parameter you input,like Stock_number,Stock_price,ect, it will also print out this information.
4.Function basic_inf_for_each_stock. The input should be the stock number it shows on the screen, and it will print out more information about that stock.
Data Presentation
1.Function  plot_piechart_by_total_market_value(). It will show the proportion of each stock by its total market value.
2.Function plot_barchart_by_top10_Total_market_value(). It will show the top10 stock¡¯s market value,stock price,PB_ration on the bar chart.
3.Function present_top10stock_details() Create a table to see more information about top10 stock,
4.Function liner_regression_model() By using this function, we will see the relationship between stockprice and Total_market_value,PE_ratio,Earning_per_Share,Net_asset_per_share. Use the statsmodels module to do the regression analysis. Then we find the.PE_ratio correlates more with stock_price. The we plot the linear regression picture based on these two factors.
 
###Detail about Run FinalProject_unittest.py
I also created another file called final_practice.py which is same with FinalProject_data_run.py But it does not contain the input function. The final_practice.py is used to import all information for testing.
1.test_table1_stocknumber() and test_table1() These two functions are used to test the data from stock.db(SQL file) table1
2.test_table2() This function is used to test the data from stock.db(SQL file) table2.
3.test_dataStructure() This function is used to test list_of_dictionary created in the FinalProject_data_run.py
4.Class TestRank_function() The functions in this class are used to test the function created in FinalProject_data_run.py .
5.Testdata_presentation()The functions in this class are used to test the data presentation part created in FinalProject_data_run.py .

###Command instruction
Following the instructions showed on the git bush screen.
Input the key words showed on the git bush screen.

