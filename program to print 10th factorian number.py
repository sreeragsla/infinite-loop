#w.a.p.t.p 10th factorian number
n=1
fc=0
while True:
    dummy=n
    summ=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        fact=1
        for i in range(1,rem+1):
            fact*=i
        summ+=fact
    if n==summ:
        fc+=1
    if fc==10:
        print(n)
        break
    n+=1

        
