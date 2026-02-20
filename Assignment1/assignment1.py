# Comprehensive list:
# 1.Write a list comprehension to generate squares of numbers from 1 to 10.  
# li = [x**2 for x in range(1,11) ]
# print(li) 
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] 

# ---------------------------------------------------------------

# 2. Create a list of even numbers between 1 and 50 using list 
# comprehension. 
# li = [x for x in range(1,51)  if x%2 == 0 ]
# print(li)

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

# --------------------------------------------------------------------------------------------

# 3. Convert all strings in a list to uppercase using list comprehension.
# li = ['snehal', 'dighore','A'] 
# li2 = [i.upper() for i in li ]
# print(li2) 
# ['SNEHAL', 'DIGHORE', 'A']

# -------------------------------------------------------------------------------------------------

# 4. Given a list of integers, create a new list that contains only the positive 
# numbers.
# li=[1,2,3,-1,-2,3,4,-6] 
# li2 = [x for x in li if x>=0 ] 
# print(li2) 
# [1, 2, 3, 3, 4]

# ---------------------------------------------------------------------------------- 

# 5. Create a list of tuples (num, num^2) for numbers 1 to 5. 
# li = [(x,x**2) for x in range(1,6)] 
# print(li) 
# [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

# ------------------------------------------------------------------------------------- 

# 6. Extract all vowels from a given string using list comprehension. 
# st = 'snehal'  
# st.lower()
# li = [st[x] for x in range(len(st)) if st[x] in ['a','e','i','o','u']]
# print(li) 
# ['e', 'a']

# ------------------------------------------------------------------------------------------

# 7. Flatten a 2D list using list comprehension. 

# x = [[1, 2, 3], [4, 5], [6, 7, 8]]
# flattened = [item for i in x for item in i]
# print(flattened)
# [1, 2, 3, 4, 5, 6, 7, 8] 

# -------------------------------------------------------------------------------------------

# 8. Replace all negative numbers in a list with 0 using list comprehension.  
# li = [1,2,3,-2,2,-1,-4] 
# li2 = [x if x >= 0 else 0 for x in li]
# print(li2) 
# [1, 2, 3, 0, 2, 0, 0] 

# ----------------------------------------------------------------------------------------------

# 9. Given a list of words, create a list of lengths of each word.   
# words = ['snehal','dighore']
# li = [len(word) for word in words] 
# print(li)
# [6, 7]

# ------------------------------------------------------------------------------------------

# 10. Filter out words that start with the letter 'A' or 'a'.  
# li = ['can',"An",'ant','ban']
# li2 = [w for w in li if not w.lower().startswith('a')] 
# print(li2) 
# ['can', 'ban']

# --------------------------------------------------------------------------------------

# 11. From a list of numbers, generate a list of “even” or “odd” strings using 
# list comprehension.  

# li = [1,2,3,4,5,6]
# li2 = ["even" if x % 2 == 0 else "odd" for x in li]
# print(li2)  
# ['odd', 'even', 'odd', 'even', 'odd', 'even']

# --------------------------------------------------------------------------------------

# 12. Create a list of numbers divisible by both 3 and 5 in range 1–100.  
# li = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0] 
# print(li)
# [15, 30, 45, 60, 75, 90] 

# ----------------------------------------------------------------------------------------
# 13. Write a nested list comprehension to generate a multiplication table 
# for 1–5. 

# li = [[i * j for j in range(1, 11)] for i in range(1, 6)]
# print(li) 
# [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 6, 8, 10, 12, 14, 16, 18, 20], [3, 6, 9, 12, 15, 18, 21, 24, 27, 30], [4, 8, 12, 16, 20, 24, 28, 32, 36, 40], [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]]

# ----------------------------------------------------------------------------------------

# 14. Convert a dictionary’s keys into a list using list comprehension.  
# di = {1:2,2:4,5:6,7:2}
# li = [k for k in di] 
# print(li) 

# [1, 2, 5, 7]
# ----------------------------------------------------------------------------------------------

# 15. Extract numeric digits from a string using list comprehension. 

