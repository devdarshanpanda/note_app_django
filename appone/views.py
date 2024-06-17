from django.shortcuts import render,redirect
from appone.forms import Notes_form,CustomerRegistrationForm,Login_form
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate,login,logout as auth_logout
from appone.models import Note
# Create your views here.
# ===============================
# home
# =================================
def home(request):
    
    return render(request,"index.html")
# ===================================
# add note
# =================================
def add_note(request):
    form=Notes_form()
    return render(request,"index.html",{'form':form})
# ===================================
# save note 
# ===================================
def save_note(request):
    if request.user.is_authenticated:
        user=request.user
        if request.method=="POST":
            form=Notes_form(request.POST)
            if form.is_valid():
                note_title=form.cleaned_data['note_title']
                note_description=form.cleaned_data['note_description']
                Note.objects.create(user=user,note_title=note_title,note_description=note_description)
                return redirect("my_notes")
                
        else:
            messages.error(request,"enter valid data")
    messages.error(request,"pls login")

# ===================================
# sign in
# =================================
class signup(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,"signup.html" ,{"form":form})
    
    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            email=form.cleaned_data['email']
            email=form.cleaned_data['email']
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            data=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password)
            return redirect("/")
        return render(request,"signup.html",{"form":form})
# ===================================
# login
# =================================
def user_login(request):
    if request.method == "POST":
        form=Login_form(request=request,data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=uname,password=password)
            if user is not None:
                print(user)
                login(request,user)
                return redirect("/")
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form=Login_form()
    
    return render(request,"login.html",{'form':form})
# ===================================
# logout
# =================================
def logout(request):
    auth_logout(request)
    return redirect("/")
# ===================================
# my notes
# =================================
def my_notes(request):
    if request.user.is_authenticated:
        user=request.user
        data=Note.objects.filter(user=user)
        return render(request,"mynotes.html",{'data':data})

# ===================================
# edit note 
# ===================================
def edit_notes(request,id):
    note=Note.objects.get(id=id)
    form =Notes_form(instance=note)
    if request.method=="POST":
        form=Notes_form(request.POST,instance=note)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("my_notes")
    return render(request,"edit_note.html",{'form':form})
#  ===================================
# delete_notes 
# ======================================
def delete_notes(request,id):
    note=Note.objects.get(id=id)
    note.delete()
    return redirect("my_notes")

