

def GreetMe(name):
    print("Good Morning",name) #parameterised function

GreetMe("priya")

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def myaddition(a,b):

    sum=(a+b)
    print(sum)

myaddition(2,3)

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("priya", "kiran")

def my_function(*kids):
  print("The youngest child is " + kids[1])

my_function("Hiranmayi", "Nakshatra")