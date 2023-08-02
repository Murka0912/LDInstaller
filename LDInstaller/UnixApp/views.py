from django.shortcuts import render
from django.contrib.auth.models import User
from . import unix_upload
from . forms import RegForm
from . models import Srv_map, components
# Create your views here.
def main(request):
    filelist = unix_upload.list_files('.\\uploads\\')
    components.objects.all().delete()
    print(filelist)
    for f in filelist:
        #print(f , filelist[f])
        save= components.objects.create(nameComp=f, nameFilepath=filelist[f])
    model = components.objects.all()
    return render(request,'main.html',{'objects':model})


def add_srv(request):
    form = RegForm()
    Comp_model = components.objects.all()
    if request.method =='POST':
        if form.is_valid():
            countries = form.cleaned_data.get('favorite_colors')
            form.save()
    return render(request,'env.html',{'form':form,
                                      'components':Comp_model})


def upload(requset):
    print('upload')
    model = Srv_map.objects.all().filter(ip_addr='172.29.17.130')
    for g in model:

        host = g.ip_addr
        username = g.username
        password = g.password

        port = 22
        print(f'host {host}')

        filelist = unix_upload.list_files('.\\uploads\\')
        #print(filelist)
        s_dir = []
        f_name = []
        for f in filelist:
            s_dir.append(filelist[f])
            print('s_dir=',s_dir)

        k=0

        uploading = unix_upload.upload_to_unix(host=host,
                                               port=port,
                                               username=username,
                                               password=password,
                                               source_path=s_dir,
                                               dest_path='/home/dimm/new_cat/'
                                               )

    return render(requset, 'main.html', {'OK':"OK"
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