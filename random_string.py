import random

ages = ['age', 'free', 'one', 'cone', 'tone', 'red', 'reap', 'flee', 'gone', 'near', 'done']
strings = 'abcdefghjiklmnopqrstuvwxyz'

new_array = []


while True:
    t = random.sample(strings, k = 4)
    q = ''.join(t).strip()
    if q not in ages:
        continue
    else:
        new_array.append(q)
        if len(new_array) == 25:
            break
    

print(new_array)
print(list(set(new_array)))


def permutation_calc(n, r):
    i = 1
    j = 1
    p = n - r
    for x in range(1, n+1):
        i*=x
    for y in range(1, p+1):
        j*=y
    permutation = int(i/j)
    print(f"Your answer is {permutation}")

        

    
permutation_calc(26, 4)




        
