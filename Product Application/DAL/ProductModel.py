from DAL.persian_typerv import *

class Prroduct :
    def __init__(self,title,city,score,price,delivery):
        self.title=title
        self.city=city
        self.score=score
        self.price=price
        self.delivery=delivery

    def __str__(self):
        return f"{type_persian(self.title)}\t{type_persian(self.city)}\t{self.score}\t{self.price}\t{type_persian(self.delivery)}"