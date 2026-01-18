from http import HTTPStatus

from api import models
from django.test import Client, TestCase

class TaskiApiTestCase(TestCase):
    def SetUp(self):
        self.guest_client - Client()
    
    def self_list_exists(self):
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def self_task_creation(self):
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertEqual(models.Task.objects.filter(title='Test').exists())
