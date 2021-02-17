# read animals.txt
# Open file 'animals.txt' to write list of animals from animal_list_1
# file = open('animals.txt', 'w', encoding='utf-8')

# animal_list_1 = ['rabbit', 'cat', 'turtle']

# for animal in animal_list_1:
    # file.write(animal + '\n')

# file.close()

# Open file 'animals.txt' to read list of animals and add them to animal_list_2
file = open('animals.txt', 'r')

animal_list_2 = []

# Read each line, remove '\n' from each animal string, and append animal to animal_list_2
for line in file:
    animal_list_2.append(line.rstrip('\n'))

number_animals = int(len(animal_list_2))
animal_chain = ''

for i in range(0, number_animals - 1):
    animal_list_2[i] = animal_list_2[i] + ' '
    animal_chain = animal_chain + animal_list_2[i]

animal_chain = animal_chain + animal_list_2[number_animals - 1]

file.close()

# and write animals_new.txt
file = open('animals_new.txt', 'w', encoding='utf-8')

file.write(animal_chain)

file.close()
