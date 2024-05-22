import numpy as np
r1 = np.random.randint(0,100)
print(r1)
count = 0
print(' the random number   guesser ')
while True:
    n1 = (input('Guess the number :'))
    count +=1
    if n1.isdigit() ==True:
        n1 = int(n1)
        if n1 == r1:
            print('you win')
            break 
        elif n1 < r1 :
            print(' low guess')
        else:
            print('high guess')
        print('attempt:',count)
    else :
        print('Enter the valid input : ')
        