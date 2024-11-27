#w.a.p.t.p Nth prime number

count=int(input())
pc=0
n=1
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
            if pc>=count:
                print(n)
            if pc==count:
                break
    n+=1
