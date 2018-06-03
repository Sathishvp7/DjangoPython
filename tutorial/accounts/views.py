from django.shortcuts import render_to_response
from accounts.forms import RegistrationForm
from django.views.generic.edit import UpdateView
from accounts.forms import EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import BlogForm,Userprofileform
from .models import Blogs
from django.http import HttpResponseRedirect
from functools import wraps
from django.middleware.csrf import CsrfViewMiddleware, get_token
from django.utils.decorators import decorator_from_middleware
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
#from .forms import ContactForm, ColorfulContactForm
#from accounts.forms import HomeForm
#from accounts.models import Enter_task


def home(request):
    return render(request, 'accounts/Home.html')
def EnterTask(request):
    return render(request, 'accounts/Enter Task.html')
def login(request):
    return render(request,'accounts/login1.html')
def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/Signuplogin')
    else:
        form=RegistrationForm()
        args={'form': form}
        return render(request,'accounts/reg_form.html',args)
@login_required
def profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)
@login_required
def changepassword_profile(request):
    args={'user':request.user}
    return render(request,'accounts/Changepassword_profile.html',args)
@login_required
def edit_profile(request):
    if request.method=='POST':
        form = EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form=EditProfileForm(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit_profile.html',args)

@login_required
def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/account/Changepassword_profile')

        else:
            return redirect('accounts/change_password')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/change_password.html',args)



def add_blog(request):#Adding New Task
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            #text = form.cleaned_data['fields']
            #form = BlogForm()
            return render(request, 'accounts/popup.html')
    else:
        form = BlogForm()
    args = {'form': form}
    return render(request, 'accounts/blog_form.html', args)


def BlogAll(request):# To View All Task-->View
    return render_to_response('accounts/list.html',{'BlogAll': Blogs.objects.filter(user=request.user)})


def BlogGet(request, blog_id=1):#To View Particular taskg
    return  render_to_response('accounts/list1.html',{'BlogGet':Blogs.objects.get(id=blog_id)})
#def BlogGet(request, blog_id=1):#To View Particular taskg
 #   return  render_to_response('accounts/list1.html',{'BlogGet':Blogs.objects.get(id=request.user)})


def BlogAlls(request): # To View All Task-->Edit
    return render_to_response('accounts/ListEdit.html',{'BlogAlls': Blogs.objects.filter(user=request.user)})


def BlogEdit(request,id=None): # To Edit Particular Task
    instance=get_object_or_404(Blogs,id=id)
    form = BlogForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return render(request, 'accounts/popup.html')
        form = BlogForm()
    args = {
            'form': form,
            'instance': instance,
                }
    return render(request,'accounts/list3.html',args,{'BlogAll': Blogs.objects.all})

def add_userprofile(request):#Adding userprofile
    if request.method == "POST":
        form = Userprofileform(request.POST)
        if form.is_valid():
            blog_item = form.save(commit=False)
            blog_item.save()
            #text = form.cleaned_data['fields']
            #form = BlogForm()
            return render(request, 'accounts/popup.html')
    else:
        form = Userprofileform()
    args = {'form': form}
    return render(request, 'accounts/userprofile_form.html', args)









