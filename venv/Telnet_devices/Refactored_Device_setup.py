
class Device():

    def __init__ (self, ipaddress, username, password, connection=None):
        self.ipaddress = ipaddress
        self.username = username
        self.password = password
        self.connection = connection

    def telnet_connection(self):
        import telnetlib
        self.connection = telnetlib.Telnet(self.ipaddress)
        print ("Connection successful")

    def authentication(self):
        self.connection.read_until(b'Username: ')
        self.connection.write(self.username.encode() + b'\n')
        self.connection.read_until(b'Password: ')
        self.connection.write(self.password.encode() + b'\n')
        print ("Authentication successful!")


    def execute_commands(self, command):
        self.connection.write(command.encode() + b'\n')
        print("Command executed:" + command)

    def display_output(self):
        output = self.connection.read_all().decode()
        print (output)

with open('devices.txt') as file:
    devices = file.read().splitlines()
    ips = []
    for device in devices:
        tmp = device.split(':')
        ips.append(tuple(tmp))

for ip in ips:
    ip = Device(ip[0], 'rugsi', 'cisco')
    ip.telnet_connection()
    ip.authentication()
    with open('Router_config_commands.txt') as file:
        content = file.readlines()
        for cmd in content:
            ip.execute_commands(cmd)
    ip.display_output()
    print ('#'*200)


