from django.shortcuts import render, redirect, HttpResponse
from . models import Email, EmailManager
from django.contrib import messages

# Create your views here.

def index(request):
    print 'a'
    context = {
        'emails': Email.objects.all()
    }
    return render(request, 'email_app/index.html', context)

def process(request):
    print 'in process', request.POST
    postData = request.POST['email']
   
    valid, errors = Email.objects.validate_email(postData) #getting back a tupple. either true and object or false and error list
    
    if valid: #tupple unpacking
        print "woot!", errors
        return redirect('/success')
        #flash all the errors
    else:
        for error in errors:
            print error
            messages.error(request, error)
        return redirect('/')

def success(request):
    print 'c'
    context = {
        'emails': Email.objects.all()
    }
    return render(request, 'email_app/success.html', context)

def remove(request, id):
    print 'd'
    if request.method == "POST":
        Email.objects.filter(id=id).delete()
    return redirect('/')