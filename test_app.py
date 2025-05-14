import unittest
import os
from app import app


class RealAPICallTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_real_api_call(self):
        # Example of making a real API call through your Flask route
        response = self.app.get("/convert?from=USD&to=EUR&amount=1")
        data = response.get_json()

        # Imprimir el resultado completo aunque falle
        print("DEBUG - Status Code:", response.status_code)
        print("DEBUG - JSON response:", data)

        # Verificación del código HTTP
        self.assertEqual(response.status_code, 200)

        # Verificación robusta del campo 'result'
        self.assertIn("result", data, msg="Missing 'result' in response")
        self.assertIsInstance(data["result"], float, msg=f"'result' is not float, got {type(data['result'])}")


if __name__ == "__main__":
    unittest.main()
