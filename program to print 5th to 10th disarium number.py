#w.a.p.t.p 5th to 10th disarium number
dc=0
n=1
while True:
    dummy=n
    summ=0
    p=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ=rem**p
        p-=1
    if n==summ:
        dc+=1
        if dc>=5 and dc<=10:
            print(n)
    if dc==10:
        break
    n+=1


