Bosses = {"irfan" : "irfan123"}
Employees = {}
#Employeeler sipariş alacaklar. Customerlar sepeti güncelleyebilirler employeeler için ayrı bir sipariş ekranı oluşturulabilir

class Employee:
    def __init__(self,id,password):
        self.id = id
        self.password = password

class Boss(Employee):
    coffeelist = []
    coffee_pricelist = []
    coffee_with_price = []
    dessertlist= []
    dessert_pricelist = []
    dessert_with_price = []
    
    def __init__(self,id,password):
        super().__init__(id,password)

    def update_coffee_with_price():
        Boss.coffee_with_price = list(zip(Boss.coffeelist, Boss.coffee_pricelist))
    
    def add_coffee(self):
        coffee = str(input("Add A Coffee: "))
        Boss.coffeelist.append(coffee)
        price = float(input("Enter The Price:"))
        Boss.coffee_pricelist.append(price)
        Boss.update_coffee_with_price()
        print(f"Coffee '{coffee}' added with price {price}$!")
        print("\n")
    
    def update_dessert_with_price():
        Boss.dessert_with_price = list(zip(Boss.dessertlist, Boss.dessert_pricelist))

    def add_dessert(self):
        dessert = str(input("Add A Coffee: "))
        Boss.dessertlist.append(dessert)
        price = float(input("Enter The Price:"))
        Boss.dessert_pricelist.append(price)
        Boss.update_dessert_with_price()
        print(f"Dessert '{dessert}' added with price {price}$!")
        print("\n")

    def create_employee(self):
        id = input("Enter the employee's name: ")
        password = input("Enter the password (default: '123'): ")
        if id not in Employees:
            Employees[id] = Employee(id,password)
            print("Employee added successfully!")
            print("\n")
        else:
            print("This employee name is already registered!")

def Coffee_Menu():
    print("\nCoffee Menu:")
    for index, (coffee, price) in enumerate(Boss.coffee_with_price, start=1):
        print(f"{index}. {coffee}: {price:.2f}$")

def Dessert_Menu():
    print("\nDessert Menu:")
    for index, (dessert, price) in enumerate(Boss.dessert_with_price, start=1):
        print(f"{index}. {dessert}: {price:.2f}$")

class shopping_basket():
    order_list = []  
    total_cost = 0
    while True:
        print("\nShopping Basket:")
        print("1. Add Coffee")
        print("2. Add Dessert")
        print("3. View Basket")
        print("4. Checkout")
        print("0. Exit Basket")
        choice = int(input("Choose an option: "))

        if choice == 1:
            Coffee_Menu()
            coffee_choice = int(input("Enter the coffee number to add: "))
            if 1 <= coffee_choice <= len(Boss.coffee_with_price):
                coffee, price = Boss.coffee_with_price[coffee_choice - 1]
                order_list.append((coffee, price))  
                total_cost += price  
                print(f"Added {coffee} ({price:.2f}$) to basket! Current total: {total_cost:.2f}$")
            else:
                print("Invalid choice. Try again.")
        
        elif choice == 2:
            Dessert_Menu()
            dessert_choice = int(input("Enter the dessert number to add: "))
            if 1 <= dessert_choice <= len(Boss.dessert_with_price):
                dessert, price = Boss.dessert_with_price[dessert_choice - 1]
                order_list.append((dessert, price))  
                total_cost += price 
                print(f"Added {dessert} ({price:.2f}$) to basket! Current total: {total_cost:.2f}$")
            else:
                print("Invalid choice. Try again.")
        
        elif choice == 3:
            print("\nYour Basket:")
            if not order_list:
                print("Your basket is empty!")
            else:
                for index, (item, price) in enumerate(order_list, start=1):
                    print(f"{index}. {item}: {price:.2f}$")  # Her ürün ve fiyat
                print(f"Total Cost: {total_cost:.2f}$")  # Toplam ücret
        
        elif choice == 4:
            print("\nCheckout Summary:")
            if not order_list:
                print("Your basket is empty!")
            else:
                for index, (item, price) in enumerate(order_list, start=1):
                    print(f"{index}. {item}: {price:.2f}$")  # Her ürün ve fiyat
                print(f"Total Cost: {total_cost:.2f}$")  # Toplam ücret
            print("Thank you for your purchase!")
            break
        
        elif choice == 0:
            print("Exiting shopping basket...")
            break
        
        else:
            print("Invalid choice, please try again!")

def login():
    while True:
        id = str(input("Username: "))
        password = str(input("Password: "))
        if id in Employees and Employees[id].password == password :
            print(f"Welcome {id}")
            print("\n")
            return Employee_Menu()
            
        elif id in Bosses and Bosses[id] == password :
            print(f"Welcome {id}!")
            print("\n")
            return Boss_Menu()            
        
        else:
            print("Invalid password or username")
            print("\n")
            return login()
            


def Main_Menu():
    while True:
        print("\nWelcome!")
        print("1 for Boss")
        print("2 for Employee")
        print("3 for Customers")
        choice = int(input("Choose an option: "))
        if choice == 1:
            return login()
        elif choice == 2:
            return login()
        elif choice == 3:
            return Menu()
    
def Menu():
    while True:
        print("\n Welcome to Sline")
        print("1 for Coffee Menu")
        print("2 for Dessert Menu")
        print("3 for Shopping Basket")
        print("0 to Exit")
        choice = int(input("Choose an option: "))
        if choice == 3:
            shopping_basket()
        elif choice == 1:
            Coffee_Menu()
        elif choice == 2:
            Dessert_Menu()
        elif choice == 0:
            print("Exiting menu...")
            break
        else:
            print("Invalid choice, please try again!")
            return choice
        
def Boss_Menu():
    while True:
        print("1 for Add Coffee")
        print("2 for Add Dessert")
        print("3 for Add An Employee")
        print("4 for Returning Main Menu")
        print("0 to Exit")
        choice = int(input("Choose an option: "))
        if choice == 1:
            Boss.add_coffee(self = super) #Static Function Call: Super ile classtan fncyi çekmek için bu yapıyı kullanıyoruz
            return Boss_Menu()
        elif choice == 2:
            Boss.add_dessert(self = super)
            return Boss_Menu()
        elif choice == 3:
            Boss.create_employee(self = super)
            return Boss_Menu()
        elif choice == 4:
            return Main_Menu()
        elif choice == 0:
            print("Exiting menu...")
            break
        else:
            print("Invalid choice, please try again!")
            return choice
        
def Employee_Menu():
    while True:
        print("1 for Checking Basket")
        print("2 for Getting Purchase")
        print("3 for Return Main Menu")
        choice = int(input("Choose an option: "))

        if choice == 1:
            print("\nYour Basket:")
            if not shopping_basket.order_list:
                print("Your basket is empty!")
                
            else:
                for index, (item, price) in enumerate(shopping_basket.order_list, start=1):
                    print(f"{index}. {item}: {price:.2f}$")  # Her ürün ve fiyat
                print(f"Total Cost: {shopping_basket.total_cost:.2f}$")  # Toplam ücret
        
        elif choice == 2:
            print("\nCheckout Summary:")
            if not shopping_basket.order_list:
                print("Your basket is empty!")
            else:
                for index, (item, price) in enumerate(shopping_basket.order_list, start=1):
                    print(f"{index}. {item}: {price:.2f}$")  # Her ürün ve fiyat
                print(f"Total Cost: {shopping_basket.total_cost:.2f}$")  # Toplam ücret
            print("Thank you for your purchase!")

        elif choice == 3:
            return Main_Menu()
    
user = Main_Menu()

