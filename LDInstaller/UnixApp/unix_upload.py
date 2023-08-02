import paramiko
import os
import base64



def upload_to_unix(host,port,username,password, source_path, dest_path):
    transport = paramiko.Transport(host, port)


    print(dest_path)

    local_path = source_path  #if using google colab, this will work with no modifications. Otherwise, overwrite with your local file path to the file
    print(source_path)
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    for s_file in local_path:
        print(s_file)
        sftp.put(s_file, dest_path)

    sftp.close()
    transport.close()
    ok = 'OK'
    return ok

def ssh_cli(host,port,username,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password, port=port)
    a, b, c = ssh.exec_command('mkdir /home/dimm/rpms1')

    a1, b2, c2 = ssh.exec_command('ls -la /home/dimm/rpms1')
    s = b2.readlines()
    return s

def list_files(dir):
    fileslist= []
    fileslist1 = {}
    for path,folder,files in os.walk(dir):
        #print(path)
        for f in files:
            dirs = path+'\\'+f
            fileslist1[f] = dirs
        #print(fileslist1)
        return  fileslist1
host='172.29.17.130'
port=22
username='root'
password='Landocs123'

#print(ssh_cli(host,port,username,password))