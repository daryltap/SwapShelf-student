import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "swapshelf.settings")
application = get_wsgi_application()

if os.environ.get("VERCEL"):
    from django.core.management import call_command

    call_command("migrate", interactive=False, verbosity=0)
    call_command("seed", verbosity=0)
