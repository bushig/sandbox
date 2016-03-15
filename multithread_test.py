import time
import threading
from random import random

loops=[1,4,5,2,3,4,5, 2, 5,2,1,0,2,5,2,4,5,3,5,2,1]
result=[]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.func=func
        self.args=args
        self.name=name

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('starting loop', nloop,'at',time.ctime())
    time.sleep(nsec)
    global result
    result.append(nsec)
    print('ending loop', nloop, 'at',time.ctime())


def main():
    print('starting ALL at:',time.ctime())
    threads=[]
    nloops=range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('finished ALL at: {}'.format(time.ctime()))
    print(result)



if __name__=='__main__':
    main()