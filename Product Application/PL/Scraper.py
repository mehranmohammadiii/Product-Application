import sys
sys.path.insert(0, 'C:/Users/digi kala/Desktop/Python/App1')
import requests
from bs4 import BeautifulSoup
import re
from DAL.ProductModel import Prroduct

class Scrap:
    def __init__(self,url):
        self.res=requests.get(url)
        self.soup=BeautifulSoup(self.res.content,"html.parser")
    
    def GetListProductTag(self):
        productlist=[]
        for item in self.soup.select("div.SPPLyJ") :
            try :
                self.titlee=item.select_one("h2").text.strip()
            except :
                self.titlee=""
            try :
                self.c=item.select_one("span.fkclky")
                self.city=self.c.contents[0].strip()
            except :
                self.city=""
            try :
                self.score=item.select_one("span.V938ul").text.strip()
            except :
                self.score=""
            try :
                self.p=item.select_one("span.VVeeBY")
                self.pric=self.p.contents[0]
            except :
                self.pric=""
            try :
                self.d=item.select_one("div.T_9fEo").text
                self.delivery=re.findall(r"(ارسال رایگان)",self.d)[0]
            except :
                self.delivery="" 
            p1=Prroduct(self.titlee,self.city,self.score,self.pric,self.delivery)
            productlist.append(p1)
        return productlist