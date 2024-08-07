from django.test import TestCase
from graphene.test import Client
from device_app.schema import schema
from devices.models import Device


class QueryTestCase(TestCase):
    def setUp(self):
        # Create some test devices here
        self.device1 = Device.objects.create(name='Device 1')
        self.device2 = Device.objects.create(name='Device 2')

    def test_all_devices_query(self):
        client = Client(schema)
        executed = client.execute('''{ allDevices { name } }''')
        self.assertEqual(len(executed['data']['allDevices']), 2)

    def test_device_by_name_query(self):
        client = Client(schema)
        executed = client.execute('''{ deviceByName(name: "Device 1") { name id } }''')
        self.assertEqual(executed['data']['deviceByName']['name'], self.device1.name)
        self.assertEqual(int(executed['data']['deviceByName']['id']), self.device1.pk)