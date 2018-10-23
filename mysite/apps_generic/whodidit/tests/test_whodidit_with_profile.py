from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.entities.models import Profile
from project.defs import ProfileRole
from utils.helpers_for_tests import create_user, dump


class ProfileListCreateAPITest(TestCase):

    def setUp(self):
        self.c = APIClient()
        self.admin = create_user('admin@staff')
        Profile.grant_user_role(ProfileRole.role_global_admin, self.admin)

    def test_create_outside_of_request(self):
        profile = Profile.objects.create(name="Profile")

        # created_on / updated_on should be set
        self.assertIsNotNone(profile.created_on)
        self.assertIsNotNone(profile.updated_on)
        self.assertGreater(profile.updated_on, profile.created_on)

    def test_create_outside_of_request_with_forced_user(self):
        profile = Profile.objects.create(
            name="Profile",
            created_by=self.admin,
            updated_by=self.admin
        )

        # created_on / updated_on should be set
        self.assertIsNotNone(profile.created_on)
        self.assertIsNotNone(profile.updated_on)
        self.assertGreater(profile.updated_on, profile.created_on)

        # admin should be set as author of changes
        self.assertEqual(profile.created_by, self.admin)
        self.assertEqual(profile.updated_by, self.admin)

    def test_create_in_request(self):
        self.c.login(username=self.admin.username, password='111')

        response = self.c.post(
            '/api/profile/',
            data={
                'name': "Test Profile 02"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        profile = Profile.objects.latest('id')

        # created_on / updated_on should be set
        self.assertIsNotNone(profile.created_on)
        self.assertIsNotNone(profile.updated_on)
        self.assertGreater(profile.updated_on, profile.created_on)

        # admin should be set as author of changes
        self.assertEqual(profile.created_by, self.admin)
        self.assertEqual(profile.updated_by, self.admin)