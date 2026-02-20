
# index 
# 1)
name = ''' Hi How are you? Starterd learning python.It's really interesting.''' 
# Then what is the output of following code

# · name[:]
# output : Hi How are you? Starterd learning python.It's really interesting.

# · name[-10:-5]
# output: teres

# · name[3:12]
# output:  How are 

# · name[12:3]
# output : ' '

# · name[5,6]
# output: errer 

# · name[-4:-12]
# ouput: ' '

# · name[::2]
# output: iHwaeyu tredlann yhnI' elyitrsig

# · name[::-2]
# output: .nteen larst.otpgire rtaS?o r o H

# ---------------------------------------------------------------------------

# 2)
L1 = [ 'a' , 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major' ]

# a. L1[:]
# print(L1[:])
# output : ['a', 'b', 20, 30, 't', 100, 300, 400, 'Happy', 'major']

# b. L1[::3]
# print(L1[::3]) 
# output: ['a', 30, 300, 'major']


# # c. L1[::-2] 
# print(L1[::-2])     #output ['major', 400, 100, 30, 'b']


# # d. How to extract value “Happy” based on index and negative index
# pri1[-2])  #output: Happy


# # e. How to check type of data in list at 4th position 
# print(type(L1[3])) #output:<class 'int'>

# # f. Extract values for 100, 300, 400 
# print("index for 100 : ",L1.index(100) , " ,index for 300 : " , L1.index(300), ", index of 400 : " , L1.index(400))
#index for 100 :  5  ,index for 300 :  6 , index of 400 :  7
# -----------------------------------------------------------------

# 3)
l2 = [1,2,3,5,['a', 'b', 'work hard'],100 , 200, 'Success']  

# # then what is the output of fol lowing  

# · L2[4]
#['a', 'b', 'work hard']

# # · L2[1:5]   
# [2, 3, 5, ['a', 'b', 'work hard']]

# # · L2[7] success


# # · L2[7][2] c


# # · L7[7][2:] ccess 


# # · L2[ : 3] 1 2 3 


# # · L2[3:]    
# [5, ['a', 'b', 'work hard'], 100, 200, 'Success'] 
# --------------------------------------------------------------------------

# 4)

# 4. From the above l2 value ‘b’ must be changed to ‘BEE’. 
# l2[4][1] = 'BEE' 
# [1, 2, 3, 5, ['a', 'BEE', 'work hard'], 100, 200, 'Success']
# ----------------------------------------------------

# 5. From l2 “BEE” has to discard.  
# l2.pop()    #[1, 2, 3, 5, ['a', 'BEE', 'work hard'], 100, 200]
# print(l2.index('BEE'))    #'BEE' is not in list
# print(l2.index(l2[4][1]))  #'BEE' is not in list

# print(l2)  #  [1, 2, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success']

# ----------------------------------------------------------------


# 6. In l2 add a dictionary at the end {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}
l2.append('{‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}') 
# [1, 2, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', '{‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}']

# ----------------------------------------------------------
# 7. From l2 extract insect information.
# print(l2[8][:])
# {‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}

# ----------------------------------------------------------------
# 8. Create a dictionary d1 = {‘a’:10, ‘b’:20, ‘c’ : 30} and add the d1 at 2nd position of l2
d1 = {'a':10, 'b':20, 'c' : 30}  
l2[1] = d1
# print(l2)        #[1, {'a': 10, 'b': 20, 'c': 30}, 3, 5, ['a', 'b', 'work hard'], 100, 200, 'Success', '{‘insect’: [‘bee’, ‘moth’] , ‘bird’ : [‘parrot’, ‘sparrow’]}']

# ---------------------------------------------------------------------------

# 9. Based on new l2 created here extract the value 10 from l2 dictionary. 
# l = list(l2[1].values())
# print(l[0])    #10 

# ----------------------------------------------------------------

# 10. If l2 =[1,2,3,5, (90,40,50,10), ‘Python’, 400 ,[‘a’, ‘b’, ‘work hard’],100 , 200, “Success”, (200,300,“Hundreds”)] then what is the output of following
L2 = [1,2,3,5, (90,40,50,10), 'Python', 400 ,['a', 'b', 'work hard'],100 , 200, 'Success', (200,300,'Hundreds')]

# · L2[4][2]     #50


# · L2[5][:]  #Python

# · L2[2] [:]    #TypeError: 'int' object is not subscriptable

# · L2[1:5]    #  [2, 3, 5, (90, 40, 50, 10)]

# · L2[5]     #Python

# · L2[5][3:-1]   #ho

# · L2[-1]   (200, 300, 'Hundreds')

# · L2[-4, -3]     TypeError: list indices must be integers or slices, not tuple

# · L2[-4: -10]     []

# · L2[7][2]   work hard

# · L2[-7][2:]     thon

# · L2[ :- 3]      [1, 2, 3, 5, (90, 40, 50, 10), 'Python', 400, ['a', 'b', 'work hard'], 100]

# · L2[-3:]      [200, 'Success', (200, 300, 'Hundreds')]

# ----------------------------------------------------------------------


# 11. Ask user to enter the marks and define if the user got distinction, first class, second class, pass, Fails
# If marks are more than 80 output must be “You got distinction”
# For marks more than 60 output must be “You got First class”
# Marks more than 40 will display “You got second class”
# Marks more than or equal to 35 “PASS” Otherwise Fail 

# if (float(marks) <=100  and float(marks)>=0 and str(marks).isdigit) or (not marks.isalnum and not marks.isalpha) :
#        marks = float(marks)
#        round(marks)
#        if marks > 80 : 
#          print("You got distinction") 
#        elif marks > 60 : 
#          print ("You got First class") 
#        elif marks > 40 : 
#          print ("You got second class") 
#        elif marks >=35 : 
#          print("Pass")
#        else : 
#          print("Fail") 
# else : 
#          print("enter marks in correct format and out of 100 !!")  


# using function 

# in function format : 
# def checkMarks(marks) :  
#        round(marks)
#        if marks > 80 : 
#          return "You got distinction"
#        elif marks > 60 : 
#          return "You got First class"
#        elif marks > 40 : 
#          return "You got second class" 
#        elif marks >=35 : 
#          return "Pass"
#        else : 
#          return "Fail" 

# marks = input("enter your marks : ")
# if (marks.isdigit() and float(marks) <=100  and float(marks)>=0) or (not marks.isalnum and not marks.isalpha) :
#     marks = float(marks)
#     round(marks)
#     print(checkMarks(marks))      
# else : 
#     print("enter marks in correct format and out of 100 !!")   

# ========================================================================================================= 


# 12. Ask user to enter information about salary of the employee per year and rating received as A, B, C, D
# If salary upto 5 lpa then increament based on ratings are A = 16% , B=12%, C= 10%, D=6%
# If salary upto 10 lpa then increament based on ratings are A = 14% , B=10%, C= 8%, D=6%
# If salary upto 15 lpa then increament based on ratings are A = 8% , B=6%, C= 4%, D = no increment
# If salary upto 23 lpa then increament based on ratings are A = 7% , B=5%, C= 4%, D=no 

# function to extract the int value from the string 
# s = '154lpa'
# num = 0 
# for i in range(len(s)): 
#     if s[i].isdigit() : 
#         num = num * 10 + int(s[i])

# print(num) 


# def ratingInc(sal,rating): 
#    if (sal.isdigit() and  float(sal) >= 0 ) or (not sal.isalnum and not sal.isalpha) : 
#      rating = str(rating.upper())
     
#      sal = float(sal) * 100000
#      round(sal)
#    #   print(sal)
#      if sal <= 500000 : 
#          if rating == 'A': 
#            sal = sal + sal * 0.16
#            return  ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'B' : 
#             sal = sal + sal * 0.12
#             return ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'C': 
#             sal = sal + sal * 0.1
#             return ("for rating : ",rating ," your salary will be = ",sal) 

#          elif rating == 'D' : 
#             sal = sal + sal * 0.06
#             return ("for rating : ",rating ," your salary will be = ",sal) 
      
#      elif sal <= 1000000 : 
#          if rating == 'A': 
#            sal = sal + sal * 0.14
#            return  ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'B' : 
#             sal = sal + sal * 0.1
#             return ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'C': 
#             sal = sal + sal * 0.08
#             return ("for rating : ",rating ," your salary will be = ",sal) 

#          elif rating == 'D' : 
#             sal = sal + sal * 0.06
#             return ("for rating : ",rating ," your salary will be = ",sal) 
      
#      elif sal <= 1500000 : 
#          if rating == 'A': 
#            sal = sal + sal * 0.08
#            return  ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'B' : 
#             sal = sal + sal * 0.06
#             return ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'C': 
#             sal = sal + sal * 0.04
#             return ("for rating : ",rating ," your salary will be = ",sal) 

#          elif rating == 'D' : 
#             sal = sal + sal * 0.06
#             return ("for rating : ",rating ," your salary will be = ",sal) 
              
#      elif sal <= 2300000 : 
#          if rating == 'A': 
#            sal = sal + sal * 0.07
#            return  ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'B' : 
#             sal = sal + sal * 0.05
#             return ("for rating : ",rating ," your salary will be = ",sal) 
#          elif rating == 'C': 
#             sal = sal + sal * 0.04
#             return ("for rating : ",rating ," your salary will be = ",sal) 
#    # else : 
#    #    return "enter proper format : "
   
# salr = input("enter salary in lpa only  : ") 
# rating = input("enter rating ")
# print(ratingInc(salr,rating))

# =================================================================================


# 13. Ask user to opt for courses for master degree based on the following
# L1 = [“HR”, “Finance”, “Marketing”, “DS”]
# Based on above subject there are two different streams. For example- HR is having HR core and HR analytics and Marketing is having core and Marketing analytics. Analytics is the optional subject and having added extra fees. DS is not having analytics.
# If fees for L1 is 2 lakhs for each course core subject having the same fees but analytics subject having 10% extra on 2 lakhs.
# If student opts for hostel then 2 lakhs per year is added. For food monthly 2000 .
# Transportation charges 13000 per semester. Calculate the total annual cost based on selected service.
# User will enter values as subject, analytics(Y/N), Hostel (Y/N), food(How many months?), Transportation(semester/annual) . 

# for each to streams (core and analytics )      
    

# sub = input("Enter subject (HR/Finance/Marketing/DS): ").upper()    
# stream = input("Analytics or Core (A/C): ").upper()   
# stay = input("Hostel (Y/N): ").upper()             
# food = int(input("Enter food months: "))      
# transport = input("Transportation (SEMESTER/ANNUAL/NONE): ").upper()        

# def expCal(sub, stream, stay, food, transport): 
#     grandTotal = 0 
    
#     base_fee = 200000
#     if stream == 'A' and sub != 'DS':
#         grandTotal += base_fee + (base_fee * 0.10)
#     else:
#         grandTotal += base_fee

#     if stay == 'Y':
#         grandTotal += 200000  # Hostel fee
    
#     grandTotal += (food * 2000) 
    
#     if transport == 'SEMESTER':
#         grandTotal += 13000
#     elif transport == 'ANNUAL':
#         grandTotal += 13000 * 2
        
#     print(f"\nBreakdown for {sub} ({stream}):")
#     print(f"Total Annual Cost: {grandTotal}")
#     return grandTotal

# expCal(sub, stream, stay, food, transport)

# print(expCal(stream,sub,stay,food,transport)) 



# ======================================================================

# 14. Digitalize the book allotment process for school. Charges are mentioned here in the given table:

standard = { 
    (1,2,3,4):{'Hindi':60 , 'Marathi':60, 'English':80,'Science': 90, 'Maths':100 },
    (5,6,7,8):{'Hindi':100 , 'Marathi':100, 'English':100,'Science': 120, 'Maths':140},
    (9,10):{'Hindi':150 , 'Marathi':150, 'English':150,'Science': 200, 'Maths':250}, 

    'Notebook':{ '100':{ 'Square':40,'4lines':30, '2lines':30, 'SingleLines':60,'A4':100},
                 '200':{ 'Square':40,'4lines':30, '2lines':30, 'SingleLines':60,'A4':100}
                }
}

# ---------------------------------------------------------------


# def findPrices(std,books):
#     li = list(standard.keys()) 
#     books = books.capitalize()
#     for i in range(len(li)) :
#        tup = li[i] 
#        for j in range(len(tup)) : 
#            if std == tup[j] :
#             return standard[tup][books] 

# def findPricesforNotebooks(pages,type) :
#    li = list(standard.keys())
# #    type = type.capitalize()
#    for i in range(len(li)): 
#       tup = li[i] 
#       if tup == 'Notebook' : 
#          li2= list(standard[tup].keys()) 
#          for j in range(len(li2)) : 
#            if li2[j] == pages : 
#              return standard[tup][pages][type]
            
# def runAll(): 
#   total = 0
#   notebookTotal =0
#   countbook = 0
#   countNotebook =0

#   while True: 
#    sel = input('\n'"Book/Notebook/Exit (for grand total)")
#    sel = sel.capitalize()
 
#    if sel == 'Book' : 
#       std = int(input("enter which class books you want : "))
#       bookName = str(input("enter book name Hindi/English/Marathi/Maths/Science: ")) 
#       price = findPrices(std,bookName)
#       print(bookName,"          ",price)
#       total = total + price  
#       countbook += 1
    
#    elif sel == 'Exit' : 
#        print('\n'"your total book amount for ",countbook,"books is : ", total)
#        print('\n'"your notebook total for ",countNotebook,"notebooks is : ",notebookTotal)
#        print('\n''your total bill amount is : ', total + notebookTotal)
#        print('\n')
#        break 
#    elif sel == 'Notebook' : 
#       pages = str(input("how many pages you want 100 or 200: ")) 
#       type1 = str(input("choose: Square/4lines/2lines/Singlelines/A4 "))
#       type1 = type1.capitalize() 
#       notebookTotal = notebookTotal + findPricesforNotebooks(pages,type1)
#       countNotebook +=1

#    else : 
#       print("do you want another book : ") 

# print(runAll())
      

# ====================================================================================== 



# 17. Create 
a=100
# str2 = '100'
# print(float(str2)) 

# · Convert a to string 
# str1 = str(a)                yes
# print(type(str1))
# · Convert a to list 

# li = list(a)    not
# print(li)
# 'int' object is not iterable but string can be change into list 

# · Convert a to tuple
# tup = tuple(a)       not
# print(tup)
# 'int' object is not iterable same as list 

# · Convert a to dict 
# di = dict(a)             not
# print(di) 
# same for all non iterable datatypes cann't be change into iterable datatypes  

# · Convert a to set 
# s = set(a)
# print(s)             not 

# · Convert to float 
# f = float(a)
# print(f)    it will typecast 
# ----------------------------------------------------------------

# 8. Create 
city = 'Pune'

# · Convert to int
# print(int(city))    #ValueError: invalid literal for int() with base 10: 'Pune'

# · Convert float
# print(float(city))   #ValueError: could not convert string to float: 'Pune'

# · Convert list
# print(list(city))    #['P', 'u', 'n', 'e']

# · Convert tuple 
# print(tuple(city))     #('P', 'u', 'n', 'e') 

# · Convert dict 
# print(dict(city))      #ValueError: dictionary update sequence element #0 has length 1; 2 is required

# · Convert set 
# print(set(city))       #{'n', 'P', 'e', 'u'}     

# ----------------------------------------------------------------------- 

# 9. Create a list as 
marks = [20,18,15,17,18]

# · Convert to int 
# print(int(marks))     #ypeError: int() argument must be a string, a bytes-like object or a real number, not 'list' 

# · Convert float 
# print(float(marks))    #TypeError: float() argument must be a string or a real number, not 'list'

# · Convert list   
# print(list(marks)) #[20, 18, 15, 17, 18]

# · Convert tuple 
# print(tuple(marks))   #(20, 18, 15, 17, 18)

# · Convert dict 
# print(dict(marks))    #TypeError: cannot convert dictionary update sequence element #0 to a sequence

# · Convert set    
# print(set(marks))      #{17, 18, 20, 15}

# ---------------------------------------------------------------------------


# List operations

# 10. Create the empty list snames
snames = []

# · Add value 20 in the list using append 
snames.append(20) 
# print(snames)     #[20]

# · Add value 30 in the list using extend
# snames.extend(30)
# print(snames)    #TypeError: 'int' object is not iterable 

# · Add values in the list using append
# for i in range(4): 
#     snames.append(i) 

# print(snames)   #[20, 0, 1, 2, 3]

# · Add value “WORK" in the list using extend
# snames.extend('WORK') 
# print(snames)      #[20, 0, 1, 2, 3, 'W', 'O', 'R', 'K']

# · Create a new list combo having the values [1, ‘a’, ‘b’ ,2 , 3]
# combo = [1,'a','b',2,3]  

# · Add sname to combo using addition operator
# combo = combo + snames 
# print(combo)    #[1, 'a', 'b', 2, 3, 20, 0, 1, 2, 3, 'W', 'O', 'R', 'K']

# · Add combo to snames using append 
# snames.append(combo) 
# print(snames)         #[20, 0, 1, 2, 3, 'W', 'O', 'R', 'K', [1, 'a', 'b', 2, 3, 20, 0, 1, 2, 3, 'W', 'O', 'R', 'K']]

# · Add combo to snames using extend.  
# snames.extend(combo)
# print(snames)               #[20, 0, 1, 2, 3, 'W', 'O', 'R', 'K', [1, 'a', 'b', 2, 3, 20, 0, 1, 2, 3, 'W', 'O', 'R', 'K'], 1, 'a', 'b', 2, 3, 20, 0, 1, 2, 3, 'W', 'O', 'R', 'K']


# -------------------------------------------------------------------- 

# 11. Create one list l1 having two elements and l3 having 7 elements. Now at 4th position add l1
# l1 = [1,2]
# l3 = [2,4,6,7,5,4,3] 
# l3[3] = l1
# print(l3)       #[2, 4, 6, [1, 2], 5, 4, 3]


# 12. Collection is the list having values [1,2,3,[‘a’, ‘b’, ‘c’], 100, ‘Nisha’, 20.50, 90.10 ] if the data is in integer or float then multiply with 5.
Collection = [1,2,3,['a', 'b', 'c'], 100, 'Nisha', 20.50, 90.10 ] 
# for i in range(len(Collection)) : 
#     if type(Collection[i]) in [int,float]: 
#         Collection[i] *= 5
# print(Collection)       #[5, 10, 15, ['a', 'b', 'c'], 500, 'Nisha', 102.5, 450.5]


# · From the collection delete the record for “Nisha” 
# for i in range(len(Collection)-1): 
#     if Collection[i] == 'Nisha':
#         Collection.pop(i)
# print(Collection)               #[1, 2, 3, ['a', 'b', 'c'], 100, 20.5, 90.1]

# · Find the location of 20.50
# print(Collection.index(20.50))    #6 

# 13. Create a comprehensive list for square upto 10 
# l = [x**2 for x in range(11)] 
# print(l)     #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 14. Create the comprehensive list to find number divisible by 13 till 200  
# l = [x for x in range(201) if x%13 == 0 ]
# print(l)       #[0, 13, 26, 39, 52, 65, 78, 91, 104, 117, 130, 143, 156, 169, 182, 195]


# 15. Create the list which is divisible by 4 from 300 to 400 
# l = [x for x in range(300,401) if x%4 == 0] 
# print(l)     #[300, 304, 308, 312, 316, 320, 324, 328, 332, 336, 340, 344, 348, 352, 356, 360, 364, 368, 372, 376, 380, 384, 388, 392, 396, 400]

# 16. Create a comprehensive list to generate list up to x, y as a number. For example if x = 3 list will be x_list = [0,1,2] and y=2 then y_list =[0,1]
# l = [x for x in range(x) x = 3] 
# print(l) 

# Then generate a new list based on all combination of x and y.

# For example: if x = 1 and y =2 then x_list = [0] and y_list = [0,1]

# And output will be [[0,0],[0,1]] 
# x = 1
# y = 2
# x_list = list(range(x)) 
# y_list = list(range(y)) 
# combinations = [[i, j] for i in x_list for j in y_list]
# print(combinations) # Output: [[0, 0], [0, 1]]



# If x=2 and y = 2 then output will be [[0,0],[0,1][1,0],[1,1]]


# 17. What is the difference between add and update methods in set?
# add - to add a single value in set 

# update - to add multiple values in a set  


# 18. What is the difference between append and extend methods in list?
# append - it will add a value at the end of the list  

# extend - to add iterative values in a list as a single character string  


# 19. What is the difference between pop and remove methods? 
# pop - to delete the element from the last  and it takes value as a parameter

# remove - to delete the element from the list from index position wise  


# 20. What is the difference between discard, pop, remove methods? 
# discard- Removes element x from the set 
# remove- Removes element x from the set. 
# pop()- Removes and returns an arbitrary (random) element from the set because sets are unordered. 

# 21. How to create empty set? 
set1 = {}

# 22. Create the set s1 and s2 and perform set operations like union, intersection, difference, set difference.
s1 = {1,2,3}
s2 = {1,4,5,2}

# union 
# print(s1.union(s2))     #{1, 2, 3, 4, 5}

# intersection 
# print(s1.intersection(s2))     #{1, 2}  

#difference 
# print(s1.difference(s2))        #{3} 



# 23. Create l2 as a list and perform set operation on s1 with l1 
l2 = [2,3,1] 


# -------------------------------------------------------------

# 24. Ask user to enter the name and DOB and generate the password based on first 
# name 4 characters and @ddmm. For example name = SURESH and DOB = 05-05-1978 
# then password will be SURE@0505  
from datetime import datetime
# name = input("enter your name : ")
# dob = input("enter date in format dd/mm/yyyy :")  

def dateFormat(digit):
  day = ''
  if digit in [1,2,3,4,5,6,7,8,9]:
     day = '0'+ str(digit)
  else : 
    day = str(digit)
  return day  

def charExtract(name): 
  charName = '' 
  if len(name) <= 4 : 
     charName += name
  else:
    for i in range(4) : 
      charName += name[i]
  return charName 

def passwordGen(name,dob):
    st = ''
    try: 
       if  name.isalpha() :  
         dob = datetime.strptime(dob,"%d/%m/%Y")
         day = dateFormat(dob.day)
         month = dateFormat(dob.month)  
         nam = charExtract(name)
         st = f"{nam}{'@'}{day}{month}"
       else:
             print("enter name in proper format")
    except ValueError: 
       print("valueerror") 
    return f"your Password is {st}"  

# print(passwordGen(name,dob))


# -----------------------------------------------------------------

# 26. triangle star printing  
# for i in range(5): 
#     print('*' * i)


# 27. revese triangle star pattern 
# i = -4 
# while i<0 : 
#     print('*' * abs(i))
#     i += 1 


# 28. abcd tringale pattern 
# str1 = "ABCD"
# s = ""
# for i in range(len(str1)):
#     s = s + " " +str1[i]
#     print(s)  


# 29.Create the repeatative alphabates triangle 
# s ="ABCD"
# i = 1 
# j = 0 
# while i<=len(s) and j< len(s): 
#    print(s[j]*i)
#    i+=1 
#    j+=1

# 30. Create the format mentioned below:
# 1
# 22
# 333
# 4444 
# for i in range(1,5): 
#    print(str(i)*i) 


# 31. Val = “ABCD” based on the Val, create the format mentioned below
# D
# DC
# DCB
# DCBA  
# val = "ABCD"
# revVal = val[::-1]

# for i in range(1, len(revVal) + 1):
#     print(f"{revVal[:i]}")


# 32. Ask user to enter the string. If string is UPGRAD then output must be
# D
# DA
# DAR
# DARG
# DARGP
# DARGPU 

# val = input("Enter the string: ").upper()
# if val == "UPGRAD":
#     revVal = val[::-1]
#     for i in range(1, len(revVal) + 1):
#         print(revVal[:i])
# else:
#     print("String does not match UPGRAD")
# ----------------------------------------------------------------------------------

# 33. Create a list of odd numbers from 1 to 10
# 1. Using for loop
# 2. Using comprehensive list 

# odd_list = []
# for i in range(1, 11, 2):
#     odd_list.append(i)
# print(odd_list)                    # Output: [1, 3, 5, 7, 9] 


# odd_list = [i for i in range(1, 11, 2)]
# print(odd_list)                    # Output: [1, 3, 5, 7, 9]

# ----------------------------------------------------------------------- 

# 34. Create even number list using for loop from 200 to 250
# even_list = []
# for i in range(200, 251, 2):
#     even_list.append(i)
# print(even_list)
# [200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250]

# ------------------------------------------------------------------------------------------

# 35. List2 = [2,70,'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3,10,302.5]
# Multiply each and every element by 2 and display the answer
# Assuming para is a string variable 

# para = "test" 
# list2 = [2, 70, 'work', para, 2.5, [1,2,3], (1,2), {1,2}, {1:'a', 2:'b'}, 3, 10, 302.5]
# list3 = [item * 2 if not isinstance(item, (set, dict)) else "Can not multiply Set/Dict" for item in list2]
# print(list3)
# [4, 140, 'workwork', 'testtest', 5.0, [1, 2, 3, 1, 2, 3], (1, 2, 1, 2), 'Cannot multiply Set/Dict', 'Cannot multiply Set/Dict', 6, 20, 605.0]

# ---------------------------------------------------------------------------------------------------

# 37. Create a function to accept marks from user utilize exception concept to validate proper marks.
# def get_marks():
#     try:
#         marks = float(input("Enter marks: "))
#         if 0 <= marks <= 100:
#             return marks
#         else:
#             raise ValueError("Marks must be between 0 and 100.")
#     except ValueError as e:
#         print(f"input is not valid: {e}")
#         return None
# print(get_marks())

# Enter marks: 300
# input is not valid: Marks must be between 0 and 100.
# None

# ----------------------------------------------------------------------------------------

# 38. Create a function to validate user first name/last name. User first name/last name should contain only characters. No special characters, numbers, space in name
# def validate_name(name):
#     if name.isalpha():
#         return True
#     return False


# -------------------------------------------------------------------------------------------------------------------

# 39. Create a function to accept mobile number. Mobile number should contain 10 digits. No Special character, alphabets and space.
def validate_mobile(number):
    if number.isdigit() and len(number) == 10:
        return True
    return False

# ----------------------------------------------------------------------------
# 40. Create a function to generate auto-password based on specific person details. Ask user to enter name, DOB. And password must be First name 4 characters and year of birth.
# def generate_password():
#     name = input("Enter Name: ")
#     dob = input("Enter DOB (DD-MM-YYYY): ")
#     password = name[:4] + dob[-4:]
#     return password
# print(generate_password()) 

# Enter Name: snehal
# Enter DOB (DD-MM-YYYY): 25-08-2002
# sneh2002

# -------------------------------------------------------------------------------------------------------------

# 41. Create a empty dictionary and ask user to enter values as name, DOB, mobile number add all the details in dictionary with customer number as 1 for first time. If user try to enter another value, then number should increase as 2 with new details and previous values should not change.
# For example:
# {}
# {1:{name : "Sachin", "DOB": "21-06-1965" , "mobile": "1234123423"}}
# {1:{name : "Sachine", "DOB": "21-06-1965" , "mobile": "1234123423"},
# 2: {name : "Sumedh", "DOB": "02-02-2002" , "mobile": "1234123433"}}

# customers = {}
# def add_customer():
#     name = input("Enter Name: ")
#     dob = input("Enter DOB: ")
#     mobile = input("Enter Mobile: ")
#     new_id = len(customers) + 1
#     customers[new_id] = {
#         "name": name,
#         "DOB": dob,
#         "mobile": mobile
#     }
#     print(customers)

# print(add_customer())
# Enter Name: snehal
# Enter DOB: 25-08-2002
# Enter Mobile: 8010202390
# {1: {'name': 'snehal', 'DOB': '25-08-2002', 'mobile': '8010202390'}}
# None

# ------------------------------------------------------------------------------

# 42. Based on the above example create the dictionary and save the same in a cust_info.txt or cust_info.log
import json
# customers = {
#     1: {"name": "snehal", "DOB": "21-06-1965", "mobile": "1234123423"}
# }
# with open("cust_info.txt", "w") as file:
#     json.dump(customers, file, indent=4)
# print("Dictionary saved to cust_info.txt")

# Dictionary saved to cust_info.txt
# ----------------------------------------------------------------------------------------------------

# 43. Based on the above example read the file cust_info.txt . check if dictionary any information is available in the file. If there is information then read the dictionary store into one variable and then append new information of customer if added.

# import json
# import os

# # Check if file exists and has content
# if os.path.exists("cust_info.txt") and os.path.getsize("cust_info.txt") > 0:
#     with open("cust_info.txt", "r") as file:
#         cust_data = json.load(file)
#         print("Information available in file. Loading data...")
# else:
#     cust_data = {}
#     print("No information found. Creating new dictionary.")
# name = input("Enter Name: ")
# dob = input("Enter DOB: ")
# mobile = input("Enter Mobile: ")
# new_id = str(len(cust_data) + 1)

# cust_data[new_id] = {"name": name, "DOB": dob, "mobile": mobile}

# with open("cust_info.txt", "w") as file:
#     json.dump(cust_data, file, indent=4)

# print(f"Customer {new_id} added. Updated dictionary: {cust_data}") 

# output: 
# Information available in file. Loading data...
# Enter Name: snehal
# Enter DOB: 25-08-2002
# Enter Mobile: 8010202390
# Customer 2 added. Updated dictionary: {'1': {'name': 'snehal', 'DOB': '21-06-1965', 'mobile': '1234123423'}, '2': {'name': 'snehal', 'DOB': '25-08-2002', 'mobile': '8010202390'}}


# --------------------------------------------------------------------------------------------------

# 44. Create a table cust_info as sr_no, name, DOB, mobile. Ask user to enter the information from python code. Validate all fields and after validation insert records in the table.
import pyodbc

# conn_str = (
#     r'DRIVER={ODBC Driver 17 for SQL Server};'
#     r'SERVER=CRAVETO;'
#     r'DATABASE=CUSTOMER1;'
#     r'Trusted_Connection=yes;'
# )

# try:
#     conn = pyodbc.connect(conn_str)
#     cursor = conn.cursor()

#     cursor.execute('''
#         IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='cust_info' AND xtype='U')
#         CREATE TABLE cust_info (
#             sr_no INT IDENTITY(1,1) PRIMARY KEY,
#             name VARCHAR(100),
#             DOB VARCHAR(20),
#             mobile VARCHAR(15)
#         )
#     ''')
#     conn.commit()

#     print("--- Enter Customer Details ---")
#     name = input("Enter Name: ").strip()
#     dob = input("Enter DOB (DD-MM-YYYY): ").strip()
#     mobile = input("Enter 10-digit Mobile Number: ").strip()

#     is_valid = True
    
#     if not name.isalpha():
#         print("Error: Name should contain only characters.")
#         is_valid = False
        
#     if not (mobile.isdigit() and len(mobile) == 10):
#         print("Error: Mobile must be exactly 10 digits (numbers only).")
#         is_valid = False

#     if is_valid:
#         insert_query = "INSERT INTO cust_info (name, DOB, mobile) VALUES (?, ?, ?)"
#         cursor.execute(insert_query, (name, dob, mobile))
#         conn.commit()
#         print("Successfully validated and inserted record into the database.")
#     else:
#         print("Insertion failed due to validation errors.")

# except pyodbc.Error as e:
#     print("Database Error:", e)

# finally:
#     if 'conn' in locals():
#         conn.close()

# --- Enter Customer Details ---
# Enter Name: SNEHAL
# Enter DOB (DD-MM-YYYY): 25-08-2002
# Enter 10-digit Mobile Number: 8010202390
# Successfully validated and inserted record into the database.


# -------------------------------------------------------------------------------------------------- 


# 45. Dict1= {“Key”: {“subkey”:20} , “k2”:{“sub2” : 5}, “k3” : {“sub4” :16}, “k4” : {“sub4” : 6}}
# Sort elements based on values  

# Dict1 = {"Key": {"subkey": 20}, "k2": {"sub2": 5}, "k3": {"sub4": 16}, "k4": {"sub4": 6}}
# sorted_dict = dict(sorted(Dict1.items(), key=lambda item: list(item[1].values())[0]))
# print(sorted_dict) 

# Output: {'k2': {'sub2': 5}, 'k4': {'sub4': 6}, 'k3': {'sub4': 16}, 'Key': {'subkey': 20}}

# --------------------------------------------------------------------------------------------------- 

# 46. Create a function to calculate age till now. 

from datetime import date

# def calculate_age(birth_date):
#     today = date.today()
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return age

# print(calculate_age(date(2002, 8, 25)))           #23

# ------------------------------------------------------------------------------------------------------

# 47. Create a function to check age eligibility for given customer based on DOB. Function will take two input DOB and ELIGIBILITY age.
from datetime import datetime

# def check_eligibility():
#     dob_input = input("Enter DOB (DD/MM/YYYY): ")
#     required_age = int(input("Enter required age: "))

#     dob = datetime.strptime(dob_input, "%d/%m/%Y")
#     today = datetime.today()

#     user_age = today.year - dob.year
  
#     if (today.month, today.day) < (dob.month, dob.day):
#         user_age -= 1

#     if user_age >= required_age:
#         print(f"Eligible! Age is {user_age}")
#         return True
#     else:
#         print(f"Not Eligible. Age is {user_age}")
#         return False

# print(check_eligibility())
# Enter DOB (DD/MM/YYYY): 25/08/2002
# Enter required age: 18
# Eligible! Age is 23
# True

# ---------------------------------------------------------------------------------

# 48. Create a function to check if string is palindrome or not ? For example, if input is NITIN then reverse of the string is same then it is palindrome. If input is ANIL then reverse is LINA which is not same then it is not palindrome.
# def is_palindrome(s):
#     s = s.upper()
#     return s == s[::-1] 
# print(is_palindrome('snehal')) 
# print(is_palindrome('dad')) 
# False
# True

# ----------------------------------------------------------------------------------

# 49. Create a function to generate a Fibonacci Series. 0 1 1 2 3 5 8 13 21 34 ….. upto 100
# def generate_fibonacci():
#     a, b = 0, 1
#     series = []
#     while a <= 100:
#         series.append(a)
#         a, b = b, a + b
#     return series

# print(generate_fibonacci())
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# ------------------------------------------------------------------------------------------------

# 50. Write a code to generate factorial of the number For example: factorial of 5 = 5! = 5*4*3*2*1

# def factorial(n):
#     res = 1
#     for i in range(1, n + 1):
#         res *= i
#     return res

# print(factorial(5))  120

# ------------------------------------------------------------------

# 51. Write a program to find largest number in the list.
# l = [10, 45, 2, 99, 7]
# largest = l[0]
# for num in l:
#     if num > largest:
#         largest = num
# print("Largest number:", largest)     Largest number: 99

# ------------------------------------------------------------------------------------

# 52. Write a program to check frequency of each element in the list.
# l = [1, 2, 2, 3, 3, 3, 4]
# frequency = {x: l.count(x) for x in set(l)}
# print("Frequency:", frequency) 
# Frequency: {1: 1, 2: 2, 3: 3, 4: 1}

# ---------------------------------------------------------------------------------

# 53. There are two string l1 =[ 1,2,3,4,5] and l2 =[3,2,8,7,9] then write a program to find common elements in the list.
# l1 = [1, 2, 3, 4, 5]
# l2 = [3, 2, 8, 7, 9]
# common = list(set(l1) & set(l2))
# print("Common elements:", common)   # Output: [2, 3] 

# -------------------------------------------------------------------------------------------

# 54. Create 3 tables in sqlserver having the columns as mentioned
# 1) user : uid, mobile, passkey, date
# 2) Product : pid, pname
# 3) Order : oid, uid, pid

# user having attribute uid, mobile
# method user sign up
# sign in
# view_products
# view_orders
# place_order

# 55.Based on the OOPs concept create classes, methods, attributes and insert information
import pyodbc
from datetime import datetime

# class Store:
#     def __init__(self):
#         self.conn = pyodbc.connect(r'DRIVER={ODBC Driver 17 for SQL Server};'
#                                    r'SERVER=CRAVETO;DATABASE=CUSTOMER1;Trusted_Connection=yes;')
#         self.cursor = self.conn.cursor()
#         self.current_user_id = None

#     def sign_up(self, mobile, passkey):
#         query = "INSERT INTO [User] (mobile, passkey) VALUES (?, ?)"
#         self.cursor.execute(query, (mobile, passkey))
#         self.conn.commit()
#         print("Sign-up successful!")

#     def sign_in(self, mobile, passkey):
#         query = "SELECT uid FROM [User] WHERE mobile = ? AND passkey = ?"
#         self.cursor.execute(query, (mobile, passkey))
#         user = self.cursor.fetchone()
#         if user:
#             self.current_user_id = user[0]
#             print(f"Welcome! User ID: {self.current_user_id}")
#             return True
#         print("Invalid credentials.")
#         return False

#     def view_products(self):
#         self.cursor.execute("SELECT * FROM Product")
#         for row in self.cursor.fetchall():
#             print(f"ID: {row.pid} | Name: {row.pname}")

#     def place_order(self, pid):
#         if self.current_user_id:
#             query = "INSERT INTO [Order] (uid, pid) VALUES (?, ?)"
#             self.cursor.execute(query, (self.current_user_id, pid))
#             self.conn.commit()
#             print("Order placed successfully!")

#     def view_orders(self):
#         if self.current_user_id:
#             query = """SELECT o.oid, p.pname FROM [Order] o 
#                        JOIN Product p ON o.pid = p.pid WHERE o.uid = ?"""
#             self.cursor.execute(query, (self.current_user_id,))
#             for row in self.cursor.fetchall():
#                 print(f"Order ID: {row.oid} | Product: {row.pname}")


# app = Store()
# app.sign_up("9876543210", "pass123")

# if app.sign_in("9876543210", "pass123"):
#     print("\nAvailable Products:")
#     app.view_products()
    
#     prod_id = int(input("\nEnter Product ID to buy: "))
#     app.place_order(prod_id)
    
#     print("\nYour Orders:")
#     app.view_orders() 

# Sign-up successful!
# Welcome! User ID: 1

# Available Products:
# ID: 1 | Name: Laptop
# ID: 2 | Name: Mouse
# ID: 3 | Name: Keyboard
# ID: 4 | Name: Phone
# ID: 5 | Name: Touchscreen
# ID: 6 | Name: Charger

# Enter Product ID to buy: 2
# Order placed successfully!

# Your Orders:
# Order ID: 1 | Product: Laptop
# Order ID: 2 | Product: Mouse

# -------------------------------------------------------------------

# 56. Build a function to print bill. Generate the bill as mentioned below. 
# def print_bill(hotel_name, items):
#     width = 40
#     print("-" * (width + 2))
#     print(f"|{hotel_name.center(width)}|")
#     print("-" * (width + 2))
#     print(f"| {'sr':<4} {'Menu':<15} {'qunt':>8} {'price':>8} |")
    
#     grand_total = 0
#     for i, item in enumerate(items, 1):
#         name = item['name']
#         qty = item['qty']
#         price = item['price']
#         total = qty * price
#         grand_total += total
        
#         print(f"| {i:<4} {name:<15} {qty:>8} {price:>8} |")
    
#     print("-" * (width + 2))

#     print(f"| {'Total':<20} {grand_total:>17} |")
#     print("-" * (width + 2))

# hotel = "Welcome Hotel name"
# order_items = [
#     {'name': 'idli', 'qty': 2, 'price': 60}
# ]

# print_bill(hotel, order_items) 

# ------------------------------------------
# |           Welcome Hotel name           |
# ------------------------------------------
# | sr   Menu                qunt    price |
# | 1    idli                   2       60 |
# ------------------------------------------
# | Total                              120 |
# ------------------------------------------


# ----------------------------------------------------------------------------------------------

# Create the class college
# College name
# Address

# Init method must have Username ,password
# Methods enter_marks( roll_num)
# Check_marks(roll_num)
 

# class College:
#     college_name = "Vivekanand Educations Societies Institute of Technology"
#     address = "chembur mumbai"

#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.student_marks = {}
#         print(f"Connected to {self.college_name} system.")

#     def enter_marks(self, roll_num):
#         """input marks for a specific roll number."""
#         try:
#             marks = float(input(f"Enter marks for Roll No {roll_num}: "))
#             self.student_marks[roll_num] = marks
#             print(f"Marks for {roll_num} saved successfully.")
#         except ValueError:
#             print("Invalid input. Please enter numeric marks.")

#     def check_marks(self, roll_num):
#         """Retrieves and displays marks for a specific roll number."""
#         if roll_num in self.student_marks:
#             print(f"Roll No: {roll_num} | Marks: {self.student_marks[roll_num]}")
#         else:
#             print(f"Error: No record found for Roll No {roll_num}.")

# my_college = College("admin_user", "secure_pass123")
# my_college.enter_marks(101)
# my_college.enter_marks(102)

# print("\n--- Checking Student Records ---")
# my_college.check_marks(101)
# my_college.check_marks(105) # Test for a non-existent roll number

# Connected to Vivekanand Educations Societies Institute of Technology system.
# Enter marks for Roll No 101: 65
# Marks for 101 saved successfully.
# Enter marks for Roll No 102: 89
# Marks for 102 saved successfully.

# --- Checking Student Records ---
# Roll No: 101 | Marks: 65.0
# Error: No record found for Roll No 105.


# ------------------------------------------------------------------------------------------------
# What is difference in 1D numpy array and series
# Indexing: NumPy uses only integer positions (0, 1, 2); Series uses an explicit index (can be names, dates, or strings).
# Data Types: NumPy is homogeneous (all elements must be the same type); Series can be heterogeneous (different types in one column).
# Labels: NumPy is unlabeled raw data; Series provides a label for every single data point.
# Missing Data: NumPy has limited support for missing values; Series has built-in NaN handling for data cleaning.
# Alignment: NumPy performs operations by position; Series aligns data by index labels automatically. 


# What is difference in 2D numpy array and dataframe
# Column Headers: NumPy uses column numbers; DataFrames use column names (like 'Age', 'Salary').
# Data Consistency: In NumPy, the entire matrix must be one data type; in a DataFrame, each column can have its own type.
# Structure: NumPy is a mathematical grid for linear algebra; a DataFrame is a tabular spreadsheet for data analysis.
# Metadata: NumPy stores only raw values; DataFrames store labels, column names, and indices.
# Operations: NumPy is built for matrix math; DataFrames are built for SQL-like tasks (Groupby, Joins, Merges).


# ----------------------------------------------------------------------------------------------------------------------
