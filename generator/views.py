from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request,'generator\home.html',)

def password(request):
    all_small_char=list('abcdefghijklmnopqrstuvwxyz')
    #getting length
    length=int(request.GET.get('length',12))
    #getting Uppercase
    if request.GET.get('uppercase'):
        all_small_char.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    #Special
    if request.GET.get('special'):
        all_small_char.extend('!@#$%^&*')
    #number
    if request.GET.get('numbers'):
        all_small_char.extend('1234567890')

    gen_pass=''
    for x in range(length):
        gen_pass += random.choice(all_small_char)
    return render(request,'generator\password.html',{'pass':gen_pass})
