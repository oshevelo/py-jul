from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from project.defs import MCTPlatform
from utils.helpers_for_tests import dump, create_user, login_user
from unittest import mock


def fake_bundle_info(platform_name):
    if platform_name == MCTPlatform.linux:
        return {
            'url': "/static/mct_install/linux/MetricCollectionTool-1.11.38.deb",
            'size': 102002003,
            'version': "1.11.38"
        }
    elif platform_name == MCTPlatform.mac:
        return {
            'url': "/static/mct_install/mac/MetricCollectionTool-1.11.38.dmg",
            'size': 110002003,
            'version': "1.11.38"
        }
    elif platform_name == MCTPlatform.windows:
        return {
            'url': "/static/mct_install/windows/MetricCollectionTool-1.11.38.exe",
            'size': 72002003,
            'version': "1.11.38"
        }


def fake_bundle_info_no_windows(platform_name):
    if platform_name == MCTPlatform.linux:
        return {
            'url': "/static/mct_install/linux/MetricCollectionTool-1.11.38.deb",
            'size': 102002003,
            'version': "1.11.38"
        }
    elif platform_name == MCTPlatform.mac:
        return {
            'url': "/static/mct_install/mac/MetricCollectionTool-1.11.38.dmg",
            'size': 110002003,
            'version': "1.11.38"
        }


class MCTInstallAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        self.user = create_user('user@staff')

    @mock.patch('apps.info.mct_install.bundle_info', side_effect=fake_bundle_info)
    def test_install(self, fake_bundle_info):
        login_user(self.c, self.user)

        response = self.c.get('/api/info/mct-install/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'windows': {
                'url': "/static/mct_install/windows/MetricCollectionTool-1.11.38.exe",
                'size': 72002003,
                'version': "1.11.38"
            },
            'mac': {
                'url': "/static/mct_install/mac/MetricCollectionTool-1.11.38.dmg",
                'size': 110002003,
                'version': "1.11.38"
            },
            'linux': {
                'url': "/static/mct_install/linux/MetricCollectionTool-1.11.38.deb",
                'size': 102002003,
                'version': "1.11.38"
            }
        })

    @mock.patch('apps.info.mct_install.bundle_info', side_effect=fake_bundle_info_no_windows)
    def test_missing_bundle(self, fake_bundle_info_no_windows):
        login_user(self.c, self.user)

        response = self.c.get('/api/info/mct-install/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'windows': None,
            'mac': {
                'url': "/static/mct_install/mac/MetricCollectionTool-1.11.38.dmg",
                'size': 110002003,
                'version': "1.11.38"
            },
            'linux': {
                'url': "/static/mct_install/linux/MetricCollectionTool-1.11.38.deb",
                'size': 102002003,
                'version': "1.11.38"
            }
        })
