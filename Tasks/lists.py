task:
1)Even or Odd Checker:
Take an integer as input and print whether it's even or odd.
n=int(input("enter a value:"))
if n%2==0:
    print("even")
else:
    print("not even")

2)Sum of Digits:
Given a number, find the sum of its digits (e.g., 123 ➝ 6).

n = int(input("Enter a number: "))
total = 0
while n > 0:
    digit = n % 10       
    total += digit       
    n = n // 10          
print("Sum of digits:", total)

3)Count Vowels in a String:
Input a string and count how many vowels it contains.

def count(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
str = input("Enter a string: ")
a= count(str)
print("Number of vowels:", a)
4)Check Palindrome:
Check if a given string or number is a palindrome (same forward and backward).

def palindrome(value):
    value = str(value)  
    return value == value[::-1] 

a= input("Enter a string or number: ")

if palindrome(a):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")

5)Find Maximum in a List:
Given a list of numbers, find and print the maximum number.

def find_max(numbers):
    maximum = numbers[0]  
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

input_list = [10, 45, 2, 89, 34]
result = find_max(input_list)
print("Maximum number in the list:", result)