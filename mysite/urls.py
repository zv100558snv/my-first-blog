from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views
from register.views import RegisterFormView                                            # Регистрация

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    
    url(r'^register/$', RegisterFormView.as_view(), name = "register"),                 # Регистрация
    
    url(r'', include('blog.urls')),
]
