import sys
import os
import unittest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from app import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(app)

    def test_create_db(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"database": "created"})

if __name__ == '__main__':
    unittest.main()
