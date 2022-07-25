import sqlite3
class product():
    def __init__(self,name,type,barcode,expiration_date,cost):
        self.name = name
        self.type = type
        self.barcode = barcode
        self.expiration_date = expiration_date
        self.cost = cost
    def __str__(self):
        return "Product: {}\nType: {}\nBarcode: {}\nExpiration Date: {}\nCost: {}".format(self.name,self.type,self.barcode,self.expiration_date,self.cost)
    def __len__(self):
        print("Cost: {}".format(self.cost))

class market():
    def __init__(self):
        self.connect = sqlite3.connect("database.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Market (Product TEXT,Type TEXT,Barcode TEXT,Expiration_Date TEXT,Cost FLOAT)")
        self.connect.commit()
    def unconnect(self):
        self.connect.close()
    def show_detailed(self):
        self.cursor.execute("SELECT * FROM Market")
        market = self.cursor.fetchall()
        if len(market) == 0:
            print("Market is empty")
        else:
            for i in market:
                item = product(i[0],i[1],i[2],i[3],i[4])
                print(item)
    def show(self):
        self.cursor.execute("SELECT Product,Cost FROM Market")
        market = self.cursor.fetchall()
        if len(market) == 0:
            print("Market is empty")
        else:
            for i in market:
                print("Product: {} - Cost: {}\n".format(i[0],i[1]))
    def cost_filter(self,limit,type):
        self.cursor.execute("SELECT * FROM Market")
        items = self.cursor.fetchall()
        if len(items) == 0:
            print("Market is empty")
        else:
            if type == "<":
                for i in items:
                    if i[4] < limit:
                        item = product(i[0],i[1],i[2],i[3],i[4])
                        print(item)
                    else:
                        continue
            else:
                for i in items:
                    if i[4] > limit:
                        item = product(i[0],i[1],i[2],i[3],i[4])
                        print(item)
                    else:
                        continue
    def search_barcode(self,barcode):
        self.cursor.execute("SELECT * FROM Market WHERE Barcode = ?",(barcode,))
        items = self.cursor.fetchall()
        if len(items) == 0:
            print("Product does not exists")
        else:
            for i in items:
                item = product(i[0],i[1],i[2],i[3],i[4])
                print(item)
    def add(self,item):
        self.cursor.execute("INSERT INTO Market VALUES (?,?,?,?,?)",(item.name,item.type,item.barcode,item.expiration_date,item.cost))
        self.connect.commit()
    def delete(self,item):
        self.cursor.execute("SELECT * FROM Market WHERE Product = ?",(item,))
        items = self.cursor.fetchall()
        if len(items) == 0:
            print("Product does not exists")
        else:
            self.cursor.execute("DELETE FROM Market where Product = ?",(item,))
            self.connect.commit()
    def update_cost(self,n_cost,item):
        self.cursor.execute("SELECT * FROM Market WHERE Product = ?",(item,))
        items = self.cursor.fetchall()
        if len(items) == 0:
            print("Product does not exists")
        else:
            self.cursor.execute("UPDATE Market set Cost = ? where Product = ?",(n_cost,item))
            self.connect.commit()
    def sort_by_cost(self,order):
        self.cursor.execute("SELECT * FROM Market")
        items = self.cursor.fetchall()
        if len(items) == 0:
            print("Empty Market")
        else:
            self.cursor.execute("DELETE FROM Market")
            if order == '0':
                items.sort(key = lambda item:item[4])
            else:
                items.sort(key = lambda item:item[4],reverse = True)
            for i in items:
                self.cursor.execute("INSERT INTO Market VALUES (?,?,?,?,?)",(i[0],i[1],i[2],i[3],i[4]))
                self.connect.commit()

    def sort_by_name(self,order):
        self.cursor.execute("SELECT * FROM Market")
        items = self.cursor.fetchall()
        if len(items) == 0:
            print("Empty Market")
        else:
            self.cursor.execute("DELETE FROM Market")
            if order == '0':
                items.sort()
            else:
                items.sort(reverse = True)
            for i in items:
                self.cursor.execute("INSERT INTO Market VALUES (?,?,?,?,?)",(i[0],i[1],i[2],i[3],i[4]))
                self.connect.commit() 