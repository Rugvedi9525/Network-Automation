'''
SSHing is pretty much similar for all the devices, but specifically for the linux machines the problem occurs
 because we have to execute commands as root
and also enter the password after executing the command. The following code shows how to do that.
'''
import paramiko
linux_machine_ip = ''
ssh_client=paramiko.SSHClient()
ssh_client.set_mising_host_keys_policy(paramiko.AutoAddPolicy())
ssh_client.connect(linux_machine_ip, port=22,usernam='rugsi',password='rugsi' ,look_for_keys=False, allow_agent=False)
input, output, error = ssh_client.exec_command('sudo apt get update \n')
input.write('rugsi\n')
print (output.read().decode())
ssh_client.close()