from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from app2.forms import SendForm
from .models import Send


def blog(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
        else:
            return HttpResponse("error occured")

    else:
        formi = SendForm()
        items = Send.objects.all()
        count = Send.objects.all().count
        return render(request, 'blog.html', {'formj': formi, 'items': items, 'count': count})