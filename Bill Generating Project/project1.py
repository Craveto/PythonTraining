import pyodbc
import os 
from datetime import datetime 

# printing the bill and storing the orders in a table connection with database . 

# this is my rough work flow for this program 
# -----------------------------------------
# create a database : menu and orders(this is for all time record )
# connection with database 
# taking input from user and store it on database 
# after the input retrive the data from orders table and generate the bill  
# print the bill  
# also write bill in the file to give that file as a copy of bill to the user  
# ------------------------------------------

# connection with database  

conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=CRAVETO;'
    'DATABASE=hotel;'
    'Trusted_Connection=yes;'

) 
cursor = conn.cursor()  
li = cursor.execute('select *from menuCart') 

# all the items are stored in dict cart  
cart = {}
for i in li:
    # print(i) 
    cart[i[0]] = {i[1] : i[2]}

# -----------------------------------------------------------------

def listItmes(): 
    li = cursor.execute('select *from menuCart') 
    print("{:^30}".format('Item List')) 
    print('-'*35)
    print("{:<4} {:<5} {:>12}".format('id','item','price'))
    for i in li : 
        print(f"{i[0]} - {i[1]:12} - {i[2]:.2f}".format('id','item','','price'))  
    
    print('-'*35)
    return "Enter Id to select the item Sir/Mam...😊  \n"

      


# ------------------------------------------

def takeInputFromUser():
    li = []
    while True: 
      userInuput = input(f"Enter Id (1-7) or 0 to exit: ")

      if userInuput.isdigit()  and  userInuput != '0':  
         if int(userInuput) in [1,2,3,4,5,6,7]:
            quantity = input("Enter quantity: ")
            if (userInuput.isdigit() and quantity.isdigit()) and (int(userInuput) in [1,2,3,4,5,6,7]) : 
              li.append((int(userInuput),int(quantity))) 
         else :
            print("input is not in (1,2,3,4,5,6,7)") 

      elif userInuput == '0' :  
          break 
      else : 
          print("Invalid input : enter proper input !!!") 

    print("Your item is being ready 🔃")
    return li  
   
# print(takeInputFromUser())   # output : (id,quantity) [(2, 1), (3, 5)]

# ------------------------------------------------------------------------ 

# generating the bill 
def billPrinting(tuplist):  
    print("{:^50}".format("Snehal's cafe"))
    print('-'*55)
    print("{:} {:>6} {:>13} {:>13} {:>15}".format('Id','Item', 'Quantity', 'TotalPrice','OrigionalPrice'))
    li = cursor.execute('select id, price,name from menuCart') 

    sumTotal = 0 
    li = list(li) 
    for item in tuplist :  
        total =0 
        for i in li : 
           if int(item[0]) == int(i[0]): 
              total = i[1] * item[1]
              sumTotal += total
              print(f"{item[0]} {i[2]:>10} {item[1]:>7} {total:>12.2f} {i[1]:>13.2f}".format()) 
              d = datetime.now()
              cursor.execute('insert into orders (id, name , quantity, orderDate) values(?,?,?,?)',(item[0],i[2],item[1],d))
              conn.commit()
           else: 
            continue 
        continue  
    print('-'*55)  
    return f"total bill is : {sumTotal:>17.2f}".format()

# ------------------------------------------------------------------------------------------------------


# final function to call all functions 
def finalCall(): 
   
   print(listItmes()) 
   userInputVal = takeInputFromUser() 
   
   print("Please pay the Amount for Receipt")

   print(billPrinting(userInputVal)) 

   return "Your bill generated successfully !!✅"
   
print(finalCall())



cursor.close()
conn.close()



