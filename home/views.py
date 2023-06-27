from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.models import User
from datetime import datetime
from .models import MenuList,mainmenu
from home.models import Contact,profile
from home.serializers import menuserializer,submenuserializer
from django.db.models import Count

# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages,auth
from django.contrib.auth import authenticate,login,logout
#last import for flashing messgae
# Create your views here.
def index(request):
    context={
        "variable1":"Aditya",
        "Variable2":"Sinha"
    }
    # messages.success(request,"This is a text message")
    return render(request, 'index.html', context)


def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has beeen submitted.")
    return render(request, 'contact.html')

def register(request):
   if request.method=='POST':
    #    name = request.POST['name']
    #    lastname = request.POST['lastname']
       uname = request.POST['username']
       email = request.POST['email']
       pass1 = request.POST['password']
       pass2 = request.POST['password2']
       
       if pass1 != pass2:
           return HttpResponse("Your Paasword is not same")
       else:
           my_user=User.objects.create_user(uname,email,pass1)
           my_user.save()
           return redirect('login')
    #    return HttpResponse("User has been created succefully")
    


    #    print(uname,email,pass1,pass2)

    #    if pass1==pass2:
    #        if User.objects.filter(email=email).exists():
    #            messages.info(request,'email already exist')
    #            return redirect('register')
    #        elif User.objects.filter(uname=uname).exists():
    #            messages.info(request,'username is already taken!')
    #            return redirect('register')
    #        else:
    #           my_user=User.objects.create_user(uname,email,pass1)
    #           my_user.save()
              
    #         #   user_model = User.objects.get(uname=uname)
    #         #   new_profile = profile.objects.create(user=user_model, id_user=user_model.id)
    #         #   new_profile.save()
    #           return redirect('register')
           
    #        return HttpResponse("User has been created succefully")
           
    #    else:
    #     messages.info(request,'password does not match')
    #     return redirect('register')
       
   else:
       return render(request, 'register.html')
   

def Login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username or password is wrong!')
            # return HttpResponse("Username and password are not correct!!!")
    return render(request,'login.html') #this is important line for not geeting value error 
       
def Logout(request):
    logout(request)
    return redirect('login')

def dynamicmenu(request):
 
    try:       
           
        menuList = MenuList.menulist_objects.values('menuname').order_by('MenuType').annotate(Count('menuname'))
        submenuList = MenuList.menulist_objects.all().filter(id__in=[1,2,3,4,5,6,7,8,9,10])
        mainmenu = menuserializer(menuList,many=True)
        data = mainmenu.data
       # print(data)
        request.session['mainM'] = data
 
        submenudata = submenuserializer(submenuList,many=True)
        subdata = submenudata.data
        print(subdata)        
        request.session['submenu'] = subdata
        return render(request, 'base.html', {})  
 
    except Exception as identifier:         
        return render(request, 'base.html', {})  