from DAL.Db_Connection import ConnectSQL
import re

class DBM():


    def __Convert_to_correct_values(self,productvalue):
        s1=str(productvalue)
        r=re.findall(r"\d",s1)
        r1="".join(r)
        return r1

    def INsertAddProduct(self,product):
        
        self.mycursor=ConnectSQL().cursor()
        query1="""
            insert into T_Product(Title,City,Score,Price,Delivery) values(?,?,?,?,?)
            """
        self.mycursor.execute(query1,product.title,product.city,product.score,int(self.__Convert_to_correct_values(product.price)),product.delivery)
        self.mycursor.commit()
        self.mycursor.close()
        return 1

    def INsertNewProductFromTK(self,product):
        self.db=ConnectSQL()
        self.mycursor=self.db.cursor()
        query1="""
            insert into T_Product(Title,City,Score,Price,Delivery) values(?,?,?,?,?)
            """
        self.mycursor.execute(query1,product[0],product[1],product[2],int(product[3]),product[4])
        self.mycursor.close()
        self.db.commit()
        self.db.close()
        return 1
    
    def searchbyproduct(self,productid):
        self.db=ConnectSQL()
        self.mycursor=self.db.cursor()
  
        self.mycursor.execute("EXEC Usp_Getproductbyid @productid = ?", (productid))
        rows = self.mycursor.fetchall()
        self.mycursor.close()   
        self.db.close()     
        return rows
    
    def deletebyproductid(self,productid):
        self.db=ConnectSQL()
        self.mycursor=self.db.cursor()    
        self.mycursor.execute("EXEC Usp_deletebyproductid @productid = ?", (productid))    
        self.mycursor.close()
        self.db.commit()
        self.db.close() 

