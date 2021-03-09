from rest_framework import routers

from .viewsets import recomendacionViewSet, PreguntasViewSet


router = routers.SimpleRouter() 
router.register('recomendacion',recomendacionViewSet) 
router.register(r'Preguntas',PreguntasViewSet) 

urlpatterns = router.urls