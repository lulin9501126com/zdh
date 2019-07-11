from django.shortcuts import render,HttpResponse,redirect

from  web import  models
from web import modelform
# Create your views here.

def register(request):
    if request.method == 'GET':
        register_obj = modelform.Register()
        return render(request,"register.html",{"register_obj":register_obj})

    if request.method == 'POST':
        register_obj = modelform.Register(request.POST)
        if register_obj.is_valid():
            register_obj.save()

            return  redirect('login')
        else:
            return render(request,"register.html",{'register_obj':register_obj})




def login(request):
    if request.method == 'GET':
        return  render(request,'login.html')

    else:
        username = request.POST['username']
        password = request.POST['password']
        obj = models.Userinfo.objects.filter(username=username,password=password).exists()
        if obj:
            return render(request,'index.html')
        else:
            return redirect('login')
