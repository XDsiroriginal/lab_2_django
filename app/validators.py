import re
from django.core.exceptions import ValidationError

def validate_cyrillic_and_spaces(value):
    if not re.fullmatch(r'^[А-Яа-яЁё\s-]+$', value):
        raise ValidationError(
            'Поле должно содержать только кириллические буквы, пробелы и дефисы.'
        )