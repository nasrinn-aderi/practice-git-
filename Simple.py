import numpy as np

for number in range(1,np.random.randint(1,100)):
    number = number**2
    if number % 2 ==0:
        print(number , "is even")
    else:
        print(number, "is odd")
