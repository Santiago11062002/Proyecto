from rest_framework import routers
from .api import ProyectoviewSet

router=routers.DefaultRouter()
router.register('api/ApiProyecto',ProyectoviewSet,'ApiProyecto')

urlpatterns = router.urls