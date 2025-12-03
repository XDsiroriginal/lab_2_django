import re
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

def validate_cyrillic_and_spaces(value):
    if not re.fullmatch(r'^[А-Яа-яЁё\s-]+$', value):
        raise ValidationError(
            'Поле должно содержать только кириллические буквы, пробелы и дефисы.'
        )

from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_image(value): # Исправлено название функции (iamge -> image)
    max_size_in_bytes = 2 * 1024 * 1024
    extension_validator = FileExtensionValidator(allowed_extensions=('jpg', 'jpeg', 'png', 'bmp'))
    try:
        extension_validator(value)
    except ValidationError:
        raise ValidationError(
            'Ваш формат не подходит, загружать можно файлы "jpg", "jpeg", "png", "bmp".'
        )

    if value.size > max_size_in_bytes:
        raise ValidationError(
            'Ваш файл превышает размер 2 мегабайта'
        )