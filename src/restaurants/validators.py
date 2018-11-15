from django.core.exceptions import ValidationError

CATEGORIES = ['food', 'drinks']

def validate_category(value):
    if not value in CATEGORIES:
        raise ValidationError("\"{}\" is not a Valid Category".format(value))
