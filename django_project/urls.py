from django.conf.urls import include, url
from django.contrib import admin
from jingle.views import hello

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^jingle/',include('jingle.urls')),

]
