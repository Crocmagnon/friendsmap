from django.conf import settings


def app_settings(request):
    """
    A context processor with all APP settings.
    """
    return {
        'app': settings.APP,
    }
