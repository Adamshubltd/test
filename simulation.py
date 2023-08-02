import random

print(random.randint(1,7))


ls = [0]

for x in range(100):
    step = ls[-1]

    dice = random.randint(1,7)
    
    if dice <=2:
        step-=1
    elif dice <=5:
        step+=1
    else:
        step+=dice
        print('Condition is not satisfied!')
    ls.append(step)
print(ls)
#print(len(ls))
