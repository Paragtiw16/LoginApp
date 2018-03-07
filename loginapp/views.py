# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def loginreq(request):

    if request.method == "POST":
        print("Inside Post Method")
        get_uname=request.POST.get("uname")
        print(get_uname)

        return render(request, "login.html", {"username": get_uname})




def loginform(request):

     if request.method=="GET":
        return render(request, "signup.html")

