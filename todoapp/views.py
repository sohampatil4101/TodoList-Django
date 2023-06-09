from django.shortcuts import render, redirect
from todoapp.models import Contact
from todoapp.models import Task
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from datetime import datetime


# Create your views here.




def home(request):
    return render(request, 'home.html')



def about(request):
        
    return render(request, 'about.html')



def contact(request):
    
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']

        if (len(name) or len(email) or len(phone) or len(desc)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}


        else:
            ins = Contact(name = name, email= email, phone = phone, desc = desc)
            ins.save()
            context = {'success': True}



    return render(request, 'contact.html', context)




def loginuser(request):
    context = {'success': False, 'successs':False}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        request.session['username'] = username
        user = authenticate(username= username, password = password)

        if (User.objects.filter(username= request.session.get('username')).exists()):
            login(request, user)
            return redirect("/logged")
            context = {'successs':False}


        else:
            context= {'success':True, 'soham':"Please enter correct username or password!!!"}
            return render(request, 'login.html', context)



    return render(request, 'login.html', context)
    
def logged(request):
    return render(request, "todo.html")


def todo(request):
    context = {'successs':False}
    if request.method == "POST":
        task = request.POST['task']
        description = request.POST['description']
        if len(task) == 0:
            context = {'err' : "Please enter task name", 'successs': True}
            return render(request, 'todo.html', context)
        else:
            ins = Task(name =  request.session.get('username'), task = task, description = description, date=datetime.today())
            ins.save()
    return render(request, 'todo.html')
    logout(request)
    try:
        del request.session['username']
    except KeyError:
        pass
    return redirect('/')




def register(request):
    
    context = {'success': False, 'successs':False, 'mssg':""}
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if ( len(username) or len(email) or len(password1)) == 0:
            context={'successs':True,'mssg':"Please enter every field!!"}

        elif (password1 != password2 ):
            context={'successs':True,'mssg':"Both passwords are not same!!"}

        elif (User.objects.filter(username=username).exists() ):
            context={'successs':True,'mssg':"Username exists!!"}
            

        elif ( User.objects.filter(email=email).exists() ):
            context={'successs':True,'mssg':"Email exists!!"}

        else:
            ins = User.objects.create_user(username = username, email = email, password = password1)
            ins.save()
            context = {'success': True}

    return render(request, 'register.html', context)




def todolist(request):
    # search
    if request == "GET":
        namee = request.GET['namee']
        va = Task.objects.filter(name= request.session.get('username'))
        context = {'va':va,'namee':namee}            
        return render(request, 'todolist2.html', context)

    va = Task.objects.filter(name= request.session.get('username'))
    context = {'va':va}
    return render(request, 'todolist.html', context)



def todolist2(request):
    namee = request.GET['namee']
    va = Task.objects.filter(name= request.session.get('username'), task=namee)
    context = {'va':va,'namee':namee}
    return render(request, 'todolist2.html', context)


def delete(request, task):
    ent = Task.objects.get(task = task)
    ent.delete()
    return redirect("/todolist")


