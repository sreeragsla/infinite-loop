#w.a.p.t.p first 10 perfect number
n=1
pc=0
while True:
    ds=0
    for i in range(1,n//2+1):
        if n%i==0:
            ds+=i
    if n==ds:
        print(n)
        pc+=1
    if pc==10:
        break
    n+=1

        
    
