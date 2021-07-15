#import math

#math.factorial() #python alredy have got factorial function




#--------------------





a = int(input()) #input for test

def factorial(x): #main function
    if not x<0:
        x_1=1
        for i in range(1, x+1):
            x_1=x_1*i
        return x_1

print(factorial(a)) #run function
