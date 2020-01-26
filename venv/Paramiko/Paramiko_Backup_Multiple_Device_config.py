'''
Backing up configuration of multiple devices
Step1: SSH Connection
Step2: Get the current running configuration
Step3: Delete the unwanted content from the configuration
Step4: Save the config to a text file
'''

import myparamiko_refactoring_paramiko
import datetime
devices = ['10.1.1.10']
for device in devices:
    ssh_client = myparamiko_refactoring_paramiko.open_connection(device, 22, 'rugsi','cisco')
    remote_connection = myparamiko_refactoring_paramiko.invoke_shell(ssh_client)
    myparamiko_refactoring_paramiko.send_command(remote_connection, 'show run')
    output = myparamiko_refactoring_paramiko.recv_output(remote_connection)
    list = output.split('\n')
    list=list[4:-1]
    backup_config = '\n'.join(list)
    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-'+ str(now.day)
    file = device + '-' + today
    with open(file, 'w') as file:
        file.write(backup_config)
    myparamiko_refactoring_paramiko.close_connection(ssh_client)

