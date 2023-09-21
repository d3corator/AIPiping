import unittest
from fastapi.testclient import TestClient
from app import app


class PositiveTest(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_get_data(self):
        info = {
            "country": "India",
            "season": "Summer"
        }

        response = self.client.post("/api/recommend", json=info)
        self.assertEqual(response.status_code, 200)  
        data = response.json()
        self.assertEqual(data["country"], "India") 
        self.assertEqual(data["season"], "Summer")    
        self.assertIsInstance(data["recommendations"], list)  

    def test_invalid_json(self):
        invalid_json = "This is not valid JSON"

        response = self.client.post("/api/recommend", data=invalid_json)
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
