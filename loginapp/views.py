# from django.shortcuts import render

# Create your views here.
# import password as password
from django.http import request
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from loginapp.models import Login


@csrf_exempt
def loginreq(request):

    if request.method == "POST":
        get_uname=request.POST.get('uname')
        get_pwd=request.POST.get('pwd')
        get_email=request.POST.get('email')
        login_details = Login.objects.create(username=get_uname,password= get_pwd,email= get_email)
        # login_details =Login(username=get_uname,password= password,email= email)
        login_details.save()
        return render(request, "login.html")



def loginform(request):

     if request.method=="GET":
        return render(request, "signup.html")



def login_reqq(request):

     if request.method=="GET":
         return render(request,"match.html")


@csrf_exempt
def auth(request):
     if request.method=="POST":
         data = Login.objects.all()
         for i in data:
             user=(i.username)
             pssword =(i.password)
             email=(i.email)
         # user= data.username
         # pssword =data.password
         # email=data.email
         get_pwd=request.POST.get('pwd')
         get_email=request.POST.get('email')

     if pssword==get_pwd and email==get_email:
             return render(request, "user.html" ,{"Username":user})


