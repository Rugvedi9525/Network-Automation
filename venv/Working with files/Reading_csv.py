import csv
print ('='* 200)
'''
Reading from the csv file is done using the reader object 
Printing the reader object doesnt actually print the contents of the reader infact it just prints the location of the object. 
'''
with open('airtravel_csv.csv') as file:
    content = csv.reader(file)
    print (content)
print ('='* 200)
'''
In  order to print the contents of the csv file we need to iterate over the reader object using the for loop. 
'''
with open('airtravel_csv.csv') as file:
    content = csv.reader(file)
    for row in content:
        print (row)
print ('='* 200)

'''
If you dont want to print the Headers of each row i.e the first column we can skip it using an inbuilt fucntion called next
'''

with open('airtravel_csv.csv') as file:
    content = csv.reader(file)
    next(content)
    for row in content:
        print (row)
print ('='* 200)

'''In order the read the contents of the csv without using the inbuilt next function to skip the first column or the header of each row
'''
with open('airtravel_csv.csv') as file:
    content = csv.reader(file)
    next(content)
    count = 0
    for row in content:
        if count == 0:
            print ()
            count +=1
        else:
            print (row)
            count +=1
print ('='* 200)

'''In order to print the maximum number of any element in the dictionary
'''
max_1958 = dict()
with open('airtravel_csv.csv') as file:
    content = csv.reader(file)
    next(content)
    for row in content:
        max_1958[row[0]] = row[1]

    max1 =  (max(max_1958.values()))
    print (max_1958)
    # Iterating through the dictionary:
    for key,value in max_1958:
        if max1 = value:
            print (key)
print ('='* 200)

'''
In order to count the number of times a value occurs
'''
with open('airtravel_csv.csv') as file:
    content = csv.reader(file)
    count = dict()
    next(content)
    for row in content:
        if (row[1] in count):
            count[row[1]] +=1
        else:
            count[row[1]] = 1
print (count)



