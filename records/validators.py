from datetime import date

from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_date_not_in_future(value: date) -> None:
    """Validator to ensure the date is not in the future."""
    if value > timezone.now().date():
        raise ValidationError("Date can't be in the future.")
