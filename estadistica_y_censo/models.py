from django.db import models

class Archivos(models.Model):
   nombre_de_archivo = models.CharField(max_length=30)
   fecha_de_subida = models.DateField
   código_de_Área = models.IntegerField
   descripcion = models.CharField(max_length=300)
   #archivo = models.FileField(upload_to='Archivos/')
   def __str__(self):
       return self.nombre_de_archivo

class Registro_de_descarga(models.Model):
   nombre= models.CharField(max_length=30)
   apellido= models.CharField(max_length=30)
   mail_de_contacto= models.EmailField
   razon_de_descarga= models.CharField(max_length=150)
   nombre_de_archivo_que_descargo= models.CharField(max_length=50)
   def __str__(self):
       return self.nombre
   
class Noticia(models.Model):
   fecha_de_subida = models.DateField
   titulo = models.CharField(max_length=30)
   #imagen = models.ImageField(upload_to='gallery', default='gallery/static/images/no-img.jpg')
   parrafo = models.CharField(max_length=1500)
   def __str__(self):
       return self.titulo
    
class Encuestador(models.Model):
   nombre = models.CharField(max_length=30)
   apellido = models.CharField(max_length=30)
   fecha_de_nacimiento = models.DateField
   dni = models.IntegerField
   #foto = models.ImageField(upload_to='gallery', default='gallery/static/images/no-img.jpg')
   habilitacion_ipc = models.BooleanField
   habilitacion_eph = models.BooleanField
   encuestas_fuera_de_lo_habitual = models.CharField(max_length=300)
