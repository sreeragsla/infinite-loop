#w.a.p.t.p 5th to 10th prime number
n=1
pc=0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                break
        else:
            pc+=1
            if pc>=5 and pc<=10:
                print(n)
            if pc==10:
                break
    n+=1
    
