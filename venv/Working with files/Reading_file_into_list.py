#Iterating through the file using a for loop.
print ("="*100)
with open('config.txt') as file:
    for line in file:
        print(line)

#Saving the contents of the file to a list using splitlines() method and iterating through the list
print ("="*100)
with open('config.txt') as file:
    mycontent_list = file.read().splitlines()
    print (mycontent_list)

#Saving the contents of the file to a list using readlines() method and iterating through the list
#Drawback with readlines() method is that it includes the \n at the end of each line.
print ("="*100)
with open('config.txt') as file:
    mycontent_list = file.readlines()
    print (mycontent_list)

#Another useful method is the readline() method using which we can just print a single line.
print ("="*100)
with open('config.txt') as file:
    print(file.readline())
    print(file.readline())

#If \n exists at the end of the lines, in order to get rid of it use a space as the end.
print ("="*100)
with open('config.txt') as file:
    for line in file:
        print(line, end=' ')

print ("="*100)
