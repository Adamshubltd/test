t = [[3-i for i in range (3)] for j in range (3)]

s = 0
for i in range(3):
    s += t[i][i]
print(s)

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])


How many elements does the my_list list contain?

my_list = [i for i in range(-1, 2)]


 What is the output of the following snippet?

my_list = [1, 2, 3]
for v in range(len(my_list)):
    my_list.insert(1, my_list[v])
print(my_list)

my_list_1 = [1, 2, 3]
my_list_2 = []
for v in my_list_1:
    my_list_2.insert(0, v)
print(my_list_2)


 var = 1
while var < 10:
    print("#")
    var = var << 1


var = 0
while var < 6:
    var += 1
    if var % 2 == 0:
        continue
    print("#")

How many hashes (#) will the following snippet send to the console?

for i in range(1):
    print("#")
else:
    print("#")


i = 0
while i <= 3 :
    i += 2
    print("*")
 
