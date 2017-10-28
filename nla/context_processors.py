from django.conf import settings


def insert_config(_):
    return {
        'settings': settings.SETTINGS_IN_VIEWS,
    }
