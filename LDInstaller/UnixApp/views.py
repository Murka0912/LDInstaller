from django.shortcuts import render
from django.contrib.auth.models import User
from . import unix_upload
from . forms import RegForm
from . models import Srv_map, components
# Create your views here.
def main(request):
    filelist = unix_upload.list_files('.\\uploads\\')
    print(filelist)
    components.objects.all().delete()

    destpath = '/home/dimm/new_cat/'
    print(filelist)
    install_file_name=''
    with open('.\\uploads\\install.sh', 'w', encoding='utf-8') as install_file:

        for f in filelist:
        #print(f , filelist[f])
            save= components.objects.create(nameComp=f, nameFilepath=filelist[f])

            if f !='install.sh':
                install_file_name = install_file_name+destpath+f+' '
        install_file.write('yum -y localinstall '+install_file_name)
        install_file.close()
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
                                               source_path=filelist,
                                               dest_path='/home/dimm/new_cat/'
                                               )

    return render(requset, 'main.html', {'OK':"OK"
                                         })

def ls(requset):
    model = Srv_map.objects.all().filter(ip_addr='172.29.17.130')
    for a in model:
        host = a.ip_addr
        username = a.username
        password = a.password
        port = 22
        dest_path = '/home/dimm/new_cat/'
        s,s1 = unix_upload.ssh_cli(host, port, username, password,dest_path)
        print(s)
    return render(requset, 'main.html',{'ls':s})

def file_list(request):
    path,files, filelist = unix_upload.list_files('.\\uploads\\')
    print(files)
    return render(request,'main.html', {'files':files,
                                        'path':path,
                                        'filelist':filelist})

def get_version(request):
    model = Srv_map.objects.all().filter(ip_addr='172.29.17.130')
    for a in model:
        host = a.ip_addr
        username = a.username
        password = a.password
        port = 22
        versions = unix_upload.version_component(host,port,username,password)
        return render(request, 'main.html', {'versions':versions})