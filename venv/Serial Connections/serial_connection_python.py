import serial
import time

#Opening a console port
with serial.Serial('COM3', baudrate=9600, stopbits=1, bytesize=8, timeout=8, parity='N') as console:
    if console.isOpen():
        print ("Console port is open")

    # Send/Execute commands on a networking device using the serial connection
    '''
    Two very important methods are used to write and read from the serial connection
    console.write
    console.read (dependency ==> console.inWaiting()
    '''
        console.write(b'\n')
        time.sleep(2)
        console.write(b'enable\n')
        time.sleep(3)
#Show version command doesn't display the entire data, we have to press space to show more and come to the console.
        console.write(b'terminal length 0\n')
        time.sleep(3)
        console.write(b'show version\n')
        time.sleep(3)

#Now to read the output in the console
        bytes_to_be_read = console.inWaiting()
        output = console.read(bytes_to_be_read)
        print(output.decode())

    else:
        print ("Error opening the console port.")



Name = "Rugvedi"
Name_encoded = Name.encode()
console.write



#Refactoring  pyserial to create our own myserial module
