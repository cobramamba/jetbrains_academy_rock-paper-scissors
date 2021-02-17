# put your python code here
grades = input()
# grades = 'F B A A B C A D'
grades = grades.split()

counter = int(0)

for i in grades:
    if i == 'A':
        counter += 1
    else:
        pass

print(round(counter / len(grades), 2))
