import pickle
import os

class Products:

    def __init__(self,Name,Group,Subgroup,Price):
        
        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()
                ids = list_of_products.keys()
                self.__id = max(ids) + 1
            except:
                self.__id=1
        else:
            self.__id=1
        self._Name=Name
        self._Group=Group
        self._Subgroup=Subgroup
        self._Price=Price

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self._Name
    def setName(self,Name):
        self._Name=Name
    
    def getGroup(self):
        return self._Group
    def setGroup(self,Group):
        self._Group=Group

    def getSubgroup(self):
        return self._Subgroup
    def setSubgroup(self,Subgroup):
        self._Subgroup=Subgroup

    def getPrice(self):
        return self._Price
    def setPrice(self,Price):
        self._Price=Price

class Admin:

    def __init__(self,Name):
        self.__id=1
        self.__Name=Name

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self.__Name
    def setName(self,Name):
        self.__Name=Name

    def ViewProduct(self):

        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()

                if list_of_products:
                    print "**************** Product-List *************************"
                    for i in list_of_products:
                        print list_of_products[i].getId(),list_of_products[i].getName(),list_of_products[i].getPrice(),list_of_products[i].getGroup(),list_of_products[i].getSubgroup()

                    print "**************** END *************************"

                else:
                    print "No Product Found"
            except:
                print "No Product Found"
        else:
            print "No Product Found"

    
    def AddProduct(self):
        try:
            Name = raw_input("Enter Name of Product")
            Price = int(raw_input("Enter Price"))
            Group = raw_input("Enter Group")
            Subgroup = raw_input("Enter Subgroup")

            p = Products(Name,Group,Subgroup,Price)

            list_of_products = {1:Products}
            list_of_products.clear()
            
            if os.path.isfile("product.pickle"):
                try:
                    pickle_in = open("product.pickle","rb")
                    list_of_products = pickle.load(pickle_in)
                    pickle_in.close()
                    list_of_products[p.getId()] = p
                    pickle_in = open("product.pickle","wb")
                    pickle.dump(list_of_products,pickle_in)
                    pickle_in.close()
                except:
                    list_of_products[p.getId()] = p
                    pickle_in = open("product.pickle", 'wb')
                    pickle.dump(list_of_products,pickle_in)
                    pickle_in.close()

            else:
                list_of_products[p.getId()] = p
                pickle_in = open("product.pickle", 'wb')
                pickle.dump(list_of_products,pickle_in)
                pickle_in.close()

            print "Product has been added successfully"
        except:
            print "Price must be in integer"
    

    def DeleteProduct(self):

        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()
                if list_of_products:
                    try:
                        id = int(raw_input("Enter ID of a product you want to Delete"))
                        if id in list_of_products:
                            del list_of_products[id]
                            pickle_in = open("product.pickle","wb")
                            pickle.dump(list_of_products,pickle_in)
                            pickle_in.close()
                            print "Product has been deleted successfully"

                        else:
                            print "Id does not exist"
                    except:
                        print "Please Enter Valid ID"
                else:
                   print "There is no product to Delete"
            except:
                print "There is no product to Delete"
        else:
            print "There is no product to Delete"
            

    def ModifyProduct(self):

        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()
                if list_of_products:
                    try:
                        id = int(raw_input("Enter ID of a product you want to Update"))
                        
                        if id in list_of_products:
                            try:
                                Name = raw_input("Enter Name of Product")
                                Price = int(raw_input("Enter Price"))
                                Group = raw_input("Enter Group")
                                Subgroup = raw_input("Enter Subgroup")
                                #p = Products(Name,Group,Subgroup,Price)
                                p=list_of_products[id]
                                p.setName(Name)
                                p.setPrice(Price)
                                p.setGroup(Group)
                                p.setSubgroup(Subgroup)
                                list_of_products[id]=p
                                pickle_in = open("product.pickle","wb")
                                pickle.dump(list_of_products,pickle_in)
                                pickle_in.close()
                                print "Product has been modified successfully"
                            except:
                                print "Price must be in integer"

                        else:
                            print "Id does not exist"
                    except:
                        print "Please Enter Valid ID"
                else:
                   print "There is no product to Modify"
            except:
                print "There is no product to Modify"
        else:
            print "There is no product to Modify"
            

    def MakeShipment(self):
        pass

    def ConfirmDelivery(self):
        pass
        

