from netmiko import ConnectHandler

devices_list = list()
with open('devices.txt') as f:
    device = f.read().splitlines()

for ip in device:
    cisco_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'rugsi',
        'password': 'cisco',
        'port': '22',
        'secret': 'cisco'
    }
    devices_list.append(cisco_device)

for device in devices_list:
    connection = ConnectHandler(**device)
    connection.enable()
    connection.config_mode()
    file = input("Enter the config file: ")
    connection.send_config_from_file(file)
    connection.disconnect()
