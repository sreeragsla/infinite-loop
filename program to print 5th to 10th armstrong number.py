#w.a.p.t.p 5th to 10th armstrong number
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
        ac+=1
        if ac>=5 and ac<=10:
            print(n)
    if ac==10:
        break
    n+=1

