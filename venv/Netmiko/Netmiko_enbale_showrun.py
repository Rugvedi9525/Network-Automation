'''
When we first ssh into a device we are not in the enable mode, therefore we cannot execute show run.
Therefore we need to first execute enable command
Enter the enable mode and then execute the show run command
'''

cisco_device = {
    'device_type': 'cisco_ios',
    'ip':'10.1.1.10',
    'username':'rugsi',
    'password': 'cisco',
    'port':'22',
    'secret':'cisco'
}

from netmiko import Netmiko

connection = Netmiko(**cisco_device)
output = connection.send_command('show ip int brief')

#Check if enable mode and enter enable mode if not
prompt=  (connection.find_prompt())
print (prompt)

if '>' in prompt:
    connection.enable()

print (connection.find_prompt())

 #Entered the enable mode
output = connection.send_command('show run')
print (output)



print (connection.check_config_mode())
if not connection.check_config_mode():
    connection.config_mode()
print('Switched to config mode')
print (connection.check_config_mode())

connection.disconnect()