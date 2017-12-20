
from django.conf.urls import include, url
from django.contrib import admin
from blog import views as blog_views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^signup/$', blog_views.signup, name='signup'),
    url(r'^login/$', auth_views.login,  name='login'),
    url(r'^logout/$', auth_views.logout,  name='logout'),
]
