from django.utils import timezone
from datetime import timedelta


def default_expiry_date():
    now = timezone.now()
    return now + timedelta(days=15)
