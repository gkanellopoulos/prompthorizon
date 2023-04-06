import unittest
from prompt_horizon.anonymizer import anonymize, save_map
from prompt_horizon.de_anonymizer import de_anonymize

class TestAnonymizerComplex(unittest.TestCase):
    def test_anonymize_complex(self):
        json_object = {
            "person": {
                "name": "John",
                "age": 30,
                "city": "New York",
                "contact": {
                    "email": "john@example.com",
                    "phone": "555-555-5555",
                    "address": {
                        "street": "123 Main St",
                        "city": "New York",
                        "zipcode": 10001,
                        "country": "USA",
                    },
                },
                "siblings": [
                    {"name": "Jane", "age": 28, "city": "New York"},
                    {"name": "Jim", "age": 32, "city": "Los Angeles"},
                ],
            }
        }

        anonymized_object, map_object = anonymize(json_object)
        de_anonymized_object = de_anonymize(anonymized_object, map_object)

        self.assertEqual(json_object, de_anonymized_object)

        # Save the map_object to a file for manual inspection
        save_map(map_object, 'test_complex_map.json')

if __name__ == "__main__":
    unittest.main()
