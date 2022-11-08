from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages
from django.conf import settings
import base64
from .models import *
from .encryption import *

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        return redirect('index')

    return render(request, 'auth/auth.html')


@require_http_methods(["POST"])
def registerView(request):
    # Only allows post requests
    username = request.POST['username'].lower()
    password = request.POST['password']
    email = request.POST['email'].lower()
    hint = request.POST['hint']

    if hint == password:
        messages.error(
            request, 'Password and password hint can\'t be the same.')
        return redirect('index')

    try:
        user = User.objects.create_user(username, email, password)
        user.hint = encrpyt(hint)
        user.save()

    except IntegrityError:  # If another user already exists with the given email or username it triggers this error
        messages.error(request, 'Error: Username / Email already exists.')
        return redirect('auth')

    login(request, user)
    return redirect('index')


@require_http_methods(["POST"])
def loginView(request):
    # Only allows post requests
    password = request.POST['password']
    email = request.POST['email']

    # Tries to authenticate the user
    user = authenticate(request, username=email, password=password)
    if user != None:
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, 'Error: Could not find user.')
        return redirect('auth')


@login_required(login_url='login')
def logoutView(request):
    logout(request)
    return redirect('auth')


def gethint(request):
    if request.POST:
        try:
            print(request.POST)
            email = request.POST['email'].lower()
            username = request.POST['username'].lower()
            user = User.objects.get(email=email, username=username)
        except:
            return render(request, 'auth/gethint.html', {'err': 'Could not find a user with such email / username.'})

        try:
            decrypted_hint = decrypt(user.hint)
            context = {
                'hint': decrypted_hint
            }
            return render(request, 'auth/gethint.html', {'hint': decrypted_hint})
        except:
            return render(request, 'auth/gethint.html', {'err': 'An error occured while trying to decrypt your password.'})

    return render(request, 'auth/gethint.html')
