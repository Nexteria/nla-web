from django.conf import settings


def exponea(_):
    return {
        'exponea_token': settings.EXPONEA_TOKEN,
        'exponea_target': settings.EXPONEA_TARGET,
    }
