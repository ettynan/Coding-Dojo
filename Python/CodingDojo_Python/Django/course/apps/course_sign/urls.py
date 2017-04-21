from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.create_course),
    url(r'^courses$', views.show_course),
    url(r'^remove/(?P<id>\d+)$', views.delete) #make sure the parenthases is AFTER the plus - it was cutting off the parameter
]