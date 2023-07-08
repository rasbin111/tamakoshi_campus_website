from django.db import models
from libs.validators import PHONE_REGEX


class ContactInfo(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15, validators=[PHONE_REGEX], null=True)
    address = models.CharField(max_length=250, null=True)
    telephone_number = models.CharField(
        max_length=15, validators=[PHONE_REGEX], null=True)


class Participant(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,
                                    validators=[PHONE_REGEX],
                                    blank=True)

    def __str__(self):
        return self.full_name


class Message(models.Model):
    message = models.TextField(blank=False)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE,
                                    related_name='message', null=True)

    def __str__(self):
        return self.participant.full_name