class Customer:
    
    def __init__(self,Name,Address,PhnNo):
        if os.path.isfile("customer.pickle"):
            try:
                pickle_in = open("customer.pickle","rb")
                list_of_customers = pickle.load(pickle_in)
                pickle_in.close()
                ids = list_of_customers.keys()
                self.__id=max(ids)+1
            except:
                self.__id=1
        else:
            self.__id=1
        self._Name=Name
        self._Address=Address
        self._PhnNo=PhnNo

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self._Name
    def setName(self,Name):
        self._Name=Name

    def getAddress(self):
        return self._Address
    def setAddress(self,Address):
        self._Address = Address

    def getPhnNo(self):
        return self._PhnNo
    def setPhnNo(self,PhnNo):
        self._PhnNo = PhnNo

    def BuyProduct(self):
        
        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()
                try:
                    id = int(raw_input("Enter id of a product you want to buy"))
                    if id in list_of_products:
                        self.MakePayment(id,list_of_products)
                    else:
                        print "ID does not exist"
                except:
                    print "Please Enter Valid ID"
            except:
                print "No product found"
        else:
            print "No product found"

    def ViewProduct(self):

        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()

                if list_of_products:
                    print "**************** Product-List *************************"
                    for i in list_of_products:
                        print list_of_products[i].getId(),list_of_products[i].getName(),list_of_products[i].getPrice(),list_of_products[i].getGroup(),list_of_products[i].getSubgroup()

                    print "**************** END *************************"

                else:
                    print "No Product Found"
            except:
                print "No Product Found"
        else:
            print "No Product Found"

    def MakePayment(self,id,list_of_products):
        print "Please pay ",list_of_products[id].getPrice()," Amount"
        CT = raw_input("Enter CardType")
        CNO = raw_input("Enter CardNo")

        py = Payment(list_of_products[id].getName(),CT,CNO)
        if os.path.isfile("payment.pickle"):
            try:
                pickle_in = open("payment.pickle","rb")
                list_pay = pickle.load(pickle_in)
                pickle_in.close()
                paylist  = list_pay[self.__id]
                paylist.append(py)
                list_pay[self.__id] = paylist
                pickle_in = open("payment.pickle","wb")
                pickle.dump(list_pay,pickle_in)
                pickle_in.close()
                print "Payment Completed"
            except:
                pay = []
                pay.append(py)
                list_pay = {1:pay}
                list_pay.clear()
                list_pay[self.__id] = pay
                pickle_in = open("payment.pickle","wb")
                pickle.dump(list_pay,pickle_in)
                pickle_in.close()
                print "Payment Completed"
        else:
            pay = []
            pay.append(py)
            list_pay = {1:pay}
            list_pay.clear()
            list_pay[self.__id] = pay
            pickle_in = open("payment.pickle","wb")
            pickle.dump(list_pay,pickle_in)
            pickle_in.close()
            print "Payment Completed"

        if os.path.isfile("cart.pickle"):
            try:
                pickle_in = open("cart.pickle","rb")
                list_cart = pickle.load(pickle_in)
                pickle_in.close()     
                ct = list_cart[self.__id]
                pList = ct.getProductList()
                f=0
                for item in pList:
                    if item.getId() == id:
                        f=1
                        break
                if f==1:
                    DeleteFromCart(id)
            except:
                pass


    def ViewCart(self):
        if os.path.isfile("cart.pickle"):
            try:
                pickle_in = open("cart.pickle","rb")
                list_cart = pickle.load(pickle_in)
                pickle_in.close()
                if list_cart:
                    ct = list_cart[self.__id]
                    x = ct.getProductList()
                    if x:
                        print "************** Cart ***********************"
                        for i in x:
                            print i.getId(),i.getName(),i.getGroup(),i.getSubgroup()
                        print "Total = ",ct.getTotal()
                        print "************** END ***********************"
                    else:
                        print "No item found in your cart"
                else:
                    print "No item found in your cart"
            except:
                print "No item found in your cart"
        else:
            print "No item found in your cart"

    def AddToCart(self):
        
        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()
                x = []
                list_cart = {1:x}
                list_cart.clear()
                if list_of_products:
                    try:
                        id = int(raw_input("Enter Id of a product you want to add"))
                        if id in list_of_products:
                            p = list_of_products[id]
                            if os.path.isfile("cart.pickle"):
                                try:
                                    pickle_in = open("cart.pickle","rb")
                                    list_cart = pickle.load(pickle_in)
                                    pickle_in.close()
                                    if list_cart:
                                        ct = list_cart[self.__id]
                                        x = ct.getProductList()
                                        total = ct.getTotal() + p.getPrice()
                                        Number = ct.getNumberOfProducts()+1
                                        x.append(p)
                                        ct.setProductList(x)
                                        ct.setTotal(total)
                                        ct.setNumberOfProducts(Number)
                                        list_cart[self.__id] = ct
                                        pickle_in = open("cart.pickle","wb")
                                        pickle.dump(list_cart,pickle_in)
                                        pickle_in.close()
                                    else:
                                        x.append(p)
                                        total = p.getPrice()
                                        ct = Cart(1,total,x,self.__id)
                                        list_cart[self.__id] = ct
                                        pickle_in = open("cart.pickle","wb")
                                        pickle.dump(list_cart,pickle_in)
                                        pickle_in.close()
                                except:
                                    x.append(p)
                                    total = p.getPrice()
                                    ct = Cart(1,total,x,self.__id)
                                    list_cart[self.__id] = ct
                                    pickle_in = open("cart.pickle","wb")
                                    pickle.dump(list_cart,pickle_in)
                                    pickle_in.close()
                            else:
                                x.append(p)
                                total = p.getPrice()
                                ct = Cart(1,total,x,self.__id)
                                list_cart[self.__id] = ct
                                pickle_in = open("cart.pickle","wb")
                                pickle.dump(list_cart,pickle_in)
                                pickle_in.close()
                        else:
                            print "Id does not exist"
                    except:
                        print "Please Enter Valid ID"
                else:
                    print "No product found"
            except:
                print "No product found"

        else:
            print "No product found"

    def DeleteFromCart(self,id=0):
        if os.path.isfile("cart.pickle"):
            try:
                pickle_in = open("cart.pickle","rb")
                list_cart = pickle.load(pickle_in)
                pickle_in.close()
                if list_cart:
                    ct = list_cart[self.__id]
                    x = ct.getProductList()
                    if x:
                        try:
                            if id==0:
                                id = int(raw_input("Enter ID you want to remove from cart"))
                            f=0
                            for item in x:
                                if item.getId() == id:
                                    p=item
                                    f=1
                                    break
                            if f>0:
                                x.remove(p)
                                number = ct.getNumberOfProducts()-1
                                total = ct.getTotal() - p.getPrice()
                                ct.setTotal(total)
                                ct.setNumberOfProducts(number)
                                ct.setProductList(x)
                                list_cart[self.__id] = ct
                                pickle_in = open("cart.pickle","wb")
                                pickle.dump(list_cart,pickle_in)
                                pickle_in.close()

                            else:
                                print "Id does not exist"
                        except:
                            print "Please Enter valid ID"
                    else:
                        print "No item found in your cart"
                else:
                    print "No item found in your cart"
            except:
                print "No item found in your cart"
        else:
            print "No item found in your cart"

    def BuyCart(self):
        if os.path.isfile("cart.pickle"):
            try:
                pickle_in = open("cart.pickle","rb")
                list_cart = pickle.load(pickle_in)
                pickle_in.close()
                if list_cart:
                    if list_cart[self.__id]:
                        ct = list_cart[self.__id]
                        print "Total amount to pay",ct.getTotal(),"Rs"
                        CT = raw_input("Enter CardType")
                        CNO = raw_input("Enter CardNo")
                        plist = ct.getProductList()
                        listname=""
                        for pname in plist:
                            if listname=="":
                                listname = pname.getName()
                            else:
                                listname = listname +","+ pname.getName()
                        py = Payment(listname,CT,CNO)
                        if os.path.isfile("payment.pickle"):
                            pickle_in = open("payment.pickle","rb")
                            list_pay = pickle.load(pickle_in)
                            pickle_in.close()
                            paylist  = list_pay[self.__id]
                            paylist.append(py)
                            list_pay[self.__id] = paylist
                            pickle_in = open("payment.pickle","wb")
                            pickle.dump(list_pay,pickle_in)
                            pickle_in.close()
                            print "Payment Completed"
                        else:
                            pay = []
                            pay.append(py)
                            list_pay = {1:pay}
                            list_pay.clear()
                            list_pay[self.__id] = pay
                            pickle_in = open("payment.pickle","wb")
                            pickle.dump(list_pay,pickle_in)
                            pickle_in.close()
                            print "Payment Completed"
                        del list_cart[self.__id]
                        pickle_in = open("cart.pickle","wb")
                        pickle.dump(list_cart,pickle_in)
                        pickle_in.close()
                    else:
                        print "No product found in cart"
                else:
                    print "No product found in cart"
            except:
                print "No product found in cart"
        else:
            print "No product found in cart"
    
    def history(self):
        if os.path.isfile("payment.pickle"):
            try:
                pickle_in = open("payment.pickle","rb")
                list_pay = pickle.load(pickle_in)
                pickle_in.close()
                paylist  = list_pay[self.__id]
                if paylist:
                    print "************** History ***********************"
                    for item in paylist:
                        print item.getName(),item.getCardType(),item.getCardNo()
                    print "************** END ***********************"
                else:
                    print "No history found"
            except:
                print "No history found"
        else:
            print "No history found"


