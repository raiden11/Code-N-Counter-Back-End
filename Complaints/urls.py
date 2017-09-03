from django.conf.urls import url
from Complaints import views


urlpatterns = [
    url(r'^$', views.complaints_list),
]

