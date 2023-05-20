from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . models import Book

# Create your views here.

def index(request):
    context={}
    return render(request, "web/index.html",context)

def about(request):
    context={}
    return render(request, "web/about-us.html",context)

def shop(request):
    book = Book.objects.all()
    context={
        "book" :book,
    }
    return render(request, "web/books-grid-view.html",context)

def book_detail(request,id):
    book = Book.objects.get(id=id)
    # comments = Comment.objects.all()

    context = {
        "book": book,
        # "comments":comments,
    }
    return render(request,"web/books-detail.html",context)

def contact(request):
    context={}
    return render(request, "web/contact-us.html",context)

def register_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if(pass1!=pass2):
            print('password not equal'*20)
            return redirect('web:signup')
        else:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                return redirect('web:signup')
            else:
                customer = User.objects.create_user(username=username,password=pass1)
                return redirect('web:login')
           

    return render(request,"web/shop-register.html")
          
def login_1(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('web:index')
        else:  
            print('hi')
            return redirect('web:login')
    return render(request,"web/shop-login.html")

def logout_1(request):
    logout(request)
    return redirect('web:index')