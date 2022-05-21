from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import home,SigninView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("signin/", SigninView.as_view(), name="signin"),
    path('accounts/', include('django.contrib.auth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)