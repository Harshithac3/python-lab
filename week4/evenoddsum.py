def createlist(l,n):
    for i in range(n):
        temp=int(input())
        l.append(temp)
    return l
def evensum(l):
    sum=0
    for i in range(len(l)):
        if (i%2==0):
            sum+=l[i]
    return sum
def oddsum(l):
    sum=0
    for i in range(len(l)):
        if (i%2!=0):
            sum+=l[i]
    return sum
n1 = int(input("enter the limit of list a:"))
n2 = int(input("enter the limit of list b:"))
n3 = int(input("enter the limit of list c:"))
alist = []
blist = []
clist = []
print("enter elements of list:")
alist=createlist(alist,n1)
print(alist)
x,x1=evensum(alist),oddsum(alist)
print(x,x1)
print("enter elements of list b:")
blist=createlist(blist,n2)
print(blist)
x,x1=evensum(blist),oddsum(alist)
print(x,x1)
print("enter elements of list c:")
clist=createlist(clist,n2)
print(clist)
x,x1=evensum(clist),oddsum(alist)
print(x,x1)
