print("_____List_____")
a = [1,22,3.4,True,'hello',3.4]
x = a.index(True)
print(x) #why does it return 0.

a = [1,22,3.4,False,'hello',3.4]
x = a.index(False)
print(x) #why does it return 3 when False is in the list.

a = [1,22,3.4,False,'hello',3.4]
x = a.index(True)
print(x) #why does it returns 0 if True is not in the list.

a = [1]
x = a.index(True)
print(x) #why does it returns 0

a = [1,22,3.4,True,'hello',True,1,1,1,1,1,1]
x = a.count(1)
print(x) # does it count True as 1, it has only 7 1's but it returns 9

a = [1,22,3.4,True,'hello',True,1,1,1,1,1,1]
x = a.count(True)
print(x) # does it count True as 1 and vise versa



print("_____Tuple_____")
a = (1,22,3.4,True,'hello',3.4,1,1,1,1,1,1)
x = a.count(1)
print(x) # does it count True as 1, the tuple has only 7 1's but it returns 8

a = (1,22,3.4,True,'hello',True,1,1,1,1,1,1)
x = a.count(1)
print(x) # does it count True as 1, the tuple has only 7 1's but it returns 9

a = (1,22,3.4,True,'hello',True,1,1,1,1,1,1)
x = a.count(True)
print(x) # does it count True as 1 and vise versa

"""the below code throws not found error
a = []
x = a.index(True)
print(x)

a = [3]
x = a.index(True)
print(x)

"""


