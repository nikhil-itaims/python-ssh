import paramiko

# ssh connection
host = "IP addreess" 
username = "username"
password = "password"
client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)

file_content = "This file content is created using ssh connection in python script!"

dir = 'path to the directory where the file is being created'

cmd = 'echo "' + file_content + f'">>{dir}/nginx'
client.exec_command(f'{cmd}')
print("File has been created")
client.close()
