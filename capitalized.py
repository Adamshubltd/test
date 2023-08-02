import random




subjects = [ 'maths', 'eng', 'geo', 20, 50.5, 'john', 'adAms', 'okpukorO']

new_subject = []
for subject in subjects:
    if  type(subject) != int and type(subject) != float:
        q = subject[0].upper()
        new_subject.append(q + subject[1:].lower())
    else:
        continue
    
print(new_subject)
    
