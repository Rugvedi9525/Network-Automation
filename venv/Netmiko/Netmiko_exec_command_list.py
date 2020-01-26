''' Multiple commands can  be executed on a device from a list or from a file'''

from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip':'10.1.1.10',
    'username':'rugsi',
    'password': 'cisco',
    'port':'22',
    'secret':'cisco'
}

#List of commands
commands = ['int loopback 3', 'ip address 3.3.3.3 255.255.255.255','exit']
connection = ConnectHandler(**cisco_device)
connection.enable()
connection.config_mode()
output = connection.send_config_set(commands)
print (output)
connection.send_command_expect('wr')
connection.disconnect()
