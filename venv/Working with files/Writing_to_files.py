#Default mode is always read so we have to change it to WRITE.
'''First check if the file exists.
If it doesn't exist it creates a file.
Overwrites all the content of the file with the data mentioned.
NOTE: No access to the cursor in this mode.
'''
with open('config1.txt', 'w') as file:
    file.write('Shivbaba is with Rugvedi\n')

'''First check if the file exists.
If it doesn't exist it creates a file.
Appends all the content to the end of the.
IMPORTANT: Doesnt append the data to a new line in the file. But simply to the end of file.
Therefore, to append to a new line we have to explicitly add 
NOTE: No access to the cursor in this mode
'''
with open('config1.txt', 'a') as file:
    file.write('What I have studied has been asked in the interview and I have surprised my papa darling')

'''First check if the file exists.
If the file doesnt exist. IT THROWS AN ERROR
NOTE: There is access to the server in this mode.
It doesn't overwrite all the contents of the file, it just overwrites the content at the beginning of the file'''
with open('config1.txt', 'r+') as file:
   file.write('Shivbaba is my father and he has given me everything I want\n')



'''
First check if the file exists.
If it doesn't exist it goes ahead and creates the file.
Have access to the cursor
and Again appending just adds to the end of the file and not to a new line
'''
with open('config1.txt', 'a+') as file:
   file.writelines('I have got the job at Facebook Shivbaba!')
   file.seek(5)
   print (file.read(3))

