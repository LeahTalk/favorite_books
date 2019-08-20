from __future__ import unicode_literals
from django.db import models
from apps.login_app.models import Users

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 1:
            errors['title'] = "The book must have a title!"
        if len(postData['desc']) < 5:
            errors['description'] = 'The description must be at least 5 characters!'
        return errors

class Books(models.Model):
    title = models.CharField(max_length = 255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(Users, related_name = 'books')
    users = models.ManyToManyField(Users, related_name = 'favorites')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()