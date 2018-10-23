import os

from django.conf import settings

from project.defs import MCTPlatform
from utils.enum_class import enumeration_class_values


INSTALL_DIR = os.path.join(settings.STATIC_ROOT, 'mct_install')

BUNDLE_EXT_DICT = {
    MCTPlatform.linux: 'deb',
    MCTPlatform.mac: 'dmg',
    MCTPlatform.windows: 'exe'
}


def get_file_version(bundle_filename):
    if type(bundle_filename) == str:
        parts0 = bundle_filename.split('-')
        if parts0:
            parts1 = parts0[1].split('.')
            if parts1:
                return '.'.join(parts1[:-1])


def bundle_info(platform_name):
    assert platform_name in enumeration_class_values(MCTPlatform)
    platform_dir = os.path.join(INSTALL_DIR, platform_name)

    bundle_filename = None
    for f in os.listdir(platform_dir):
        parts = f.split('.')
        if parts and parts[-1] == BUNDLE_EXT_DICT[platform_name]:
            bundle_filename = f

    if bundle_filename:
        version = get_file_version(bundle_filename)
        size = os.stat(os.path.join(platform_dir, bundle_filename)).st_size
        url = "{static_url}mct_install/{platform_name}/{filename}".format(
            static_url=settings.STATIC_URL,
            platform_name=platform_name,
            filename=bundle_filename
        )
        return dict(
            url=url,
            version=version,
            size=int(size / (1024 * 1024))
        )
