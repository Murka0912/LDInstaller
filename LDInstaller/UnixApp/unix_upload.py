import paramiko
import os

for dir,path,files in  os.walk('.\\'):
    print(dir)

def upload_to_unix(host,port,username,password):
    transport = paramiko.Transport(host, port)

    destination_path = "/home/dimm/test123.txt"
    local_path = ".\\UnixApp\\uploads\\rpms\\test.txt"  #if using google colab, this will work with no modifications. Otherwise, overwrite with your local file path to the file

    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(local_path, destination_path)

    sftp.close()
    transport.close()
    ok = 'OK'
    return ok

def ssh_cli(host,port,username,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password, port=port)
    a, b, c = ssh.exec_command('ls -la')
    return a