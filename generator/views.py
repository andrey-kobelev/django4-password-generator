from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def params_password(request):
    return render(request, 'generator/params_password.html')


def password(request):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    special = '!@#$%^*()_+=-'
    numbers = '1234567890'

    characters = list(chars)
    length = int(request.GET.get('length', 12))
    the_password = ''

    if request.GET.get('uppercase'):
        characters.extend(chars.upper())

    if request.GET.get('special'):
        characters.extend(special)

    if request.GET.get('numbers'):
        characters.extend(numbers)

    for i in range(length):
        the_password += random.choice(characters)

    context = {
        'password': the_password,
    }
    return render(request, 'generator/password.html', context)
