import unittest
import json
import server

class ServerTest(unittest.TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def tearDown(self):
        pass

    def routing_service_1_recipient(self, p):
        input_data = {"message": "SendHub Rocks", "recipients": ["510-555-5556"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][0]['recipients']) == 1
        assert response_data['routes'][0]['recipients'][0] == "510-555-5556"

    def routing_service_2_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["510-555-5556", "510-555-5555"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 2
        assert response_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][0]['recipients']) == 1
        assert response_data['routes'][1]['ip'] == "10.0.1.2"
        assert len(response_data['routes'][1]['recipients']) == 1


    def routing_service_4_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["510-555-5551", "510-555-5552", 
                                    "510-555-5553", "510-555-5554"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 4
        assert response_data['routes'][0]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][0]['recipients']) == 1
        assert response_data['routes'][1]['ip'] == "10.0.1.2"
        assert len(response_data['routes'][1]['recipients']) == 1
        assert response_data['routes'][2]['ip'] == "10.0.1.3"
        assert len(response_data['routes'][2]['recipients']) == 1
        assert response_data['routes'][3]['ip'] == "10.0.1.4"
        assert len(response_data['routes'][3]['recipients']) == 1

    def routing_service_5_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["510-555-5551", "510-555-5552", 
                                    "510-555-5553", "510-555-5554",
                                    "510-555-5555"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.2.1"
        assert len(response_data['routes'][0]['recipients']) == 5

    def routing_service_10_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["510-555-5551", "510-555-5552", 
                                    "510-555-5553", "510-555-5554",
                                    "510-555-5555", "510-555-5556",
                                    "510-555-5557", "510-555-5558",
                                    "510-555-5559", "510-555-8890"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.3.1"
        assert len(response_data['routes'][0]['recipients']) == 10


    def routing_service_17_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["510-555-5551", "510-555-5552", 
                                    "510-555-5553", "510-555-5554",
                                    "510-555-5555", "510-555-5556",
                                    "510-555-5557", "510-555-5558",
                                    "510-555-5559", "510-555-8890",
                                    "510-555-8891", "510-555-8892",
                                    "510-555-8893", "510-555-8894",
                                    "510-555-8895", "510-555-8896",
                                    "510-555-8897"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 4
        assert response_data['routes'][0]['ip'] == "10.0.3.1"
        assert len(response_data['routes'][0]['recipients']) == 10
        assert response_data['routes'][1]['ip'] == "10.0.2.1"
        assert len(response_data['routes'][1]['recipients']) == 5
        assert response_data['routes'][2]['ip'] == "10.0.1.1"
        assert len(response_data['routes'][2]['recipients']) == 1
        assert response_data['routes'][3]['ip'] == "10.0.1.2"
        assert len(response_data['routes'][3]['recipients']) == 1

    def routing_service_25_recipient(self, p):
        input_data = {"message": "SendHub Rocks", 
                    "recipients": ["510-555-5551", "510-555-5552", 
                                    "510-555-5553", "510-555-5554",
                                    "510-555-5555", "510-555-5556",
                                    "510-555-5557", "510-555-5558",
                                    "510-555-5559", "510-555-8890",
                                    "510-555-8891", "510-555-8892", 
                                    "510-555-8893", "510-555-8894",
                                    "510-555-8895", "510-555-8896",
                                    "510-555-8897", "510-555-8898",
                                    "510-555-8899", "510-555-8900",
                                    "510-555-8901", "510-555-8902", 
                                    "510-555-8903", "510-555-8904",
                                    "510-555-8905"]}
        response = self.app.post(path=p, data=json.dumps(input_data), content_type="application/json")
        response_data = json.loads(response.data)
        assert response.status_code == 200
        assert response_data is not None
        assert len(response_data['routes']) == 1
        assert response_data['routes'][0]['ip'] == "10.0.4.1"
        assert len(response_data['routes'][0]['recipients']) == 25


    def test_greedy_routing_service_1_recipient(self):
        self.routing_service_1_recipient('/greed')

    def test_greedy_routing_service_2_recipient(self):
        self.routing_service_2_recipient('/greed')

    def test_greedy_routing_service_4_recipient(self):
        self.routing_service_4_recipient('/greed')

    def test_greedy_routing_service_5_recipient(self):
        self.routing_service_5_recipient('/greed')

    def test_greedy_routing_service_10_recipient(self):
        self.routing_service_10_recipient('/greed')

    def test_greedy_routing_service_17_recipient(self):
        self.routing_service_17_recipient('/greed')

    def test_greedy_routing_service_25_recipient(self):
        self.routing_service_25_recipient('/greed')

    def test_dynamic_routing_service_1_recipient(self):
        self.routing_service_1_recipient('/dynamic')

    def test_dynamic_routing_service_2_recipient(self):
        self.routing_service_2_recipient('/dynamic')

    def test_dynamic_routing_service_4_recipient(self):
        self.routing_service_4_recipient('/dynamic')

    def test_dynamic_routing_service_5_recipient(self):
        self.routing_service_5_recipient('/dynamic')

    def test_dynamic_routing_service_10_recipient(self):
        self.routing_service_10_recipient('/dynamic')

    def test_dynamic_routing_service_17_recipient(self):
        self.routing_service_17_recipient('/dynamic')

    def test_dynamic_routing_service_25_recipient(self):
        self.routing_service_25_recipient('/dynamic')

if __name__ == '__main__':
    unittest.main()
