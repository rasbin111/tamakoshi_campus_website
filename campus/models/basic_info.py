from django.db import models


class CampusInfo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    campus_chief = models.CharField(max_length=250)
    telephone = models.CharField(max_length=15)
    est_date = models.DateField()

    def __str__(self):
        return self.name


