import sys
import Math.distance as M
print("點(d,e)  L:ax+by+c=0,輸入a,b,c,d,e來計算點到直線的距離")
for n in sys.stdin:
    a,b,c,d,e=n.split()
    print(M.Dis(a,b,c,d,e))
