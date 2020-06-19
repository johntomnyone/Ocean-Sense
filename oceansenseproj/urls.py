from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from oceansenseweb import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^oceansenseweb/',include('oceansenseweb.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^privacy/$', views.privacy, name='privacy'),
    url('avatar/', include('avatar.urls')),
]


urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
		urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
		urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

