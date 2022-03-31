from django.test import TestCase
from django.urls import reverse
import activity.tests.constants as constants

class TestActivityUrls(TestCase):
    def test_resolution_for_list_create(self):
        url = reverse('list_create', args=[constants.USER_ID, constants.PROJECT_ID])
        self.assertEqual(url, constants.URL_ACTIVITY_LIST_CREATE.format(
            constants.USER_ID, constants.PROJECT_ID))

    def test_resolution_for_detail(self):
        url = reverse('detail', args=[constants.USER_ID, constants.PROJECT_ID, 
            constants.ACTIVITY_ID])
        self.assertEqual(url, constants.URL_ACTIVITY_DETAIL.format(constants.USER_ID, 
            constants.PROJECT_ID, constants.ACTIVITY_ID))