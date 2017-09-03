
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^categories/', include('Facilities.urls')),
    url(r'^stores/', include('Stores.urls')),
    url(r'^users/', include('Users.urls')),
    url(r'^complaints/', include('Complaints.urls')),
    url(r'^messages/', include('Messages.urls')),
    #url(r'^people/', include('People.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
