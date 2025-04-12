import unittest
import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data.decode('utf-8'), "<p>Hello, World!</p>")

if __name__ == '__main__':
    unittest.main() 