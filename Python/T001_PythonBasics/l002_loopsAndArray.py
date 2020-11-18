# 1. author name.
__author__ = "Rajneesh Kumar"


# 1. range(a) : [0,a), but not include a.
# 2. range(a,b) : [a,b), but not include b.
# 3. range(a,b,c) : a to b by increment of c.

for i in range(2,10,3):
    print(i, end = " ")
print()

# 4. loop over List
a = [34,5.6,"Rajneesh", 's',True,False]
for i in a:
    print(i, end = " ")
print()

# 5. even - odd 
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    if i % 2 == 0:
        print("Even Number: ", i)
    else:
        print("Odd Number: ", i)

# 6. loop over characters of string
a = "Rajneesh Kumar"
for i in str(a):
    print(i, end = " -> ")
else:
   print("end")

i = 0
while( i < 6):
    print(i, end = " ")
    i += 1
else:
    print()
