import os
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import FileSystemStorage


class CustomStorage(FileSystemStorage):
    """Custom storage for django_ckeditor_5 images."""

    location = os.path.join(settings.MEDIA_ROOT, "ckeditor_files/")
    base_url = urljoin(settings.DEFAULT_DOMAIN + settings.MEDIA_URL, "ckeditor_files/")

