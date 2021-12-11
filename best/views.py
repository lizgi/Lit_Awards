from django import forms
from django.shortcuts import render,redirect
from django.http  import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Project
from .forms import showprojectform,UpdateProfileForm

# Create your views here.

def index(request):
    project = Project.objects.all().order_by('-id')
    return render(request, 'all-best/index.html',{'project':project})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile.html",{'profile':profile})

@login_required(login_url='/accounts/login/')
def showProject(request):
    if request.method == "POST":
        form = showprojectform(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
        return redirect('/')
    else:
        form = showprojectform()
    return render(request, 'show_project.html', {"form": form})

def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():      
                profile = form.save(commit=False)
                profile.save()
                return redirect('laurels:profile' ,username=user.username) 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)    