from django.conf.urls import patterns,url
from shopsys.apps.login import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
)
