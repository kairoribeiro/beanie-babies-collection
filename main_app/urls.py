from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('babies/', views.babies_index, name='babies_index'),
    path('babies/<int:baby_id>/', views.babies_detail, name='babies_detail'),
    path('babies/create/', views.BabyCreate.as_view(), name='babies_create'),
    path('babies/<int:pk>/update/', views.BabyUpdate.as_view(), name='babies_update'),
    path('babies/<int:pk>/delete/', views.BabyDelete.as_view(), name='babies_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)