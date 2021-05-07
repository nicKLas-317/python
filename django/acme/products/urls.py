from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('test/', views.testController, name='test'),
    path('', views.listProducts, name='listProducts'),
    path('<int:id>/', views.showProduct, name='showProduct'),
    path('noProduct', views.noProduct, name='noProduct'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)