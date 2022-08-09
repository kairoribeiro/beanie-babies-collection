from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('babies/', views.babies_index, name='babies_index'),
    path('babies/<int:baby_id>/', views.babies_detail, name='babies_detail'),
    path('babies/create/', views.BabyCreate.as_view(), name='babies_create'),
    path('babies/<int:pk>/update/', views.BabyUpdate.as_view(), name='babies_update'),
    path('babies/<int:pk>/delete/', views.BabyDelete.as_view(), name='babies_delete'),
    path('accounts/signup/', views.signup, name='signup')
]
