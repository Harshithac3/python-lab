p=int(input())
t=int(input())
r=int(input())
A=p*(1+r/100)**t
CI=A-p
print(round(CI,2))
