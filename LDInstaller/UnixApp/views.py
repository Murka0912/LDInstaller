from django.shortcuts import render
from . import unix_upload
# Create your views here.
def main(request):
    test = 'by world'
    return render(request,'main.html',{'test':test})


def upload(requset):
    host = "172.29.17.130"
    username = "root"
    password = "Landocs123"

    port = 22
    uploading = unix_upload.upload_to_unix(host=host,port=port,username=username,password=password)
    s = unix_upload.ssh_cli(host,port,username,password)
    return render(requset, 'main.html', {'OK':uploading,
                                         'ls':s})