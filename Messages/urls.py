from django.conf.urls import url
from Messages import views


urlpatterns = [
    url(r'^$', views.messages_list),
    url(r'^(?P<pk>[0-9]+)', views.message_user),
]