# s = "snehal dighore 1, final round 3!" 
# digits = [char for char in s if char.isdigit()] 
# print(digits) 

# ['1', '3']

# --------------------------------------------------------------------------------------------------
# 16. Use list comprehension to remove all spaces from a string. 
# s = "snehal dighore final  "
# noSpace = "".join([char for char in s if char != " "])
# print(noSpace) 

# snehaldighorefinal

# -----------------------------------------------------------------------------------------------------

# 17. Create a list of characters that appear more than once in a string. 
# s = "abracadabra"
# duplicates = list({char for char in s if s.count(char) > 1}) 

# print(duplicates) 
# ['b', 'r', 'a']

# ------------------------------------------------------------------------------------------------

# 18. From a list of sentences, generate a list of all words (split using list 
# comprehension). 

# s = ["Hello world", "Python is fun"]
# words = [word for i in s for word in i.split()] 
# print(words) 
# ['Hello', 'world', 'Python', 'is', 'fun']

# --------------------------------------------------------------------------------------------------- 

# 19. Create a list of unique elements from a list using list comprehension + 
# condition. 
# items = [1, 2, 2, 3, 4, 4, 5]
# unique = [x for i, x in enumerate(items) if x not in items[:i]]

# print(unique) 
# [1, 2, 3, 4, 5]

# -----------------------------------------------------------------------------------------------------

# 20. Generate all pairs (x, y) where x is from list A and y is from list B 
# (cartesian product)   

# A, B = [1, 2], ['a', 'b']
# pairs = [(x, y) for x in A for y in B] 
# print(pairs) 

# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# -------------------------------------------------------------------------------------------


# Lambda functions
# 1. Write a lambda to add two numbers.   
# number = lambda x, y: x + y
# print(number(1,2))      #3

# -------------------------------------------------------------
# 2. Create a lambda to check if a number is even. 
# even =lambda x: x % 2 == 0 
# print(even(2))     #True

# ------------------------------------------------------------------
# 3. Write a lambda to get the last character of a string. 
# string =lambda s: s[-1] 
# print(string('snehal'))      #l

# --------------------------------------------------------------------

# 4. Use lambda with map() to square every number in a list.  
# li = list(map(lambda x: x**2, [1, 2, 3]))
# print(li)        
# [1, 4, 9]

# -------------------------------------------------------------------------------

# 5. Use lambda with filter() to get only odd numbers from a list. 
# li =list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4]))
# print(li)

# [1, 3]

# ----------------------------------------------------------------------------------

# 6. Use sorted() + lambda to sort a list of tuples by second value.
# li = [(1,2),(0,1),(3,0)]
# li2 = sorted(li, key=lambda x: x[1]) 
# print(li2) 
# [(3, 0), (0, 1), (1, 2)]

# --------------------------------------------------------------------------------- 

# 7. Create a lambda to check if a string is a palindrome.
# palind =  lambda s: s == s[::-1] 
# print(palind('snehal'))
# print(palind('ana'))
# False
# True

# ----------------------------------------------------------------------------------- 

# 8. Use lambda to find maximum of three numbers.

# numbers =lambda a, b, c: max(a, b, c)
# print(numbers(1,2,3))     #3

# -------------------------------------------------------------------------------------

# 9. Write a lambda to reverse a string.
# l = lambda s: s[::-1]
# print(l('snehal'))  
# lahens

# -----------------------------------------------------------------------------------------

# 10. Use lambda with map() to convert a list of strings to integers. 
# li = list(map(lambda x: int(x), ["1", "2"]))
# print(li) 
# [1, 2] 

# ---------------------------------------------------------------------------------------------

# 11. Use lambda with filter() to remove empty strings from a list.
# li = list(filter(lambda s: s != "", ["a", "", "b"]))
# print(li)
# ['a', 'b']

# ----------------------------------------------------------------------------------------------- 

# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner 
# madness).
from functools import reduce 
# n = 5
# li = reduce(lambda x, y: x * y, range(1, n+1))
# print(li)
# 120

# -------------------------------------------------------------------------------------------------
# 13. Write a lambda that returns the larger of two numbers.
# numbers =lambda a, b: a if a > b else b
# print(numbers(2,3))     #3

