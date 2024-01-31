from django.urls import path, include
from .views import index, register, delete
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .api.viewsets import ConsultaViewSet

router = routers.DefaultRouter()
router.register(r'api_consulta', ConsultaViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('delete/<int:id>', delete, name='delete'),
    path('api_consulta', include(router.urls)),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
