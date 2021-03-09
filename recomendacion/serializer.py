from .models import recomendacion, Preguntas
from rest_framework import serializers

class RecomendacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = recomendacion
        fields = '__all__'

class PreguntasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = '__all__'

class Post_recomendacion(serializers.Serializer):

    consulta = serializers.CharField()
