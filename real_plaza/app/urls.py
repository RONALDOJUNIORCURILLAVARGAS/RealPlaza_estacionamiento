from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',views.HomeView.as_view(),name='home'),
    #path('reserve/',include('reserve.urls',namespace='reserve')),
    path('',include('reserve.urls')),
    path('accounts/',include('django.contrib.auth.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)