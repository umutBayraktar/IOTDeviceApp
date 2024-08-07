from django.test import TestCase
from graphene.test import Client
from device_app.schema import schema
from devices.models import Device
from locations.models import Location


class QueryTestCase(TestCase):
    def setUp(self):
        # Create some test devices and locations here
        self.device1 = Device.objects.create(name='Device 1')
        self.device2 = Device.objects.create(name='Device 2')
        self.location1 = Location.objects.create(device=self.device1, latitude=1.0, longitude=1.0, timestamp=1)
        self.location2 = Location.objects.create(device=self.device2, latitude=2.0, longitude=2.0, timestamp=2)

    def test_location_history_by_device_query(self):
        client = Client(schema)
        executed = client.execute('''{ locationHistoryByDevice(deviceName: "Device 1") 
        { latitude longitude device { name } } }''')
        self.assertEqual(executed['data']['locationHistoryByDevice'][0]['device']['name'], self.device1.name)
        self.assertEqual(executed['data']['locationHistoryByDevice'][0]['latitude'], self.location1.latitude)
        self.assertEqual(executed['data']['locationHistoryByDevice'][0]['longitude'], self.location1.longitude)

    def test_last_locations_for_all_devices_query(self):
        client = Client(schema)
        executed = client.execute('''{ lastLocationsForAllDevices { latitude longitude device { name } } }''')
        self.assertEqual(len(executed['data']['lastLocationsForAllDevices']), 2)
        self.assertEqual(executed['data']['lastLocationsForAllDevices'][0]['device']['name'], self.device1.name)
        self.assertEqual(executed['data']['lastLocationsForAllDevices'][0]['latitude'], self.location1.latitude)
        self.assertEqual(executed['data']['lastLocationsForAllDevices'][0]['longitude'], self.location1.longitude)
        self.assertEqual(executed['data']['lastLocationsForAllDevices'][1]['device']['name'], self.device2.name)
        self.assertEqual(executed['data']['lastLocationsForAllDevices'][1]['latitude'], self.location2.latitude)
        self.assertEqual(executed['data']['lastLocationsForAllDevices'][1]['longitude'], self.location2.longitude)