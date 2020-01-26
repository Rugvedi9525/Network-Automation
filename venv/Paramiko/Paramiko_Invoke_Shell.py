import paramiko
import time
'''
Invoke the shell, send commands on the shell and make sure you sleep for sometime 
to make all the commands finish execution on time
then go ahead and close the connection
'''


ssh_client= paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('10.1.1.10', port=22, allow_agent=False, username='rugsi', password='cisco', look_for_keys=False)
remote_con = ssh_client.invoke_shell()
remote_con.send('enable\n')
remote_con.send('cisco\n')
remote_con.send('configure terminal\n')
remote_con.send('int loopback 0\n')
remote_con.send('ip address 1.1.1.1 255.255.255.255\n')
remote_con.send('int loopback 1\n')
remote_con.send('ip address 2.2.2.2 255.255.255.255\n')
remote_con.send('router ospf 1\n')
remote_con.send('net 0.0.0.0 0.0.0.0 area 0\n')
remote_con.send('end\n')


time.sleep(3)

print (remote_con.recv(4096).decode())
ssh_client.close()

