# create the planets.txt
planet_list = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

file = open('planets.txt', 'w', encoding='utf-8')

for planet in planet_list:
    file.write(planet + '\n')

file.close()
