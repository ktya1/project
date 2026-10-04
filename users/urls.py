
from django.urls import path
from django.conf.urls.static import static

from config import settings
from users.views import (
    login_view, 
    logout_view, 
    profile_view, 
    register_view,
    profile_edit

    )


urlpatterns = [
    path('users/login/', login_view, name='users-login'),
    path('users/register/', register_view,  name='users-register'),
    path('users/profile/', profile_view,  name='users-profile'),
    path('users/logout/', logout_view, name='users-logout'),
    path('users/edit/', profile_edit, name='users-profile-edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)