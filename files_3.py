fhand = open('textFile.txt')
#count
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

#read
fhand = open('textFile.txt')
print(fhand.read())

#len() returns the number of items in an object or number of characters in
# a string
mylist = ["apple", "orange", "cherry", "pear"]
x = len(mylist)
print('Total Number of Fruit: ', x)

