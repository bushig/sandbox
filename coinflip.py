import random

resh=0
orel=0

for i in range(1, 10001):
    num = random.randint(0,1)
    if num==0:
        resh+=1
    elif num==1:
        orel+=1

print('Решек: {} Орлов: {}'.format(resh, orel))