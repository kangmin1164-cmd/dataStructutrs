import time

def hanoi_tower(n, fr, tmp, to):

    if(n==1):
        print("원판 1; %s --> %s" %(fr, to))

    else:
        hanoi_tower(n-1, fr,to,tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)

start=time.time()
hanoi_tower(8, 'A', 'B', 'C')
end=time.time()
print("실행시간=", end-start)