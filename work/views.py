from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import Register,Login,GenreForm,MovieForm
from django.contrib.auth.models import User
from work.models import Genre,Movies
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

# Create your views here.

def signin_required(fn):  
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

class RegisterView(View):
    def get(self,request,*args,**kwargs):
        form    =   Register()
        return render(request,"regist.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form    =   Register(request.POST)
        if form.is_valid():
            form.save
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"Added Successfully!")
        form    =   Register()
        return render(request,"regist.html",{"form":form})
    
class SignIn(View):
    def get(self,request,*args,**kwargs):
        form    =   Login()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form    =   Login(request.POST)
        if form.is_valid():
            u_name  =   form.cleaned_data.get("username")
            pwd     =   form.cleaned_data.get("password")
            userobj =   authenticate(request,username=u_name,password=pwd)
            print(userobj)
            
            if userobj:
                print("Valid Cridentials")
                login(request,userobj)
                return redirect("movielist")
            
            else:
                print("Invalid Cridentials")

        return render(request,"login.html",{"form":form})
    
    # ==================================================        G E N R E       =====================================================

    
@method_decorator(signin_required, name="dispatch")
class GenreView(View):
    def get(self,request):
        form= GenreForm()
        return render(request,"genre.html",{"form":form})
    
    def post(self,request):
        form=GenreForm(request.POST,files=request.FILES)
        
        if form.is_valid():
            print(form.cleaned_data)
            Genre.objects.create(**form.cleaned_data)
            messages.success(request,"Genre added successfully")

        else:
            messages.error(request,"Failed to add an Genre")

        return redirect('genrelist')

@method_decorator(signin_required, name="dispatch")
class GenreList(View):
    def get(self,request,*args,**kwargs):
        qs    =   Genre.objects.all()
        return render(request,"Glist.html",{"qs":qs})

    def post(self,request,*args,**kwargs):
        form    =   GenreForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        else:
            print("Get Out")
        
        form    =   GenreForm()
        qs    =   Genre.objects.all()
        return render(request,"Glist.html",{"qs":qs})

@method_decorator(signin_required, name="dispatch")
class GenreDelete(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        qs = Genre.objects.get(id=id).delete()
        return redirect('genrelist')

@method_decorator(signin_required, name="dispatch")
class GenreUpdate(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        obj = Genre.objects.get(id=id)
        form = GenreForm(instance=obj)
        return render(request,"Gupdate.html",{"form":form})
    
    def post(self,request,**kwargs):
        id = kwargs.get("pk")
        obj = Genre.objects.get(id=id)
        form=GenreForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Genre Updated Successfully.")

        else:
            messages.error(request,"Failed to Update Genre.")
            print("Get Out")
        return redirect('genrelist')

    # ==================================================        M O V I E       =====================================================

@method_decorator(signin_required, name="dispatch")
class MovieView(View):
    def get(self,request):
        form= MovieForm()
        return render(request,"Movie.html",{"form":form})
    
    def post(self,request):
        form=MovieForm(request.POST,files=request.FILES)
        
        if form.is_valid():
            print(form.cleaned_data)
            Movies.objects.create(**form.cleaned_data)
            messages.success(request,"Movie added successfully")

        else:
            messages.error(request,"Failed to add an Movie")

        return redirect('movielist')
    
@method_decorator(signin_required, name="dispatch")
class MovieList(View):
    def get(self,request,*args,**kwargs):
        qs    =   Movies.objects.all()
        return render(request,"Mlist.html",{"qs":qs})

    def post(self,request,*args,**kwargs):
        form    =   MovieForm(request.POST)
        
        if form.is_valid():
            form.save()
        
        else:
            print("Get Out")
        
        form    =   MovieForm()
        qs    =   Movies.objects.all()
        return render(request,"Mlist.html",{"qs":qs})

@method_decorator(signin_required, name="dispatch")
class MovieDelete(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        qs = Movies.objects.get(id=id).delete()
        return redirect('movielist')

@method_decorator(signin_required, name="dispatch")
class MovieUpdate(View):
    def get(self,request,**kwargs):
        id = kwargs.get("pk")
        obj = Movies.objects.get(id=id)
        form = MovieForm(instance=obj)
        return render(request,"Mupdate.html",{"form":form})
    
    def post(self,request,**kwargs):
        id = kwargs.get("pk")
        obj = Movies.objects.get(id=id)
        form=MovieForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Movie Updated Successfully.")

        else:
            messages.error(request,"Failed to Update Movie.")
            print("Get Out")
        return redirect('movielist')



class Signout(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")