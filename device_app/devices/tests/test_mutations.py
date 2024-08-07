from django.test import TestCase
from graphene.test import Client
from device_app.schema import schema
from devices.models import Device


class MutationTestCase(TestCase):
    def setUp(self):
        # Create a test device here
        self.device1 = Device.objects.create(name='Test Device')

    def test_create_device_mutation(self):
        client = Client(schema)
        executed = client.execute('''
            mutation {
                createDevice(name: "New Device") {
                    device {
                        name
                    }
                }
            }
        ''')
        self.assertEqual(executed['data']['createDevice']['device']['name'], 'New Device')
        self.assertEqual(Device.objects.count(), 2)

    def test_delete_device_mutation(self):
        client = Client(schema)
        executed = client.execute('''
            mutation {
                deleteDevice(name: "Test Device") {
                    ok
                }
            }
        ''')
        self.assertTrue(executed['data']['deleteDevice']['ok'])
        self.assertEqual(Device.objects.count(), 0)