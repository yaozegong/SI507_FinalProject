import unittest
from final_practice import *


class TestDatabase(unittest.TestCase):
    def test_table1_stocknumber(self):
        conn = sqlite.connect('stock.db')
        cur = conn.cursor()
        sql = 'SELECT Stock_number FROM table1'
        results = cur.execute(sql)
        result_list = results.fetchall()
        self.assertIn(('sz000001',), result_list)
        conn.close()

    def test_table1(self):
        conn = sqlite.connect('stock.db')
        cur = conn.cursor()
        sql = 'SELECT * FROM table1 WHERE Stock_number="sz000002"'
        results = cur.execute(sql)
        result = results.fetchall()
        self.assertEqual(result[0][1], 'sz000002')
        self.assertEqual(result[0][2], '2451.1')
        self.assertEqual(result[0][3], '25.23')
        self.assertEqual(result[0][4], '14.9')
        self.assertEqual(result[0][5], '1.2')
        conn.close()

    def test_table2(self):
        conn = sqlite.connect('stock.db')
        cur = conn.cursor()
        sql = 'SELECT * FROM table2 WHERE Stock_number="sz000001"'
        results = cur.execute(sql)
        result = results.fetchall()

        self.assertEqual(result[0][1], 'sz000001')
        self.assertEqual(result[0][2], '29.7')
        self.assertEqual(result[0][3], '3.1')
        self.assertEqual(result[0][4], '-72.06%')
        self.assertEqual(result[0][5], '0.17%')
        self.assertEqual(result[0][6], '0.85%')
        self.assertEqual(result[0][7], '1.28')
        conn.close()


class TestDatSructure(unittest.TestCase):
    def test_dataStructure(self):
        self.assertEqual(list_of_dic1[0]['Stock_number'],'sz000001')

class TestRank_function(unittest.TestCase):
    def test_rank(self):
        result=rank_stock(list_of_dic1,'Circulation_market_value')
        self.assertEqual(result[0].Circulation_market_value,2633.5)

    def test_basic_inf_for_each_stock(self):
        result=basic_inf_for_each_stock('sz000002',list1=list_of_dic1,list2=list_of_dic2)
        self.assertEqual(result['Volume'],2.0)

class Testdata_presentation(unittest.TestCase):
    def test_plot_piechart_by_Circulation_market_value(self):
        try:
            plot_piechart_by_Circulation_market_value(list_of_dic1)
        except:
            self.fail()


    def test_plot_barchart_by_top10_Total_market_value(self):
        try:
            plot_barchart_by_top10_Total_market_value(list_of_dic1)
        except:
            self.fail()

    def test_plot_barchart_by_top10_Total_market_value(self):
        try:
            present_top10stock_details(list_of_dic1,list_of_dic2)

        except:
            self.fail()










if __name__ == "__main__":
	unittest.main(verbosity=2)
