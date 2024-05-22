#prgms 
def even(l1):
    sum = 0
    for i in l1:
        if i % 2==0:
            # print(i)
            sum = sum + i
    print('sum of even ',sum)

l1 = [1,2,3,4,5,6,7,8,9,0,120,78,11]
even(l1)



