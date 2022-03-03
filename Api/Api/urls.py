
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('App.urls', namespace='app')),
    path('api-auth/',include('rest_framework.urls')),
    path('app/dj-rest-auth/',include('dj_rest_auth.urls')),
    path('app/dj-rest-auth/registration',include('dj_rest_auth.registration.urls')),
    path('app/allauth/',include('allauth.urls')),
]
