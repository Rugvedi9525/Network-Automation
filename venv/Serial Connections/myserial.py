import serial
import time

def open_port(con = 'com3', baudrate = '9600'):
    with serial.Serial(con, baudrate, stopbits=1, bytesize=8, timeout=8, parity='N') as console
        if console.isOpen():
            return console
        else:
            return ("Error opening the port!")

def execute_commands(console, command = '\n', sleep):
    console.write(command.encode() + b'\n')
    time.sleep(sleep)

def read_output(console):
    bytes_to_be_read = console.inWaiting()
    if bytes_to_be_read:
        output = console.read(bytes_to_be_read)
        print (output.decode())
    else:
        print("Nothing to read")


def initial_config(console):
    execute_commands(console)
    output = read_output(console)
    if 'Would you like to enter the initial configuration dialog?' in output:
        execute_commands(console, "no", 15)
        execute_commands(console, '\r\n')