class Cart:
    
    def __init__(self,NumberOfProducts,Total,ProductList,customer_id):
        self.__id=1
        self.customer_id=customer_id
        self._NumberOfProducts = NumberOfProducts
        self._Total = Total
        self.ProductList=ProductList

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id = id

    def getNumberOfProducts(self):
        return self._NumberOfProducts
    def setNumberOfProducts(self,NumberOfProducts):
        self._NumberOfProducts = NumberOfProducts

    def getTotal(self):
        return self._Total
    def setTotal(self,Total):
        self._Total = Total

    def getProductList(self):
        return self.ProductList
    def setProductList(self,ProductList):
        self._ProductList = ProductList


class Payment:
    
    def __init__(self,Name,CardType,CardNo):
        self.__id=1
        self.Name = Name
        self.__CardType = CardType
        self.__CardNo = CardNo

    def getId(self):
        return self.__id
    def setId(self,id):
        self.__id=id

    def getName(self):
        return self.Name
    def setName(self,Name):
        self.__Name=Name

    def getCardType(self):
        return self.__CardType
    def setCardType(self,CardType):
        self.__CardType=CardType

    def getCardNo(self):
        return self.__CardNo
    def setCardNo(self,CardNo):
        self.__CardNo=CardNo

class Guest:
    
    def ViewProducts(self):

        if os.path.isfile("product.pickle"):
            try:
                pickle_in = open("product.pickle","rb")
                list_of_products = pickle.load(pickle_in)
                pickle_in.close()

                if list_of_products:
                    print "**************** Product-List *************************"
                    for i in list_of_products:
                        print list_of_products[i].getId(),list_of_products[i].getName(),list_of_products[i].getPrice(),list_of_products[i].getGroup(),list_of_products[i].getSubgroup()

                    print "**************** END *************************"

                else:
                    print "No Product Found"
            except:
                print "No Product Found"
        else:
            print "No Product Found"

    def GetRegistered(self):
        Name = raw_input("Enter Name")
        PhnNo = raw_input("Enter Phone number")
        Address = raw_input("Enter Address")

        c = Customer(Name,Address,PhnNo)
        list_of_customers = {1:Customer}
        list_of_customers.clear()
        
        if os.path.isfile("customer.pickle"):
            pickle_in = open("customer.pickle","rb")
            list_of_customers = pickle.load(pickle_in)
            pickle_in.close()
            list_of_customers[c.getId()] = c
            pickle_in = open("customer.pickle","wb")
            pickle.dump(list_of_customers,pickle_in)
            pickle_in.close()

        else:
            list_of_customers[c.getId()] = c
            pickle_in = open("customer.pickle", 'wb')
            pickle.dump(list_of_customers,pickle_in)
            pickle_in.close()

        print  "Your ID - ",c.getId()
        print "Must Remember"
        # for i in list_of_customers:
        #     print list_of_customers[i].getName()
        
