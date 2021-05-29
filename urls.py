from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from app.views import *
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/task/$', taskApi),
    url(r'^api/task/([0-9]+)$', taskApi),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)