from rest_framework import viewsets

from .models import recomendacion, Preguntas
from .serializer import RecomendacionSerializer, PreguntasSerializer


class recomendacionViewSet(viewsets.ModelViewSet):
    queryset = recomendacion.objects.all()
    serializer_class = RecomendacionSerializer

class PreguntasViewSet(viewsets.ModelViewSet):
    queryset = Preguntas.objects.all()
    serializer_class = PreguntasSerializer