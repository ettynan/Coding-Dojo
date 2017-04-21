from django.shortcuts import render, redirect, HttpResponse
from . models import User
from django.contrib import messages

# Create your views here.

def index(request):
    print 'a'
    context = {
        'users': User.objects.all()
    }
    return render(request, 'login_app/index.html', context)

def process(request):
    print 'b', request.POST

    valid, errors, info = User.objects.validate_user(request.POST)

    if valid: #if they have followed all the rules and it validates, it will allow them forward
        print valid, errors
        request.session['first_name'] = errors['first_name']
        return redirect('/success')
    else: #if they have any validation errors they cannot move forward
        for error in errors:
            messages.error(request, error, info)
        return redirect('/')

def success(request):
    print 'c'
    if not request.session.get['first_name']:
        messages.error(request, 'You must be logged in first!')
        return redirect('login:index')
    messages.success(request, "You have logged in successfully")
    context = {
        'users': User.objects.all()
    }
    return render(request, 'login_app/success.html', context)

# def login(request):
#     print 'c'
#     context = {
#         'users': User.objects.all()
#     }
#     return render(request, 'login_app/success.html', context)

def remove(request, id):
    print 'd'
    if request.method == "POST":
        User.objects.filter(id=id).delete()
    return redirect('/')
