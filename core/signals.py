from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from unidecode import unidecode

from core import models


