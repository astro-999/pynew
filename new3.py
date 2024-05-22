#scissor paper rock
import random as r
l1 = ['scissor','paper ','rock']
u =r.choice(l1)
print(' rock scissor paper ')
count = 0 
print(u)
while True :
    guess = input('enter the choice :')
    count +=1
    if guess== u:
        print('try again')
    elif guess  == 'scissor'  and u == 'paper' or guess  == 'rock'  and u == 'scissor' or guess  == 'paper'  and u == 'rock' :
        print ('you won')
        print(f'you won on {count} try')
        break
    elif guess  == 'scissor'  and u == 'rock' or guess  == 'paper'  and u == 'scissor' or guess  == 'rock'  and u == 'paper' :
        print('you lost')
    else:
        print('invalid input')
    