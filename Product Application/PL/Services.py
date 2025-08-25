import sys
sys.path.insert(0, 'C:/Users/digi kala/Desktop/Python/App1')
from DAL.Db_Connection import ConnectSQL
from DAL.Db_Management import DBM

def GetProductList():
    db=ConnectSQL()
    mycursor=db.cursor()
    mycursor.execute("select * from V_ProductList")
    product=mycursor.fetchall()
    mycursor.close()
    db.close()
    return product

def AddNewProduct(product):
    DBM1=DBM()
    DBM1.INsertNewProductFromTK(product)

def chacksrarchvalu(productid):
    DBM1=DBM()
    val=DBM1.searchbyproduct(productid)
    return val

def deletproduct(productid):
    DBM1=DBM()
    DBM1.deletebyproductid(productid)


def GetProductcitylist(productcity):
    db=ConnectSQL()
    mycursor=db.cursor()
    str1="select * from V_ProductList where City=N'"
    str1+=productcity
    str1+="'"
    mycursor.execute(str1)
    product=mycursor.fetchall()
    mycursor.close()
    db.close()
    return product
