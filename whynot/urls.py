from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', include('whynotMain.urls')),
]