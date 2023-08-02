import random

ages = ['age', 'free', 'one', 'cone', 'tone', 'red', 'reap', 'flee', 'gone', 'near', 'done']
strings = 'abcdefghjiklmnopqrstuvwxyz'

new_arr = []
while True:
    
    t = random.sample(strings, k = 4)
    combine = ''.join(t).strip()
    if combine not in ages:
        continue
    else:
        new_arr.append(combine)
        if len(new_arr) == 5:
            break

print(new_arr)
print(list(set(new_arr)))




def perm(n,r):
    x = 1
    y = 1
    for i in range(1, n+1):
        x*=i
    for j in range(1, n-r+1):
        y*=j

    return int(x / y)

print('Your answer is ', perm(5,2))



def comb(n,r):
    x = 1
    y = 1
    z = 1
    for i in range(1, n+1):
        x*=i
    for j in range(1, r+1):
        y*=j
    for k in range(1, n-r+1):
        z*=k
    return int(x/(y * z))

print('Your answer  is' , comb(5,2))


