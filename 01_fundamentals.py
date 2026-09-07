
var1 = 40
var2 = 60
var3 = var1 + var2
print(var3)

# fundamental data structures.

arr = [30,40,100,99,-1,"Harry Potter Chamber of Secrets, by JK Rowling."]
#      0   1  2  3   4                                                 5

print(arr[0])

var4= {
"name":"Andrei",
"age" :20
}
print(var4)
def add(a, b):
    result = a + b
    return result

def multiply(a: int,b:int)-> int:
    return a*b

var5=add(4,10)
print(var5)

var6=multiply(3.5,5)
print(var6)


offer_letter = True
if offer_letter == True:
         print("All good!")
else:
         print ("Not good dawg")


age = 30
if age >25:
    print("Bătrân")

#range -> iterator.
for i in range(10):
    print(i)

i = 0
while i < 30:
    print(i)
    i= i+1

while True:
    user_input = input("you>")
    if user_input in ["q", "quit", "exit", "bye"]:
        break
    print(user_input)
