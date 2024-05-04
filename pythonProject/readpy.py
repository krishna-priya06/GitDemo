# file =open("readfile.txt")
# # print(file.read())
# print(file.readline())
# print(file.readline())
# file.close()

# file =open("readfile.txt")
# print(file.read(16))
#
# file.close()

# file = open('newtext.txt')
# line =file.readline()
# while line!= '':
#     print(line)
#     line =file.readline()
# file.close()

# file = open('newtext.txt')
# line = file.readlines()
# for line in reversed(line):
#     print (line)

with open('family.txt','r') as rf:
    content= rf.readlines()
    reversed(content)
    with open('family.txt','w') as wf:
        for line in reversed(content):
            wf.write(line)


