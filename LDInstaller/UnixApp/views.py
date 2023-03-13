from django.shortcuts import render
from django.contrib.auth.models import User
from . import unix_upload
from . forms import RegForm
from . models import Srv_map, components
# Create your views here.
def main(request):
    test = 'by world'
    path, files, filelist = unix_upload.list_files('.\\uploads\\')
    components.objects.all().delete()
    for f in filelist:
        print(f)


        save= components.objects.create(nameComp=f, nameFilepath=f)
    model = components.objects.all()
    return render(request,'main.html',{'files':files,
                                       'objects':model})


def add_srv(request):
    form = RegForm()
    if request.method =='POST':
        if form.is_valid():
            form.save()
    return render(request,'env.html',{'form':form})


def upload(requset):
    model = Srv_map.objects.all().filter(ip_addr='172.29.17.130')
    for g in model:

        host = g.ip_addr
        username = g.username
        password = g.password

        port = 22

        path, files, filelist = unix_upload.list_files('.\\uploads\\')
        print(filelist)
        print(files)
        k=0
        for s in filelist:
            for f in files:
                print(s)
                k+=1
                uploading = unix_upload.upload_to_unix(host=host,
                                               port=port,
                                               username=username,
                                               password=password,
                                               source_path=s,
                                               dest_path='/home/dimm/rpms1/'+f
                                               )

    return render(requset, 'main.html', {'OK':uploading
                                         })

def ls(requset):
    model = Srv_map.objects.all().filter(ip_addr='172.29.17.130')
    for a in model:
        print(a.password)
        host = a.ip_addr
        username = a.username
        password = a.password
        port = 22
        s = unix_upload.ssh_cli(host, port, username, password)
        print(s)
    return render(requset, 'main.html',{'ls':s})

def file_list(request):
    path,files, filelist = unix_upload.list_files('.\\uploads\\')
    print(files)
    return render(request,'main.html', {'files':files,
                                        'path':path,
                                        'filelist':filelist})