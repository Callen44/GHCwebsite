import os
import subprocess
from typing import Any
from django.core.management.base import BaseCommand

# this file starts gunicorn and starts nginx
class Command(BaseCommand):
    def handle(self, *args, **options):
        print("boot.py starting")

        #subprocess.run(["gunicorn", "-b", "0.0.0.0:8000" "-w", "4", "GHCwebsite.wsgi:application"])
        #subprocess.run(["nginx"])

        os.system("nginx & gunicorn -w 4 -b 0.0.0.0:8001 GHCwebsite.wsgi:application")
