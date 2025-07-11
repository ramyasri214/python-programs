loops:
1)while loop:
syntax:
while expression:
    statement(s)

Example:-
a = 0
while (a < 3):
    a = a + 1
    print("Hello ramyasri ")

2)Do-While:-Do while loop is a type of control looping statement that can run any statement until the condition statement becomes false specified in the loop. In do while loop the statement runs at least once no matter whether the condition is false or true.
Syntax:-
do{
    // statement or 
    // set of statements
}
while(condition)

Example:-

while True:
    number = int(input("Enter a positive number: "))
    if number > 0:
        break  
    print("That's not a positive number. Try again.")

print(f"Thanks! You entered: {number}")

3)Nested-loop:-A nested loop in Python refers to a loop inside another loop.
syntax:-
for i in range(3):         
    for j in range(2):     
        print(f"i={i}, j={j}")

example program:-
for i in range(1, rows + 1):       
    for j in range(i):             
        print("*", end=" ")
    print()
