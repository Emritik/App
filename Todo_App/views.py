from django.shortcuts import render, redirect
from .models import Todos
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        details = request.POST.get('details')
        
        Todos.objects.create(
            title = title,
            details = details
        )
        messages.success(request, "Your item is susseccfully added")
        return redirect('/')
    
    data = Todos.objects.all()
    context = {'datas':data}
        
    return render(request, 'index.html',context)

def delete(request, id):
    data = Todos.objects.filter(id=id)
    data.delete()
    messages.warning(request, "Your item is  deleted!!")
    return redirect('/')

def edit(request, id):
    
    data = Todos.objects.get(id = id)
    
    if request.method == "POST":
        title = request.POST.get('title')
        details = request.POST.get('details')
        
        data.title = title
        data.details = details
        
        data.save()
        return redirect('/')
    messages.success(request, "Your item is susseccfully edited!!")
    context = {'datas':data}
    
    return render(request, 'edit.html', context)

def loginuser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return  redirect("/")

        else:
            return redirect( '/login')
            
    return render(request, 'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")

class SignupView(generic.CreateView):
    template_name = "signup.html"
    form_class = CustomUserCreationForm
    
    def get_success_url(self):
        return (reverse("login"))    