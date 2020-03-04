import math

def a_prime(number):    
        if(number == 1 or number == 2):
            return (number," is a prime number")
        
        for i in range(1, number):
            i <= math.ceil(math.sqrt(number))
            i += 1
            if(number % i == 0 and i != number):
                return (number," isn't a prime number")
        return (number," is a prime number")

try:
    try_again = ""
    while(try_again != "n"):
        number = int(input("Ange ett tal: "))
        if(number > 0):
            print(a_prime (number))
        else:
            print("Only positive numbers pls")
        try_again = str(input("Want to try again? y/n: "))
        if(try_again is not "y" and try_again is not "n"):
            while(try_again is not "y" and try_again is not "n"):
                try_again = str(input("Please give a real answer. y/n: "))
except ValueError as n_error:
    print("Input error: {0}{1}".format(n_error," is what caused the error"))

