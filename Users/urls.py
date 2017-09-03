from django.conf.urls import url
from Users import views


urlpatterns = [
    url(r'^$', views.users_list),
    url(r'^(?P<pk>[0-9]+)', views.users_id),
    url(r'^nearby', views.users_nearby),
]


