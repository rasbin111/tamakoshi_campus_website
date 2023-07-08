from django.db import models


def get_upload_path(instance, filename):
    return f"gallery/{instance.gallery.title}/{filename}"


class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_path)
    gallery = models.ForeignKey('Gallery', on_delete=models.CASCADE, related_name='images')


class Report(models.Model):
    title = models.CharField(max_length=250)
    created_by = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    report_image = models.ImageField(null=True, blank=True, upload_to=f'images/reports/{title}/')
    report_file = models.FileField(null=True, blank=True, upload_to=f'files/reports/{title}/')
    file_name = ""

    def __str__(self):
        return self.title


class Gallery(models.Model):

    class Meta:
        verbose_name_plural = 'Galleries'

    title = models.CharField(max_length=250)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    images_list= []
    

    def __str__(self):
        return self.title
