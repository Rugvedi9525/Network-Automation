'''
Executing commands on the device that are saved on the file
'''
from netmiko import ConnectHandler

cisco_device = {
    'device_type': 'cisco_ios',
    'ip':'10.1.1.10',
    'username':'rugsi',
    'password': 'cisco',
    'port':'22',
    'secret':'cisco'
}

connection = ConnectHandler(**cisco_device)
connection.enable()
connection.config_mode()
connection.send_config_from_file('ospf.txt')
connection.disconnect()
