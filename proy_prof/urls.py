"""
URL configuration for proy_prof project.

The `urlpatterns` list routes URLs to viewsFor more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1Add an import:  from my_app import views
    2Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1Add an import:  from other_app.views import Home
    2Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1Import the include() function: from django.urls import include, path
    2Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from estadistica_y_censo.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

#home
    path('', Home),

#institucional
    path('institucional/', Institucional),
    path('organigrama/', Organigrama),
    path('autoridades/', Autoridades),
    path("mision-y-vision/", Mision_y_vision),
    path("leyes/", Marco_legal),

#definiciones
    path("biblioteca/", Biblioteca),
    path("definicion-palabras/", Definicion_palabras),

#estadisticas
    path("anuarios/", Anuarios),
    path('indicadores/', Indicadores),
    path("publicaciones/", Publicaciones),
    path("ipc/", IPC),
    path("EPH/", EPH),
    path("producto-bruto-geografico/", Producto_bruto),

#encuestadores
    path('encuestadores/', Encuestadores),
    path('encuestador/', Encuestador),
    path('validacionEncuestador/', validacionEncuestador),
    path('materiales/', Materiales),
    path('calendario/', Calendario),

#territorio
    path('mapa-provincial/', Mapa_provincial),
    path('departamentos/', Departamentos),
    path('localidades/', Localidades),
    path('censos/', Censos),
    path('cartografia/', Cartografia),


#noticia
    path('noticias/', Noticias),
    path('noticia/', Noticia),

#ubicacion
    path('ubicacion/', Ubicacion),

]
