from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Quote
from django.template import loader
from django.urls import reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    latest_quotes_list = Quote.objects.all()
    print(latest_quotes_list)
    template = loader.get_template('quotes/detail.html')
    context = {
        'latest_quotes_list': latest_quotes_list,
    }
    return HttpResponse(template.render(context, request))
@login_required
def add(request):
    if request.method == "GET":
    # functionality 1
        return render(request, 'quotes/add.html', None)

    elif request.method == "POST":
        print(request.POST.get("quote", ""))
        b = Quote(quote_text=request.POST.get("quote", ""), quoter =request.POST.get("quoter", ""), quotee =request.POST.get("quotee", ""))
        b.save()
        return HttpResponseRedirect(reverse('quotes:add', args=None))


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('quotes:add', args=None))
        else:
            template = loader.get_template('registration/signup.html')
            form = UserCreationForm()
            context = {
            'form': form,
            }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('registration/signup.html')
        form = UserCreationForm()
        context = {
        'form': form,
        }
        return HttpResponse(template.render(context, request))
    
