from django.http import Http404
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from med_accounts.forms import RegisterForm, LoginForm, UserChangeForm
from med_accounts.models import MyDoctor

# Create your views here.

def medoc(request):
    """ Afficher tous les medecins de notre database """
    mydoctor = MyDoctor.objects.all()
    """Renders the medoc page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'medoc.html',
        {'mydoctors': mydoctor},
        context_instance = RequestContext(request,
        {
            'title':'Registered Docs',
            'message':"Docs registered with us and ready to serve you!",
            'todocs': "Are you doctor and aren't registed yet? Click on the button below!",
            'year':datetime.now().year,
        })
    )


def auth_login(request):
    form = LoginForm(request.POST or None)
    next_url = request.GET.get('next')
    if form.is_valid():
        name = form.cleaned_data['name']
        password = form.cleaned_data['password']
        user = authenticate(name=name, password=password)
        if user is not None:
            login(request, user)
            if next_url is not None:
                return HttpResponseRedirect(next_url)
            return HttpResponseRedirect("/create")
    action_url = reverse("auth_login")
    title = "Login"
    submit_btn = title
    submit_btn_class = "btn-success btn-block"
    context = {
        "form": form,
        "action_url": action_url,
        "title": 'Log in',
        "submit_btn": submit_btn,
        "submit_btn_class": submit_btn_class,
        }
    return render(request, "account_login.html", context)

def auth_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data['name']
        owner_first_name = form.cleaned_data['owner_first_name']
        owner_last_name = form.cleaned_data['owner_last_name']
        country = form.cleaned_data['country']
        specialite = form.cleaned_data['specialite']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password2']
        #MyUser.objects.create_user(name=name, email=email, password=password, country=country, specialite=specialite)
        new_user = MyDoctor()
        new_user.name = name
        new_user.owner_first_name = owner_first_name
        new_user.owner_last_name = owner_last_name
        new_user.email = email
        new_user.country = country
        new_user.specialite = specialite
        #new_user.password = password #WRONG
        new_user.set_password(password) #RIGHT
        new_user.save()

    action_url = reverse("register")
    title = "Register"
    submit_btn = "Create free account"

    context = {
        "form": form,
        "action_url": action_url,
        "title": 'Register now!',
        "submit_btn": submit_btn
        }
    return render(request, "account_register.html", context)