from django.db import models

# Create your models here.
class recomendacion(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()


#Modelo preguntas
#Se define este modelo con el fin de almacenar cada una de las preguntas del test.
#Y sus atributos como enunciado, respuestas y tipo
class Preguntas(models.Model):
    NumPreg = models.CharField(max_length=50)
    Mecanica = models.IntegerField()
    Teleccom = models.IntegerField()
    Dibujo = models.IntegerField()
    Diseno = models.IntegerField()
    Fundicion = models.IntegerField()
    Electronica = models.IntegerField()
    Electricidad = models.IntegerField()
    Pregunta = models.TextField()
    Respuesta_Co = models.TextField()
    Tipo = models.TextField()
    Respuestas = models.TextField()