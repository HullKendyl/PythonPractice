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

#search using prefix
fhand = open('textFile.txt')
for line in fhand:
    #rstrip() removes the whitespace line between lines of text
    line = line.rstrip()
    if line.startswith('Gus:') :
        print(line)
        
# using in operator
fhand = open('textFile.txt')
for line in fhand:
    line = line.rstrip()
    if not 'Dog' in line :
        continue
    print(line)

# prompt for file name & add try except block
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File name does not exist. File cannot be opened:', fname)
    quit()
count = 0
for line in fhand: 
    if line.startswith('Gus:') :
        count = count + 1
print('There were', count, 'Gus speaking lines in', fname)

#lists
students = ['Cody', 'Marlow', 'Henry', 'Theodore']
print(len(students))
print(range(len(students)))

for student in students :
    print(student, 'is a student in the class.')
    
for i in range(len(students)) :
    student = students[i]
    print(student, 'is a student.')
    
