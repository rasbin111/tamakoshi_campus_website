from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
# from libs.constants import LEVEL_CHOICES


from utils.default_expiry_date import default_expiry_date
from libs.validators import PHONE_REGEX
from utils.year import current_year, year_choices, year_choices_value, current_year_value


class CampusInfo(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250, null=True)
    campus_chief = models.CharField(max_length=250, null=True)
    telephone = models.CharField(max_length=15, validators=[
                                 PHONE_REGEX], null=True)
    est_date = models.DateField()

    def __str__(self):
        return self.name


class CampusChiefInfo(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/campus_chief/')
    message = models.TextField()
    address = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(
        max_length=150, null=True, blank=True, validators=[PHONE_REGEX])
    education = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class StaffInfo(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='images/staffs/')
    address = models.CharField(max_length=250, null=True, blank=True)
    phone_number = models.CharField(
        max_length=150, null=True, blank=True, validators=[PHONE_REGEX])
    education = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


class Facility(models.Model):

    class Meta:
        verbose_name_plural = "Facilities"

    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to='images/facilities/')

    def __str__(self) -> str:
        return self.title


class Testimonial(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000)
    level = models.CharField(max_length=15)
    year = models.PositiveIntegerField(choices=year_choices_value,
                                       validators=[MinValueValidator(1950),
                                                   MaxValueValidator(current_year)],
                                       default=current_year_value
                                       )

    def __str__(self) -> str:
        return self.name


class Programme(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    admission_start_date = models.DateField(default=timezone.now)
    admission_deadline = models.DateField(
        default=default_expiry_date)
    image = models.ImageField(
        upload_to="images/programmes/", blank=True,  null=True)
    # level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='0')

    def __str__(self):
        return self.title

# class AdmissionDetails(models.Model):
    # pass
