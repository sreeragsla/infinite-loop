#w.a.p.t.p 5th to 10th harshad number
n=1
hc=0
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        summ+=rem
    if n%summ==0:
        hc+=1
        if hc>=5 and hc<=10:
            print(n)
    if hc==10:
        break
    n+=1
