from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView

class LogoutGetView(LogoutView):
    http_method_names = ['get', 'post']
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
