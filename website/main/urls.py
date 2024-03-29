from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^login',views.login, name='login'),
    url(r'^cargar_imagen',views.cargar_imagen, name='cargar_imagen'),
    url(r'^cargar_paciente',views.cargar_paciente, name='cargar_paciente'),
    url(r'^principal',views.principal, name='principal'),
    url(r'^cargar_muestra',views.cargar_muestra, name='cargar_muestra'),
    url(r'^resultado',views.resultado, name='resultado'),
    url(r'^ver_pacientes',views.ver_pacientes, name='ver_pacientes'),
    url(r'^',views.index, name='index'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)