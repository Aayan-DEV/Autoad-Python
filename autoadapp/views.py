from django.shortcuts import render, redirect
from django.contrib import messages
import requests
from requests.exceptions import ConnectionError

def index(request):
    if request.method == 'POST':
        token = request.POST.get('input_text')
        if token:
            try:
                response = requests.post('http://167.71.43.73:8000/start', json={'token': token})
                if response.status_code == 200:
                    messages.success(request, 'Bot is starting!')
                else:
                    messages.error(request, 'Failed to start bot: ' + response.text)
            except ConnectionError as e:
                messages.error(request, 'Failed to connect to the bot server: {}'.format(e))
        else:
            messages.error(request, 'No token provided!')
        return redirect('index')
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def pricing(request):
    return render(request, 'pricing.html')

def privicypolicy(request):
    return render(request, 'privicypolicy.html')

def terms(request):
    return render(request, 'terms.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')
