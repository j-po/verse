from django.db import models
from django.contrib.auth.models import User

class Request(models.Model):
    src = models.ForeignKey(User, related_name='sent')
    dest = models.ForeignKey(User, related_name='received')
    parent = models.ForeignKey('self', related_name='children',
                               related_query_name='child')
    body = models.TextField()
