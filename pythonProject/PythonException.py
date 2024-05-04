# Itemsincart = 0
# if Itemsincart!=2:
#     raise Exception ("the minimum items in cart should be 2")
Itemsinbag =1
assert (Itemsinbag==1)

# try and except
try:
    with open ("trest.txt",'r') as file:
        line = file.readline()
        print (line)
except Exception as e:
    print(e)
    print ("Reached on mars")
a = [1, 2, 3]
try:
	print ("Second element=",(a[1]))

	print ("Fourth element = ",(a[3]))

except Exception as e:
    print ("An error occurred")
    print(e)

