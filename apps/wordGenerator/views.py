import random
import string
from django.shortcuts import render, redirect

def random_word(n):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

def index(request):
    try:
        request.session['attempts']
    except KeyError:
        request.session['attempts'] = 0

    return render(request, "wordGenerator/index.html")

def generate(request):
    request.session['attempts'] += 1
    request.session['word'] = random_word(8)
    return redirect('/')

def reset(request):
    del request.session['attempts']
    del request.session['word']
    return redirect('/')
