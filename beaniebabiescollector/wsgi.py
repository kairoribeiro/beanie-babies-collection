"""
WSGI config for beaniebabiescollector project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""
# from beaniebabiescollector import MyWSGIApp
import os
from django.conf import settings
from whitenoise import WhiteNoise


from django.core.wsgi import get_wsgi_application


application = get_wsgi_application()
application = WhiteNoise(application, root=settings.STATIC_ROOT)
application.add_files("/staticfiles", prefix="more-files/")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beaniebabiescollector.settings')

