#w.a.p.t.p first 10 disarium numbers
n=1
dc=0
while True:
    dummy=n
    summ=0
    p=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**p
        p-=1
    if n==summ:
        print(n)
        dc+=1
    if dc==10:
        break
    n+=1
