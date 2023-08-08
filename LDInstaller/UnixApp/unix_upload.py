import paramiko
import os
import base64



def upload_to_unix(host,port,username,password, source_path, dest_path):
    transport = paramiko.Transport(host, port)



    print(source_path)
    transport.connect(username = username, password = password)
    sftp = paramiko.SFTPClient.from_transport(transport)
    for s_file in source_path:
        #print(s_file)
        sftp.put(source_path[s_file], dest_path+s_file)

    sftp.close()
    transport.close()
    ok = 'OK'
    return ok

def ssh_cli(host,port,username,password, dest_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password, port=port)
    a2, b2, c2 = ssh.exec_command('cd ' + dest_path)


    a, b, c = ssh.exec_command('ls -la')
    s1=b.readlines()

    a1, b1, c1 = ssh.exec_command('bash '+dest_path+'install.sh')
    s = b1.readlines()
    return s, s1

def version_component(host,port,username,password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password, port=port)
    a2, b2, c2 = ssh.exec_command('yum list installed |grep landocs')
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
        print(fileslist1)
        return  fileslist1
"""host='172.29.17.130'
port=22
username='root'
password='Landocs123'
"""

"""dest_path = '/home/dimm/new_cat/'
s,s1  = ssh_cli(host, port, username, password,dest_path)
print(s1)
for a in s:
    print(a)"""


#print(ssh_cli(host,port,username,password))