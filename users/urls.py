from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from users.views import signup, SelfInfoViewSet, UsersViewSet

app_name = 'users'

router = routers.DefaultRouter()
administrate = routers.DefaultRouter()

administrate.register(r'', UsersViewSet, basename='users')
router.register(r'', SelfInfoViewSet, basename='me')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/signup/', signup, name='signup'),
    path('users/', include(router.urls)),
    path('administrate/', include(administrate.urls)),
    path('users/', include('djoser.urls.jwt')),
]
