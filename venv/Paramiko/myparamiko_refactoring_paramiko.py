import paramiko
import time


def open_connection(ipaddress, port, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ipaddress, port=port, username=username, password=password, look_for_keys=False, allow_agent=False)
    return ssh_client

def invoke_shell(ssh_client):
    remote_connection = ssh_client.invoke_shell()
    return remote_connection

def send_command(remote_connection, command):
    remote_connection.send(command + '\n')
    time.sleep(3)

def recv_output(remote_connection):
    return (remote_connection.recv(4096).decode())

def close_connection(ssh_client):
    ssh_client.close()


#Testing the myparamiko script
ssh_client = open_connection('10.1.1.10',22, 'rugsi','cisco')
remote_connection = invoke_shell(ssh_client)
send_command(remote_connection, 'show version')
recv_output(remote_connection)
close_connection(ssh_client)
