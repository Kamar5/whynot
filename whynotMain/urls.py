from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^efforts/', views.efforts, name='efforts'),
    url(r'^rankings/', views.rankings, name='rankings'),
]