from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from users.views import signup, UsersViewSet, me

app_name = 'users'

router = routers.DefaultRouter()
administrate = routers.DefaultRouter()

administrate.register(r'', UsersViewSet, basename='users')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/signup/', signup, name='signup'),
    path('users/me', me, name='me'),
    path('administrate/', include(administrate.urls)),
    path('users/', include('djoser.urls.jwt')),
]
