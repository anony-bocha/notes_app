from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django built-in authentication URLs (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Include your notes app URLs with namespace 'notes'
    path('', include('notes.urls', namespace='notes')),
]
