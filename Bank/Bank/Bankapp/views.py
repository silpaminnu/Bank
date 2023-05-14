from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credits")
            return redirect('login')
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']


        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return render(request, "register.html")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return render(request, "register.html")
            else:
                user = User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
                user.save()
                return render(request,"login.html")

        else:
            messages.info(request,"password not matching")
            return render(request,"register.html")
        return render(request,"index.html")


    return render(request , "register.html")
def logout(request):
    auth.logout(request)
    return render(request,"login.html")
def demo(request):
    return render(request,"index.html")
def new(request):
    return render(request,"new.html")
def empty(request):
    return render(request,"empty.html")
def message(request):
    return render(request,"message.html")
from django.shortcuts import render
from django.views.generic import CreateView
from .models import Person
from .forms import PersonCreationForm


class PersonCreateView(CreateView):
    model=Person
    form_class=PersonCreationForm
    template_name="new.html"
    def update(request,id):
        movie= Person.objects.get(id=id)
        form=PersonCreationForm(request.POST or None,request.FILES,instance=movie)
        if form.is_valid():
            form.save()
            messages.info(request, "Application accepted")
            return redirect('new.html')




#
#