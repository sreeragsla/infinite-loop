#w.a.p.t.p 10th perfect number
n=1
pc=0
while True:
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if n==ds:
        pc+=1
    if pc==10:
        print(n)
        break
    n+=1
