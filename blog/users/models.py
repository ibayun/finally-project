import random
import string
import base64

from django.core.signing import Signer

ALPHABET = string.printable * 70

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    signer = Signer()
