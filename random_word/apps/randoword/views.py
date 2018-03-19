from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# the index function is called when root is visited
def index(request):
    request.session
    if not 'count' in request.session:
        request.session['count'] = 1
    if not 'unique_id' in request.session:
        request.session['unique_id'] = get_random_string(length=14)
    return render(request, 'randoword/index.html')

def generate(request):
    
    request.session['unique_id'] = get_random_string(length=14)
    request.session['count'] += 1
    return redirect('/')