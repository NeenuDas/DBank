# from django.contrib import auth,messages
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from django.shortcuts import render, redirect


# Create your views here.

#     # return HttpResponse("Hello world")
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth

from Bankapp.models import Customer


# Create your views here.
def demo(request):
    obj = Customer.objects.all()
    return  render(request,"success.html",{'result':obj})
def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is  not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('login')
    return  render(request,"login.html")

def register(request):
    if request.method== 'POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME Already Exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname,email=email)
                user.save();
                return  redirect('login')
       #print("USER CREATED SUCCESSFULLY")
        else:
            messages.info(request,"Password Not matched")
            return redirect('register')
        return redirect('/')

    return render(request, "register.html")

def app_form(request):
    return render(request, "app_form.html")

def logout(request):
        if request.user.is_authenticated:
            auth.logout(request)
            return redirect('logout')
        return redirect('/')


def home(request):
    districts = ['Ernakulam', 'Kottayam', 'Thrissur', 'Kozhikode', 'Kollam']
    return render(request, 'Home.html', {'districts': districts})

def sucess(request):
    return render(request, 'success.html')