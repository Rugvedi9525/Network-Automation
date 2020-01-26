'''
There are two ways to establish a connection with devices using Netmiko
1. Using Netmiko class from the netmiko module
1. Using ConnectHandler
'''

cisco_device = {
    'device_type': 'cisco_ios',
    'ip':'10.1.1.10',
    'username':'rugsi',
    'password': 'cisco',
    'port':'22',
    'secret':'cisco'
}

#Method 1 to establish connection
from netmiko import Netmiko

connection = Netmiko(**cisco_device)
output = connection.send_command('show ip int brief')
print (output)
connection.disconnect()


#Method 2 to establish connection with the Device

from netmiko import ConnectHandler

connection = ConnectHandler(**cisco_device)
output = connection.send_command('show ip int brief')
print (output)
connection.disconnect()
