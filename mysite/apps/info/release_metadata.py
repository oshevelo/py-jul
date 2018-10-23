""" Utils to retrieve current version details """
import datetime
import os

from django.conf import settings
from django.utils import timezone


BUILD_INFO_FILE = os.path.join(settings.STATIC_ROOT, 'build.txt')


def release_version():
    return settings.RELEASE_VERSION


def release_date():
    """ Should return date/time the build was created.

        Will be implemented after CI setup.
    """
    if os.path.isfile(BUILD_INFO_FILE):
        return datetime.datetime.fromtimestamp(os.stat(BUILD_INFO_FILE).st_mtime)


def build_version():
    """ Should return build number.

        Will be implemented after CI setup.
    """
    version = None
    if os.path.isfile(BUILD_INFO_FILE):
        with open(BUILD_INFO_FILE, 'r') as fp:
            version = fp.readline()

    return version

