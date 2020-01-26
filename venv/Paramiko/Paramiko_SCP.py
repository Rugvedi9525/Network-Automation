import paramiko
import scp


#SSH Client
linux_ipaddress = '10.1.1.10'
ssh_client= paramiko.SSHClient()

#SSH Connection
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=linux_ipaddress, port=22, allow_agent=False, username='rugsi', password='cisco', look_for_keys=False)

#SCP setup
scp = scp.SCPClient(ssh_client.get_transport())

#Put files on the remote host
scp.put('FILE', 'DESTINATION PATH')

#Put directory on the remote host
scp.put('DIRECTORY', recursive=True, remote_path='DESTINATION PATH')

#Get files from the remote host
scp.get('FILE PATH TO COPY THE FILE/DIRECTORY', 'FILE TO GET')

#Close the scp conneciton
scp.close()