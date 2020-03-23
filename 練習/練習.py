import sys
import Math.distance as D
import Math.PCH as PCH
print("點(d,e)  L:ax+by+c=0,輸入a,b,c,d,e來計算點到直線的距離")
for n in sys.stdin:
    a,b,c,d,e=n.split()
    print(D.Dis(a,b,c,d,e))
