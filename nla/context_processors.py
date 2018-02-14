from django.conf import settings


def insert_config(_):
    return {
        'settings': {
            'exponea_token': settings.EXPONEA_TOKEN,
            'exponea_target': settings.EXPONEA_TARGET,
            'registration_email': settings.REGISTRATION_PERSON_EMAIL,
            'registration_name': settings.REGISTRATION_PERSON_NAME,
            'registration_phone': settings.REGISTRATION_PERSON_PHONE,
            'registration_year': settings.REGISTRATION_YEAR,
        },
    }
