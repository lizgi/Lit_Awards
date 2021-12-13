from django import forms
from django.shortcuts import render,redirect
from django.http  import HttpResponse, request
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile,Project
from .forms import showprojectform,UpdateProfileForm,ProfileForm
from django.http  import HttpResponse,HttpResponseRedirect

# Create your views here.

def index(request):
    project = Project.objects.all().order_by('-id')
    return render(request, 'all-best/index.html',{'project':project})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    project = Project.objects.filter(user_id=current_user.id)

    return render(request,"profile.html",{'profile':profile,'project':project})

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
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    ctx = {"form":form}
    return render(request, 'update_profile.html', ctx)

def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})   

def project_details(request, project_id):
    project = Project.objects.get(id=project_id)
    # get project rating
    return render(request, "project_details.html", {"project": project})  

@login_required(login_url='/accounts/login/')
def search_project(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search').lower()
        projects = Project.search_project_name(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'found': message, 'projects': projects})
    else:
        message = 'Not found'
        return render(request, 'search.html', {'danger': message})       