from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    n = request.session.get('n', 0) + 1
    request.session['n'] = n
    if n > 4:
        del(request.session['n'])
    resp = HttpResponse('view count=' + str(n) + '  (b8a0cabd)')
    resp.set_cookie('dj4e_cookie', 'b8a0cabd', max_age=1000)
    return resp
