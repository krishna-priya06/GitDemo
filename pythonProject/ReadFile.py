# file = open('test.txt')
# print (file.read()) #to read and print content of a file
# file.close()
#
# #to read and print specific bytes or characters in a file
#
# file1 = open('test.txt')
# print (file1.read(5)) #to read and print content of a file
# file1.close()

##to read and print line by line  in a file
# file2 = open('test.txt')
# #print (file2.read(5)) #to read and print content of a file
# print(file2.readline())
# print(file2.readline())
# file2.close()

#VERYIMPORTANT INTERVIEW QUESTION - HOW TO READ A FILE LINE BY LINE
# file = open('test.txt')
# line = file.readline()
# while line !="":
#     print(line)
#     line= file.readline()
# file.close()
#
# file = open('test.txt')
# lines = file.readlines()
# print(lines)
# #print(lines)
# #print(lines[0])
# file.close()

file = open ('test.txt')
lines = file.readlines()
for line in lines:
    print(line)
file.close()

