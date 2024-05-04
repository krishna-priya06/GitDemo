def ispalindrome(s):
    return s==s[::-1]

print(ispalindrome("neon"))

str = "cook"
size = len(str)
print (size)
#print(str[2])
output = ""
while size>0:
    output = output + str[size-1]
    size = size -1

print(output)

print(str[::-1])





