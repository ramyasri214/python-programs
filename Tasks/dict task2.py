# 1)	Delete a list of keys from a dictionary
# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# # Keys to remove
# keys = ["name", "salary"]

# sample_dict={"name":"kelly","age":25,"salary":8000,"city":"new york"}
# keys=["name","salary"]
# for key in keys:
#     sample_dict.pop(key,None)
# print(sample_dict)

# 2)Count the frequency of each character in a given string using a dictionary.
# a=("hi hello how are you")
# res={}
# for x in a:
#     if x not in res:
#         res[x]=1
#     else:
#         res[x]+=1
# print(res)

# 3)	Write a Python program to create a dictionary with two keys:
# "even" → containing all even numbers from the list
# "odd" → containing all odd numbers from the list
# a=(1,2,3,4,5,6,7)
# b={"even":[],"odd":[]}
# for x in a:
#     if x%2==0:
#         b["even"].append(x)
#     else:
#         b["odd"].append(x)
# print(b)

# 4)What is the difference between dict.get() and direct key access?

# In Python, both dict.get(key) and direct key access like dict[key] are used to retrieve values from a dictionary — but they behave differently when the key is missing.

# dict[key]:-
# --->	rerturns The value for the key
# --->   if key is missing it raises the Error
# --->   it does not provide default value

# dict.get(key):-
# ----> returns the value for the Key
# ---->if key is missing it returns none or default Value
# ----> it will provide the default value

# 5)Convert a dictionary to a list of tuples.
# sample_dict={'a':1,'b':2,'c':3}
# tuple_dict=list(sample_dict.items())
# print(tuple_dict)


# 6.	Write a program to store names as keys and their lengths as values.
# names=["ramya","sri","sivanagamani","krishnakumari","tharun"]
# name_length={}
# for name in names:
#     name_length[name]=len(name)
# print(name_length)

# 7)Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and "odd" if the number is odd
# Expected Output:

# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}


# b={}
# for x in range(1,6):
#     if x%2==0:
#         b[x]="even"
#     else:
#         b[x]="odd"
# print(b)



# 8.	Create Reverse Word Dictionary
# Given list of words:
# words = ["cat", "dog", "bat"]
# Create a dictionary with words as keys and their reversed strings as values

# Expected Output:
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}

# words=["cat","dog","bat"]
# res={}
# for x in words:
#     res[x]=x[::-1]
# print(res)

# 9)Write a program to sum all the values in a dictionary.
# a={1,2,3,4,5}
# sum=0  
# for i in a:
#     sum +=i
# print(sum) 