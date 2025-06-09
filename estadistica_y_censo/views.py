from django.shortcuts import render

def Home(request):
   
   return render(request, 'index.html')

#institucional
def Institucional(request):
   return render(request, 'institucional.html')

def Organigrama(request):
   return render(request, 'organigrama.html')

def Autoridades(request):
   return render(request, 'autoridades.html')

def Mision_y_vision(request):
   return render(request, 'mision-y-vision.html')

def Marco_legal(request):
   return render(request, 'leyes.html')

#definiciones
def Biblioteca(request):
   return render(request, 'biblioteca.html')
def Definicion_palabras(request):
   return render(request, 'definicion-palabras.html')

#estadisticas
def Anuarios(request):
   return render(request, 'anuarios.html')

def Indicadores(request):
    return render(request, 'indicadores.html')

def Publicaciones(request):
   return render(request, 'publicaciones.html')
def IPC(request):
   return render(request, 'ipc.html')
def EPH(request):
   return render(request, 'eph.html')   

def Producto_bruto(request):
   return render(request, 'producto-bruto-geográfico.html')

#encuestadores
def Encuestadores(request):
   # Aquí puedes agregar la lógica para obtener los encuestadores
   return render(request, 'encuestadores.html')
def validacionEncuestador(request):
   # Aquí puedes agregar la lógica para validar el encuestador
   return render(request, 'validacionEncuestador.html')
def Encuestador(request):
   # Aquí puedes agregar la lógica para obtener el encuestador específico
   # por ejemplo, usando el DNI del encuestador en la URL
   return render(request, 'encuestador.html')
def Materiales(request):
   # Aquí puedes agregar la lógica para obtener los materiales
   return render(request, 'materiales.html')
def Calendario(request):
   return render(request, 'calendario.html')


#territorio
def Mapa_provincial(request):
    return render(request, 'mapa-provincia.html')
def Departamentos(request):
    return render(request,'departamentos.html')   
def Localidades(request):
    return render(request,'localidades.html')   
def Censos(request):
    return render(request,'censos.html')
def Cartografia(request):
    return render(request,'cartografia.html')   






#noticias
def Noticias(request):
   # Aquí puedes agregar la lógica para obtener las noticias
   # por ejemplo, desde una base de datos o un archivo
   return render(request, 'noticias.html')

def Noticia(request):
   # Aquí puedes agregar la lógica para obtener la noticia específica
   # por ejemplo, usando el ID de la noticia en la URL
   return render(request, 'noticia.html')


#donde estamos
def Ubicacion(request):
   return render(request, 'ubicacion.html')