Define all the Math modules and also write the logic for every math module

module is a python file containing variables,functions,classes.functions are used for reusability of code.
modules are divided into 3 types
1)Builtin Module
2)user defined module
3)third-party Module


--->Built-in Module:-square,
1)Math values:-
import math
print(math.sqrt(25))
import math
print(math.sqrt(36))

n=25  //with out using math.sqrt
sqrt=n**0.5
print(sqrt)



2)Power:-power expecting 2 values 1)value and 2)base
import math
print(math.pow(5,2))

import math
print(math.pow(7,2))

n=5//with out using math.pow
b=n**2
print(b)

3)floor(//):-when we have decimal number we want to convert decimal to int then use floor method
import math
print(math.floor(3))

import math
print(math.floor(500.25))

n=5.7
b=n//1
print(b)


4)ceil:-
import math
print(math.ceil(34.9))

import math
print(math.ceil(52.1))



5)fabs:-it returns an absolute number.it converts negative values to positive values
import math
print(math.fabs(-20))

import math
print(math.fabs(20))

import math
print(math.fabs(25.0))

6)Factorial:-
import math
print(math.factorial(5))

import math
print(math.factorial(6))

7)GCD:--
import math
print(math.gcd(1,3))

import math
print(math.gcd(5,9))

8)LCM:-
import math
print(math.lcm(4,9))

import math
print(math.lcm(2,4))

9)LOG:-
import math
print(math.log(3))

import math
print(math.log(6))

print(math.pi)
print(math.e)
