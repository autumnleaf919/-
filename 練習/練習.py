import sys
print("點(d,e)  L:ax+by+c=0,輸入a,b,c,d,e來計算點到直線的距離")
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
