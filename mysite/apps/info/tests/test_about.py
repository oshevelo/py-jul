from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from utils.helpers_for_tests import dump, create_user, login_user
from unittest import mock

#from utils.tz import TZ_UTC


def fake_release_version():
    return '7.0'


def fake_release_date():
    return timezone.datetime(2017, 1, 1)# tzinfo=TZ_UTC)


def fake_build_version():
    return 100500


class AboutAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        self.user = create_user('user@staff')

    @mock.patch('apps.info.api.views.release_metadata.release_version',
                side_effect=fake_release_version)
    @mock.patch('apps.info.api.views.release_metadata.release_date',
                side_effect=fake_release_date)
    @mock.patch('apps.info.api.views.release_metadata.build_version',
                side_effect=fake_build_version)

    def test_about(self, fake_release_version, fake_release_date, fake_build_version):
        login_user(self.c, self.user)

        response = self.c.get('/api/info/about/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
#        dump(response)  

        self.assertEqual(response.data, {
            'release_version': "7.0",
            'release_date': "2017-01-01T00:00:00Z",
            'build_version': 100500,
            'minor_build_version': 1
        })
