from project_market import *

Market = market()
print("""***********************************
SUMER SPOTIFY

1.Show Market
2.Show Detailed Market
3.Search Product By Barcode
4.Add Product
5.Delete Product
6.Update Cost
7.Sort By Cost
8.Sort By Name
9.Filter Products By Cost
Q:Exit

***********************************""")
while True:
    c = input("Operation: ")
    if c == 'Q':
        print("Goodbye")
        Market.unconnect()
        break
    else:
        c = int(c)
        if c == 1:
            Market.show()
        elif c == 2:
            Market.show_detailed()
        elif c == 3:
            barcode = input("Barcode ")
            Market.search_barcode(barcode)
        elif c == 4:
            Product = input("Product: ")
            type = input("Type: ")
            expiration_date = input("Expiration Date: ")
            Barcode = input("Barcode: ")
            Cost = input("Cost: ")
            item = product(Product,type,Barcode,expiration_date,Cost)
            Market.add(item)
        elif c == 5:
            Product = input("Product: ")
            Market.delete(Product)
        elif c == 6:
            Product = input("Product: ")
            n_cost = input("New Cost: ")
            Market.update_cost(n_cost,Product)
        elif c == 7:
            k = input("Sort by cost (0 For Ascending Order 1 For Descending Order): ")
            Market.sort_by_cost(k)
        elif c == 8:
            k = input("Sort by Name (0 For Ascending Order 1 For Descending Order): ")
            Market.sort_by_name(k)
        elif c == 9:
            type = input("Smaller Or Bigger (<,>): ")
            limit = int(input("Cost Limit: "))
            Market.cost_filter(limit,type)
        else:
            print("Coming Soon...")
