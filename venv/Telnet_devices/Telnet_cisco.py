import telnetlib
import getpass


#There are three ways to enter the password
host = '10.1.1.5'
username = 'rugsi'
password = getpass.getpass()


#Make a telnet connection to the device


telnet = telnetlib.Telnet(host)
telnet.read_until(b'Username: ')
telnet.write(username.encode() + b'\n')
telnet.read_until(b'Password: ')
telnet.write(password.encode() + b'\n')

#Enter the enable mode
telnet.write(b'enable\n')
telnet.write(password.encode()+b'\n')

#Run commands
telnet.write(b'terminal length 0\n')
telnet.write(b'show running-config\n')
telnet.write(b'exit\n')
output = telnet.read_all().decode()
print (output)