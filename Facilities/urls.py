from django.conf.urls import url
from Facilities import views


urlpatterns = [
    url(r'^facilities$', views.fac_list),
    url(r'^facilities/(?P<pk>[0-9]+)/$', views.fac_id),
    url(r'^facilities/(?P<pk>[0-9]+)/stores', views.fac_stores),
    url(r'^(?P<pk>[0-9]+)/facilities', views.fac_cats),
]



