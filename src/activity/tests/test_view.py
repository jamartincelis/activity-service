from django.test import TestCase, Client
from rest_framework import status
from activity.models import Activity
from json import dumps
import activity.tests.constants as constants
from django.urls import reverse
from django.urls.exceptions import NoReverseMatch

class ActivityListCase(TestCase):

    client = Client()
    fixtures = constants.FIXTURES_PATH

    def test_activity_list_without_user(self):
        user_id = ''
        project_id = '016fe969-4d2f-43f9-81b4-1bdcebd975e4'
        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse('list_create', args=[user_id, project_id]))

    def test_activity_list_without_project(self):
        user_id = 'b9e605ee-4cca-400e-99c5-ae24abca97d5'
        project_id = ''
        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse('list_create', args=[user_id, project_id]))

    def test_activity_list_with_valid_data(self):
        user_id = 'b9e605ee-4cca-400e-99c5-ae24abca97d5'
        project_id= '016fe969-4d2f-43f9-81b4-1bdcebd975e4'
        activities = Activity.objects.filter(user=user_id, project=project_id)
        response = self.client.get(reverse('list_create', args=[user_id, project_id]))
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), activities.count())

class PaymentCreateCase(TestCase):

    client = Client()
    fixtures = constants.FIXTURES_PATH

    def test_create_activity(self):
        user_id = 'b9e605ee-4cca-400e-99c5-ae24abca97d5'
        project_id= '016fe969-4d2f-43f9-81b4-1bdcebd975e4'
        payload = {
            "rule": "6e10b138-9899-43cf-8a62-d6119456aa82",
            "payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e",
            "project_name": "Meta de prueba",
            "amount" : 1000,
            "title": "Title",
            "message": "Message",
            "footer": "Footer",
            "rule_name": "Rule Name",
            "rule_icon": "Icon"            
        }
        response = self.client.post(
            reverse('list_create', args=[user_id, project_id]),
            data=dumps(payload),
            content_type=constants.CONTENT_TYPE            
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityDetailCase(TestCase):
    client = Client()
    fixtures = constants.FIXTURES_PATH

    def test_activity_detail(self):
        response = self.client.get(
            reverse('detail', args=[constants.USER_ID, constants.PROJECT_ID, constants.ACTIVITY_ID])
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_activity(self):
        payload = {
            "rule_name": "Rule Name PATCH"
        }
        response = self.client.patch(
            reverse('detail', args=[constants.USER_ID, constants.PROJECT_ID, constants.ACTIVITY_ID]),
            data=dumps(payload),
            content_type=constants.CONTENT_TYPE            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_activity(self):
        payload = {
            "user": "b9e605ee-4cca-400e-99c5-ae24abca97d5",
            "project": "016fe969-4d2f-43f9-81b4-1bdcebd975e4",
            "rule": "6e10b138-9899-43cf-8a62-d6119456aa82",
            "payment": "edf6a8f3-3081-414e-9b2f-4b6fa32eba2e",
            "amount" : 10000,
            "title": "Title Put",
            "message": "Message Put",
            "footer": "Footer Put"
        }
        response = self.client.put(
            reverse('detail', args=[constants.USER_ID, constants.PROJECT_ID, constants.ACTIVITY_ID]),
            data=dumps(payload),
            content_type=constants.CONTENT_TYPE            
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)