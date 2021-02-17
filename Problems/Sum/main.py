# read sums.txt
test_file = open('sums.txt', 'r')

for line in test_file:
    num1, num2 = line.split()
    print(int(num1) + int(num2))

test_file.close()
