
# cafeteria orders and bills display 
# take order 
# deliver the order 
# generate bill 
# print the bill  

# first print the menucard 
# take input in list (if entered item is not present then display the product is unavlible ..) 
# once order is delevered then note it down with the price and mark as it delevered . 
# after this calculate the total amount and generte the bill and display to the user. 

class cafeBerlin(): 
    orderinputList = []
    orderItemsAvailabe=[]
    def displayMenu(li): 
        print("Please order from this today !!!!!")
        li.orderItemsAvailabe =  ['Wadapav','Meggie','Virgin-mohito','Cold-drinks','Paratha','Chocolate'] 
        return(li.orderItemsAvailabe) 
        

    def orderInput(self,orderS= None) :  
        self.orderS = orderS
        orderS = input("What would you want sir ....") 
        orderS = orderS.capitalize()
        if orderS.isalpha  and orderS in self.orderItemsAvailabe: 
            self.orderinputList.append(orderS) 
        else : 
            print("enter the valid item and availale item from the above list !!! ") 
        
        return(self.orderinputList) 

    def orderBillGenerator(self):
        total = 0 
        # print(len(self.orderinputList))
        print("="*30)
        for i in range(len(self.orderinputList)): 
            if self.orderinputList[i] == 'Wadapav': 
                # wadapav is for 60 
                total = total + 60  
                print(f"{self.orderinputList[i]}-{" "* 10}Rs.{60}")
                continue 
            elif self.orderinputList[i] == 'Meggie': 
                total = total + 100  
                print(f"{self.orderinputList[i]}-{" "* 10}Rs.{100}")
                 # Meggie is for 100 
                continue 
            elif self.orderinputList[i] == 'Virgin-mohito': 
                total = total + 120 
                print(f"{self.orderinputList[i]}-{" "* 10}Rs.{120}")
                continue
            elif self.orderinputList[i] == 'Cold-drinks': 
                total += 50  
                print(f"{self.orderinputList[i]}-{" "* 10}Rs.{50}")
                continue
            elif self.orderinputList[i] == 'Paratha': 
                total += 60 
                print(f"{self.orderinputList[i]}-{" "* 10}Rs.{60}") 
                continue
            elif self.orderinputList[i] == 'Chocolate':
                total += 70 
                print(f"{self.orderinputList[i]}-{" "* 10}Rs.{70}")
                continue
            else : 
                continue
        print("="*30)
        return(f"total bill for your cart is Rs.{total}")

ob = cafeBerlin() 
# print(ob.displayMenu()) 
# print(ob.orderInput()) 
# print(ob.orderBillGenerator()) 

def returnTheOutput(): 
    print(ob.displayMenu())  
 
    while True: 
        ans = input("Add items or Exit:  'Y/N':  ") 
        ans = ans.capitalize() 
        if ans == 'Y': 
            print(ob.orderInput()) 
           
        elif ans == 'N' : 
            if len(ob.orderinputList) == 0: 
                print("you dont have any Cart") 
            else: 
                print(ob.orderBillGenerator()) 
            break
        else : 
            print("enter Y/N")
            
    return "Your bill is printed : "

print(returnTheOutput())