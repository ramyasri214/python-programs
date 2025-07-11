# Invert a dictionary with list values (group keys by their values)
# Input:
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# Output:
# {1: ['a', 'c'], 2: ['b'], 3: ['d']}
#  (Hint: Use setdefault method)

# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# res={}

# for key, value in d.items():
#     res.setdefault(value, []).append(key)

# print(res)
    

# 2)Find Max and Min Value in Dictionary
# Input:
# d = {'a': 10, 'b': 5, 'c': 15}
# Output:
# Max Value → 15
# Min Value → 5

# d = {'a': 10, 'b': 5, 'c': 15}
# max_values=max(d.values())
# print("maximum value is ---->",max_values)
# min_values=min(d.values())
# print("minimum value is ----->",min_values)

# 3)Create a dictionary using dictionary comprehension for the given list of numbers, where:
# Each number is a key.

#  The value is "prime" if the number is prime.

#  The value is "notprime" if the number is not prime
# Output:   {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}
# res={x:('prime' if all(x%y !=0 for y in range(2,9))else'not prime')for x in range(3,10)}
# print(res)

# 4)Explain about setdefault function in dictionary data type ?
# 1)The setdefault() method in a dictionary is used to:
# 2)Get the value of a specified key if it exists.
# 3)If the key doesn't exist, it adds the key with a default value and returns that default.
# syntax:-
# setdefault(key, default_value)
# key: The key to search for in the dictionary.

# -->default_value: (Optional) The value to set and return if the key is not found.

# -->If not provided, it defaults to None.

# 5)diffrenece between dict[key] and dict.get(key)
# In Python, both dict.get(key) and direct key access like dict[key] are used to retrieve values from a dictionary — but they behave differently when the key is missing.

# dict[key]:-
# --->	rerturns The value for the key
# --->   if key is missing it raises the Error
# --->   it does not provide default value

# dict.get(key):-
# ----> returns the value for the Key
# ---->if key is missing it returns none or default Value
# ----> it will provide the default value

# 6)difference between shallow copy and deep copy

# 1.) Shallow Copy:
# Creates a new outer object, but copies references to the inner objects.
# Changes to nested/mutable elements affect both copies.

# 2.) Deep Copy:
# Creates a completely independent copy, including all nested objects.
# Changes to nested elements do not affect the original.

# 7)Count Vowels in String with Dict Comprehension.

# s = "welcome to python programming"
# a="aeiouAEIOU"
# count=0
# res={}
# for ch in s:
#     if ch in a:
#        count +=1
#        res[ch]=count
# print("total vowels in a string:",count)

# 8)What is an Automorphic Number? Give examples.
#  Expected Answer:
# An Automorphic Number is a number whose square ends with the number itself.

# Examples: 5 (5² = 25), 6 (6² = 36), 76 (76² = 5776)
# n=int(input("enter a value:"))
# p=n**2
# len=(len(str(n)))
# if n==p%10**1:
#     print("automorphic number")
# else:
#     print("not automorphic number")