while 1:
    print "1 for Admin"
    print "2 for Customer"
    print "3 for Guest"
    print "0 for exit"
    try:
        choice = int(raw_input())

        if choice == 1:
            name = raw_input("Enter Admin Name")
            a = Admin(name)
            while 1:
                print "1 to AddProduct"
                print "2 to ViewProduct"
                print "3 to DeleteProduct"
                print "4 to ModifyProduct"
                print "0 to exit"
                # print "5 to MakeShipment"
                # print "6 to ConfirmDelivery"
                admin_choice = int(raw_input())

                if admin_choice == 1:
                    a.AddProduct()
                elif admin_choice == 2:
                    a.ViewProduct()
                elif admin_choice == 3:
                    a.ViewProduct()
                    a.DeleteProduct()
                elif admin_choice == 4:
                    a.ViewProduct()
                    a.ModifyProduct()
                elif admin_choice == 0:
                    break
                else:
                    print "Please make valid choice"

        elif choice == 2:
            id = int(raw_input("Enter Customer Id"))
            pickle_in = open("customer.pickle","rb")
            list_of_customers = pickle.load(pickle_in)
            pickle_in.close()
            c = list_of_customers[id]
            if c:
                while 1:
                    print "1 to BuyProduct"
                    print "2 to ViewProduct"
                    print "3 to AddToCart"
                    print "4 to DeleteFromCart"
                    print "5 to BuyCart"
                    print "6 to see history"
                    print "7 to ViewCart"
                    #print "7 to MakePayment"
                    print "0 to exit"
                    customer_choice = int(raw_input())
                    if customer_choice == 1:
                        c.ViewProduct()
                        c.BuyProduct()
                    elif customer_choice == 2:
                        c.ViewProduct()
                    elif customer_choice == 3:
                        c.ViewProduct()
                        c.AddToCart()
                    elif customer_choice == 4:
                        c.ViewCart()
                        c.DeleteFromCart()
                    elif customer_choice == 5:
                        c.ViewCart()
                        c.BuyCart()
                    elif customer_choice == 6:
                        c.history()
                    elif customer_choice == 7:
                        c.ViewCart()
                    elif customer_choice == 0:
                        break
                    else:
                        print "Please make valid choice"
            else:
                print "Unauthorized Customer"

        elif choice == 3:
            g = Guest()
            while 1:
                print "1 to ViewProducts"
                print "2 to GetRegistered"
                print "0 to exit"
                guest_choice = int(raw_input())
                if guest_choice == 1:
                    g.ViewProducts()
                elif guest_choice == 2:
                    g.GetRegistered()
                    break
                elif guest_choice == 0:
                    break
                else:
                    print "Please make valid choice"
        elif choice == 0:
            break
        else:
            print "Please make valid choice"
    except:
        print "Please make valid choice"
