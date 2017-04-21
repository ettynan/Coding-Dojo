from django.shortcuts import render, redirect, HttpResponse
from . models import Course, Description, Comment
import re

# Create your views here.
def index(request):
    print 'a'
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, 'course_sign/index.html', context)

def create_course(request):
    print 'b'
    error=0
    course = Course.objects.create(course_name=request.POST['course_name'])
    course_id=course.id
    Description.objects.create(content=request.POST['description'], course_id = course_id)
    return redirect('/')

def show_course(request):
    print 'c'
    context = {
        'all_courses': Course.objects.all()
    }
    return render(request, '/course_sign/index.html', context)

# del destroy(request, id):
#     print 'e'
#     context = {
#         'course': Course.objects.filter(id=id),
#         'id': id
#     }

def delete(request, id): #id referring to the id in urls.py and the value comes from index.html on the form action
    print 'd'
    if request.method == "POST":
        Course.objects.filter(id=id).delete() #the first id belongs to the Course.objects. The second id is the one being passed through the browser
        Description.objects.filter(id=id).delete()
    return redirect('/')