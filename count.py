from posixpath import split


words = "navgurukul is great"
x=words.split()
print(x)
counter = 0
while counter < len(x):
    print (x[counter])
    counter+=1
