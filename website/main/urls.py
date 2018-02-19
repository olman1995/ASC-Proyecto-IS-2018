from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^login',views.login, name='login'),
    url(r'^medico',views.medico, name='medico'),
    url(r'^$',views.index, name='index'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)