# ---------------------------------------------------------------------------------------

# 14. Use lambda to check if number is divisible by 5.
# li= lambda x: x % 5 == 0   
# print(li(4))
# print(li(5))
# False
# True

# ---------------------------------------------------------------------------------------------
# 15. Use lambda + map() to add 10 to each element of a list.
# li = [1,3,4,2]
# l = list(map(lambda x: x + 10, li))
# print(l)
# [11, 13, 14, 12] 

# ----------------------------------------------------------------------------------------

# 16. Use lambda to sort a list of dictionaries by a key (like "age"). 
# l = [{'age':3},{'age':2}]
# li = sorted(l, key=lambda d: d['age'])
# print(li)

# [{'age': 2}, {'age': 3}]

# -------------------------------------------------------------------------

# 17. Write a lambda that returns True if a character is a vowel.
# vov = lambda c: c.lower() in 'aeiou' 
# print(vov('a'))
# print(vov('b'))
# True
# False

# -------------------------------------------------------------------------------

# 18. Use lambda + filter to extract words of length > 5 from a list. 
# words = ['snehal', 'dighore','sn']
# l = list(filter(lambda s: len(s) > 5, words))
# print(l) 
# ['snehal', 'dighore']

# -----------------------------------------------------------------------------------

# 19. Use lambda to calculate the area of a circle (πr²).
# area = lambda r: 3.14159 * r**2 
# print(area(4)) 
# 50.26544

# ------------------------------------------------------------------------------------

# 20. Write a lambda to remove duplicates from a list using filter + set.
# seen = set()
# l = list(filter(lambda x: x not in seen and not seen.add(x), [1, 2, 1, 3, 2]))
# print(l) 
# [1, 2, 3]


# --------------------------------------------------------------------------------------

# 21. Use lambda with reduce() to find the product of all numbers in a list.
# li = reduce(lambda x, y: x * y, [1, 2, 3, 4])
# print(li) 
# 24

# ----------------------------------------------------------------------------------------

# 22. Write a lambda that returns absolute value of a number.
# value =lambda x: abs(x) 
# print(value(-5)) 
# 5

# --------------------------------------------------------------------------------------------

# 23. Use lambda to sort a list of strings by their length.
# li = ['snehal','dighore','sn']
# length=sorted(li, key=lambda s: len(s)) 
# print(li)
# ['snehal', 'dighore', 'sn']

# --------------------------------------------------------------------------------------------

# 24. Use lambda to get only uppercase characters from a string.
# s = 'snEhAl'
# l ="".join(filter(lambda c: c.isupper(), s)) 
# print(l)
# EA 

# ----------------------------------------------------------------------------------
# 25. Write a lambda that returns the square if number is even, cube if odd.
# l= lambda x: x**2 if x % 2 == 0 else x**3
# print(l(4))
# 16
# print(l(3))
# 27

# -------------------------------------------------------------------------------------
# 26. Use lambda with map to convert Celsius to Fahrenheit.
# t = 30
# conv =list(map(lambda c: (c * 9/5) + 32, [t])) 
# print(conv) 
# [86.0]

# ----------------------------------------------------------------------------------------
# 27. Write a lambda to check if two strings are anagrams.
# is_anagram = lambda s1, s2: sorted(s1.lower()) == sorted(s2.lower()) 

# print(is_anagram('snehal','dighore'))
# False

# ------------------------------------------------------------------------------------------

# 28. Use lambda to extract only numeric values from a mixed list.
# li = [1,2,{1:3},'snehal',5]
# val = list(filter(lambda x: isinstance(x, (int, float)), li))
# print(val)
# [1, 2, 5]

# --------------------------------------------------------------------------------------------

# 29. Use lambda inside any() to check if any list element is negative.
# li = [1,2,-3]

# che=any(map(lambda x: x < 0, li))
# print(che)
# True

# -----------------------------------------------------------------------------------------------
  
# 30. Use lambda to generate a function that multiplies any number by n 
# def multiply_by(n):
#     return lambda x: x * n
# doubl = multiply_by(2)

# print(doubl(10))
# 20





