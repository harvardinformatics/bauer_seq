from django.test import TestCase
from .models import Run, Instrument
from datetime import datetime, timedelta
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

class RunModelTestCase(TestCase):
    """Test for Run model"""
    def setUp(self):
        instrument = Instrument.objects.create(name = 'test', type = 'hiseq')
        self.data = {
                'name': 'test',
                'flowcell': 'test',
                'lot': 'test',
                'expiration': datetime.today() + timedelta(days=365),
                'instrument_id': instrument
        }
        self.run = Run(**self.data)

    def test_run_model(self):
        count = Run.objects.count()
        self.run.save()
        new_count = Run.objects.count()
        self.assertNotEqual(count, new_count)

class RunCreateTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        instrument = Instrument.objects.create(name = 'test', type = 'hiseq')
        self.data = {
                'name': 'test',
                'flowcell': 'test',
                'lot': 'test',
                'expiration': (datetime.today() +
                    timedelta(days=365)).strftime('%Y-%m-%d'),
                'instrument_id': instrument.id
        }
        self.response = self.client.post(
                reverse('create'),
                self.data,
                format='json')
        print(self.response.content)
    def test_api_create_run(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
