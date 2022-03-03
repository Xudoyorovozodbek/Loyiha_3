from django.urls import path
from .views import *

app_name = 'App'

urlpatterns = [
    path('index/', FoydalanuvchiListAPIView.as_view(), name='fio-index'),
    path('create/', FoydalanuvchiCreateAPIView.as_view(), name='fio-create'),
    path('update/<int:pk>/', FoydalanuvchiUpdateAPIView.as_view(), name='fio-update'),
    path('delete/<int:pk>/', FoydalanuvchiDeleteAPIView.as_view(), name='fio-delete'),

    path('mix/<int:pk>/', Mix.as_view(), name='fio-mix'),
    path('mixes/<int:pk>/', Mixes.as_view(), name='fio-mixs'),

]
