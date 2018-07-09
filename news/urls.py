from django.conf.urls import url
import . from views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
]