"""
WSGI config for startproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'startproject.settings') # os환경의 메소드을 사용하게 된다. 라이브러리 같은 느낌

application = get_wsgi_application()
