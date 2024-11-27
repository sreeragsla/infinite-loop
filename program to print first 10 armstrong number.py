#w.a.p.t.p first 10 armstrong numbers
n=1
ac=0
while True:
    dummy=n
    summ=0
    p=len(str(n))
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem**p
    if n==summ:
        print(n)
        ac+=1
    if ac==10:
        break
    n+=1
