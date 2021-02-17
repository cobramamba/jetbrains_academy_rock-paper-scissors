# read sample.txt and print the number of lines
test_file = open('sample.txt', 'r')
print(len(test_file.readlines()))
test_file.close()
