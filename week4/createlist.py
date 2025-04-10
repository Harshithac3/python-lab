def createlist(l,n):
    for i in range(n):
        temp=int(input())
        l.append(temp)
    return l
n1 = int(input("enter the limit of list a:"))
n2 = int(input("enter the limit of list b:"))
n3 = int(input("enter the limit of list c:"))
alist = []
blist = []
clist = []
print("enter elements of list:")
alist=createlist(alist,n1)
print(alist)
print("enter elements of list b:")
blist=createlist(blist,n2)
print(blist)
print("enter elements of list c:")
clist=createlist(clist,n3)
print(clist)
