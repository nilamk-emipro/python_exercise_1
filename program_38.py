# Write a program having classes as Product, Order, Customer
# a.Do appropriate inheritance of the above classes
# b.Write appropriate methods / constructors in each classes
# c.Following output is expected
#     1.Order No : SO001
#     2.Customer : Sanjay Patel
#     3.Customer Email : sanjay@dummy.com
#     4.Name of the product is 'Pencil'
#     5.Product Qty is : 15
#     6.Unit Price is 20
#     7.Order total is : 300


class Product():
    def __init__(self, Qty, Price):
        self.Qty = Qty
        self.Price = Price

    def print_prod_details(self):
        print("Product Qty is :", self.Qty)
        print("Unit Price is :", self.Price)
        print("Total Order is :", self.Qty * self.Price)

class Customer:
    def __init__(self,Name,EmailAdd):
        self.Name = Name
        self.EmailAdd = EmailAdd

    def print_cust_details(self):
        print("Customer :", self.Name)
        print("Customer Email :", self.EmailAdd)

class Order(Product,Customer):
    def __init__(self, Orderno,qty,price,custname,customeremail):
        self.Orderno = Orderno
        Product.Qty=qty
        Product.Price=price
        Customer.Name=custname
        Customer.EmailAdd=customeremail

    def print_order_details(self):
       print("Product No :", self.Orderno)

prod1=Order("SO001",15,20,"Sanjay Patel","sanjay@dummy.com")
prod1.print_order_details()
prod1.print_cust_details()
prod1.print_prod_details()




