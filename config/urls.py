from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include([
        path('v1/', include([
            path('drf/', include('rest_framework.urls')),
            path('accounts/', include('apps.accounts.api.v1.urls')),
            path('uploader/', include('apps.uploader.api.v1.urls')),
        ])),
    ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
