from django.conf.urls import url
from Stores import views


urlpatterns = [
    url(r'^$', views.stores_list),
    url(r'^(?P<pk>[0-9]+)', views.stores_id),
]

