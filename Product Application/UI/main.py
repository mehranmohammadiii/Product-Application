import sys
sys.path.insert(0, 'C:/Users/digi kala/Desktop/Python/App1')
from DAL.Db_Connection import ConnectSQL
from PL.Scraper import Scrap
from DAL.Db_Management import DBM
import re
from PL.Services import GetProductcitylist

# s1=Scrap("https://basalam.com/cat/apparel/%D8%B3%D8%A7%D8%B9%D8%AA-%D9%85%DA%86%DB%8C")

# d1=DBM()
# for item in s1.GetListProductTag():
#     d1.INsertAddProduct(item)


# dbm1=DBM()
# val=dbm1.searchbyproduct(20)
# print(val)
# val[0][0]=str(val[0][0])
# val[0][4]=str(val[0][4])
# res="\n".join(val[0])
# print(res)
# temp="\n".join(res)

# val=GetProductcitylist("مشهد")
# str1="select * from V_ProductList where City=N'"
# str1+='مشهد'
# str1+="'"
# print(str1)
# print(val)

# print(bool("b"))


