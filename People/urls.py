from django.conf.urls import url
from People import views


urlpatterns = [
    url(r'^reg$', views.register),
]

