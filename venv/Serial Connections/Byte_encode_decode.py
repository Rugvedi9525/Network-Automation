Name = 'Rugvedi'
Blah = '&*@69*$#*$@($'

'''
Encoding string to  a byte of strings 
.encode('ENCODING FORMAT')
'''
Name_encoded = (Name.encode())
Blah_encoded = (Blah.encode())

print(Name_encoded)
print(Blah_encoded)

print(type(Name_encoded))
print(type(Blah_encoded))


'''
Decoding string to  a byte of strings 
.decode('ENCODING FORMAT')
'''
Name_decoded = Name_encoded.decode()
Blah_decoded = Blah_encoded.decode()

print(Name_decoded)
print(Blah_decoded)

print(type(Name_decoded))
print(type(Blah_decoded))



