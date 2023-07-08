from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from utils.default_expiry_date import default_expiry_date

class ValidNoticeManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(valid=True)
    
class Notice(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True, null=True)
    description = models.TextField()
    issued_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(default=default_expiry_date)
    image = models.ImageField(upload_to="notices", blank=True, null=True)
    files = models.FileField('files/notices/', blank=True)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    valid = models.BooleanField(default=True)

    objects = models.Manager()
    valid_objects = ValidNoticeManager()


    def __str__(self):
        return self.title
    
    def save(self):
        title_arr = self.title.lower().split(" ")
        title_with_dashes = "-".join(title_arr)
        self.slug = title_with_dashes
        return super().save()

