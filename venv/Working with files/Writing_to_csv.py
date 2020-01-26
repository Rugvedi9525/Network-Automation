import csv

'''Writing Content to a csv file
Writer function is used to write to a csv
We can write in rows
Items in the list will be converted to columns in the CSV
'''
with open('Numbers_csv.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['x','x**2','x**3'])
    for x in range (1,101):
        writer.writerow([x,x**2,x**3])

'''
If the file is not comma separated file, instead there are some other delimiters,
then we can mention the additional parameters when opening the file
for example:
with open('Numbers_csv.csv', 'w', delimiter=':', lineterminator='\n') as file:

Or we can define csv dialects, in which we can set our own parameters and define a name for the customized dialect
for example:
csv.register_dialect('hashes',delimiter='#',quoting=csv.QUOTE_NONE, lineterminator = '\n')
with open('Numbers_csv.csv', 'w') as file:
    reader = csv.reader(file, dialect = 'hashes')
    

'''