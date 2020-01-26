#Read all the contents of the file
f = open('config.txt', 'r' )
print ("="*50)

content = f.read()
print (content)
print ("="*50)

#After this the cursor is at the end of the text file, so reading anything after this will return only null
content = f.read(7)
print ("Cursor position is at the end of the file "+ str(f.tell()))
print ("Content = " + content)
print ("="*50)

print (f.closed)
f.close()
print (f.closed)


#Read only a few contents of the file and study the positionin of the cursor
f = open('config.txt', 'r' )
print ("="*50)

content = f.read(7)
print ("Content = " +content)
print ("="*50)
print ("Now the cursor position is at the end of 7 characters " + str(f.tell()))

#Now reading the file again will display the content from where the cursor position is currently.
content = f.read(7)
print ("Content =" +content)
print ("="*50)

#Now to move the position of the cursor back to zero.
f.seek(0)
print ("Now the cursor position at the beginning again " + str(f.tell()))
content = f.read(7)
print ("Content = " +content)
print ("Now the cursor position is back at the end of 7 characters " + str(f.tell()))
print ("="*50)


print (f.closed)
f.close()
print (f.closed)
print ("="*50)


#Using with to open, read and manipulate files.
#This method automatically closes the file and we don't need to explicitly close the file


with open("config.txt", 'r') as file:
    print(file.read())

print ("="*50)
print(file.closed)
print ("="*50)

