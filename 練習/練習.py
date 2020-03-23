import sys
print("ax+by+c=0 (d,e),輸入a,b,c,d,e")
for n in sys.stdin:
    a,b,c,d,e=n.split()
    a=float(a)
    b=float(b)
    c=float(c)
    d=float(d)
    e=float(e)
    distance=abs((a*d)+(b*e)+c)/(((a**2)+(b**2))**(1/2))
    print(distance)
    print("")
