1

matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]



for row in range(len(matrix)):
    for i in range(len(matrix)) :
        print(matrix[row][i],end=' ')

for i in matrix :
    for h in i :
        print(h,end=' ')
    print()


2
matrix1=[]
for i in matrix :
    for h in i :
        matrix1.append(h)
print(sum(matrix1))
3

l=0
for i in range(len(matrix)) :
    l+=(matrix[i][i])
    print(l)


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]



sum_numbers=0
for i in range(len(matrix)):
        sum_numbers+=(matrix[i][i])
        print(sum_numbers)

4

import random
list1=[]
MyList = [[0]*3] * 3
for row in MyList :
    print(row)
print()
for i in range(3) :
    new=[]
    for i in range(3):
        new.append(random.randint(0,9))
    list1.append(new)

for i in list1 :
    print(i)

for i in range(3):
    for j in range(3):
        swap=i
        if i==j :
            print(list1[i][j])
        else: j=swap and i=j
        print(list1)



print(MyList)





list1=[]
l1=[]
l2=[]
l3=[]
n=0
for i in range(3):
    num=random.sample(range(50,100),3)
    l1.append(num)
    l2.append(num)
    list1.append(l1+l2)
print(list1)


MyList = [[]] * 5
# for i in range(5):
MyList[0].append(1)

print(MyList)

4

5
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
list1=[]
list1.append(matrix[0])
matrix.remove(matrix[0])

for i in list1:
    for j in i :
        print(j, end=' ')
print()
for i in matrix:
    i.sort(reverse=True)
    print(i)


6

guests=[]
vip=['bar','ofir','neta']
family= ['aviram', 'ohad']
friends=['moti','liron','roni']
name_remove=input('enter the name you would like to remove')
name_add=input('enter the name you would like to add')

if name_remove in vip:
    vip.remove(name_remove)
else: print('the name is not in the vip list')

type_guest=input('enter th type of the guest')
if type_guest=='friends':
    friends.append(name_add)
elif type_guest=='vip':
    vip.append(name_add)
elif type_guest=='family':
    family.append(name_add)
else:
    print("there is no list with this name")

guests.append(vip)
guests.append(family)
guests.append(friends)

for i in guests :
    print(i )



7

num=int(input('enter a number'))
the_list=[]
list1=[]
l=1
for i in range(num):
    for i in range(num):
        list1.append(l)
        l+=1
    the_list.append(list1)
    list1=[]
print(the_list)
matrix=list(zip(*reversed(the_list)))
for i in matrix :
    print(i)

8
num=int(input('enter a number'))
the_list=[]
list1=[]
l=0
for i in range(num):
    for i in range(num):
        list1.append(l)
    the_list.append(list1)
    list1=[]
    for x in range(len(the_list)):
        for y in range(len(the_list)):
            while x-y<1 :
                l=x-y
print(the_list)
l=0
num=int(input('enter a number'))
matrix=[]
i=0
for i in range(num):
    list1 = []
    for i in range(num):
        list1[i]

num=int(input('enter a number'))
matrix=[[]*num]*num
l=0
for i in range(num):
    for j in range(num):
        matrix.append(l)

for row in range(len(matrix)):
    for cal in range(len(matrix)):
            while row-cal<1 :
                matrix[row][cal]

matrix=[]
list1=[]
num=int(input('enter a number'))
for i in range(num):
    for j in range(num):
        help=i-j
        if help > 0 :
            list1.append(help)
        else: list1.append(0)
    matrix.append(list1)
    list1=[]
for stop in matrix:
    print(stop)
print()