# write the code here
line = str(input())

file = open('input.txt', 'w', encoding='utf-8')

file.write(line)

file.close()
