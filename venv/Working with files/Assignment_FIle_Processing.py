#The csv approach

import csv
with open('colon_csv.csv') as file:
    reader = csv.reader(file, delimiter= ':')
    content = []
    for row in reader:
        content.append(row)
    print (content)

#General file approach
with open('colon_csv.csv') as file:
    read = file.read().splitlines()
    content = []
    for item in read:
        tmp = item.split(':')
        content.append(tmp)
    print (content)

