import telnetlib
import time


device_list = ['10.1.1.10', '10.1.1.11', '10.1.1.12']


for device in device_list:
    username = 'rugsi'
    password = 'cisco'
    telnet = telnetlib.Telnet(device)
    telnet.read_until(b'Username: ')
    telnet.write(username.encode() + b'\n')
    telnet.read_until(b'Password: ')
    telnet.write(password.encode() + b'\n')

    # Enter the enable mode
    telnet.write(b'enable\n')
    telnet.write(password.encode() + b'\n')

    # Run commands
    telnet.write(b'terminal length 0\n')
    telnet.write(b'show running-config\n')
    telnet.write(b'exit\n')
    output = telnet.read_all().decode()
    print(output)
    time.sleep(2)
