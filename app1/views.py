from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy

from .forms import OgiForm
from .models import Ogi
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


@login_required(login_url=reverse_lazy('login'))
def dashboard(request):
    items = Ogi.objects.all()
    count = Ogi.objects.all().count()
    return render(request, 'dashboard.html', {'items': items, 'count': count})




def chat(request):
        return render(request, 'chat.html')

@login_required(login_url=reverse_lazy('login'))
def add(request):
    if request.method == 'POST':
        form = OgiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add')

    else:
        form = OgiForm()
        return render(request, 'add.html', {'form': form})



@login_required(login_url=reverse_lazy('login'))
# Update Method
def update(request,id):
    item = Ogi.objects.get(pk=id)
    updateForm = OgiForm(instance=item)
    if request.method == 'POST':
        todoAdd = OgiForm(request.POST, instance=item)
        if todoAdd.is_valid():
            todoAdd.save()
            from django.contrib import messages
            messages.success(request, 'Data has been updated.')
            return redirect('dashboard')
        else:
            return redirect('update')
    else:

        return render(request, 'update.html', {'form': updateForm, 'item': item})




@login_required(login_url=reverse_lazy('login'))
def delete(request,id):
    Ogi.objects.filter(id=id).delete()
    return redirect('dashboard')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        from django.contrib import auth


        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html', {'name': username})
        else:
            return render(request, 'register.html')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        from django.contrib.auth.models import User

        user = User.objects.create_user(email=email, password=password, username=username)
        user.save()

        return render(request, 'index.html', {'user': username})
    else:
        return render(request, 'register.html')


def logout(request):
    auth.logout(request)

    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

