# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/posts/', include('post.urls')),
    path('api/study-programs/', include('sprogram.urls')),
    path('api/header-contents/', include('headerpost.urls')),
    path('api/forums/', include('forum.urls')),
    path('api/announcements/', include('announcement.urls')),
    path('accounts/', include('django.contrib.auth.urls')), # Rute Login/Logout
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)