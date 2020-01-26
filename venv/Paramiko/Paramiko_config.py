#Paramiko is used to implement ssh version 2 protocol
'''
So a ssh connection authentication can be done 2 ways.
1. using a password
2. using public and private keys


Step1: Is to create a ssh client
Step2: Make to set the Add set_missing_host_key_policy(paramiko.AddPolicy())
Step3: If using the device local database(username and password to login) make sure to set these parameters to False --> Look_for_keys =False and allow_agent=False
Step4: Execute commands on the device, make sure to remember that the execute command returns the tuple(input, outout, error occured)
Step5: VERY IMPORTANT. Make sure to explicitly close the ssh connection.
'''
import paramiko

ssh_client = paramiko.SSHClient() # Creating a ssh client
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Store the keys if they dont exist.
ssh_client.connect('10.1.1.10', port=22, username='rugsi', password='cisco', allow_agent=False, look_for_keys=False) #Connect to the device

input, output, error  = ssh_client.exec_command(b'show version') #Execute commands on the device

print(output.read().decode()) #Reading the output

ssh_client.close() #Close the connection
''' If we dont close the connection the Python Interpreters Garbage collector will close the connection'''




