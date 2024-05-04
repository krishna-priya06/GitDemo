#if_ifelse
greeting = "goodmorning"
if greeting == "goodmorning":
    print("condition matches")
else:
    print("condition doesnot match")


a=6
b=7
if a==b:
    print("the numbers or equal")
elif a!=b:
    print("the numbers or not equal")
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")

a = 330
b = 2
print("A") if a > b else print("B")

#forloop

objs = [1,2,3,4]
for obj in objs:
    print(obj*2)

nums =[1,2,3,4,5]
sum=0
for num in nums:
    sum =sum+num
print (sum)

nums =[1,2,3,4,5,6,7,8,9,10]
for num in nums:
    if (num%2!=0):
        continue
    else:
        print(num)
print("*****************")
nums =[6,3,4,1,7,8,0]
i = 0
for num in nums:
    #print(ind)
    if (i%2==0):
        pass
    else:
        print(num)
    #print('before incrementing',ind)
    i = i + 1
    #print('after incrementing',ind)

summation = 0
for j in range(1,6):
    summation= summation+j
print(summation)



# i=1
# while i<10:
#     if i==7:
#         continue
#     else:
#         print(i)
#     i=i+1
#
setz = [1,2,3,4,5,6,7,8,9,10]

# for set in setz:
#     if set==7:
#         continue
#     else:
#         print(set)

for setz in range (1,30):
    if setz == 7:
        continue
    else:
        print(setz)

i =-1
while i<6:
    i += 1
    if i==3:
        continue
    print(i)

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

fruits= ("apple", "banana", "Orange")
for fruit in fruits:
    print(fruit)
i=2
fruits= ["apple", "banana", "Orange"]
while i>-1:
    print( fruits[i])
    i=i-1

print("********")
i=5
x= "orange"
# while i>-1:
#  print(x[i])
#  i=i-1
# print("********")
# x= "orange"
# print(x[-10])

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)