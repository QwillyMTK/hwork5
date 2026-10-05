from datetime import date
from rest_framework.exceptions import ValidationError

def validate_age_from_token(token_data):
    birthdate = token_data.get("birthdate")

    if not birthdate:
        raise ValidationError("Укажите дату рождения, чтобы создать продукт.")

    try:
        birthdate = date.fromisoformat(birthdate)
    except ValueError:
        raise ValidationError("Некорректный формат даты рождения.")

    today = date.today()
    age = today.year - birthdate.year - (
        (today.month, today.day) < (birthdate.month, birthdate.day)
    )

    if age < 18:
        raise ValidationError("Вам должно быть 18 лет, чтобы создать продукт.")
