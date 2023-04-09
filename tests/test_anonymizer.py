import tempfile
import os
import json
import unittest
from prompt_horizon.anonymizer import anonymize


class TestAnonymizer(unittest.TestCase):
    def test_anonymize(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_anonymized_json = {"k1": "v1", "k2": "v2", "k3": "v3"}
        expected_map_object = {
            "keys": {"name": "k1", "age": "k2", "city": "k3"},
            "values": {"John": "v1", "30": "v2", "New York": "v3"}
        }

        anonymized_json, map_object = anonymize(input_json)

        self.assertEqual(anonymized_json, expected_anonymized_json)
        self.assertEqual(map_object, expected_map_object)

    def test_anonymize_with_file(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_anonymized_json = {"k1": "v1", "k2": "v2", "k3": "v3"}
        expected_map_object = {
            "keys": {"name": "k1", "age": "k2", "city": "k3"},
            "values": {"John": "v1", "30": "v2", "New York": "v3"}
        }

        # Create a temporary JSON file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".json") as temp_file:
            json.dump(input_json, temp_file)
            temp_file_path = temp_file.name

        # Call the anonymize function with the file path
        anonymized_json, map_object = anonymize(temp_file_path)

        self.assertEqual(anonymized_json, expected_anonymized_json)
        self.assertEqual(map_object, expected_map_object)

        # Clean up the temporary file
        os.remove(temp_file_path)

    def test_anonymize_with_map_file_path(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}

        # Create a temporary directory to save the map file
        with tempfile.TemporaryDirectory() as temp_dir:
            map_file_path = os.path.join(temp_dir, "map.json")

            anonymized_json, map_object = anonymize(input_json, map_file_path)

            # Check if the map file exists at the specified location
            self.assertTrue(os.path.exists(map_file_path))

            # Load the map file and compare it with the map_object
            with open(map_file_path, 'r') as f:
                loaded_map_object = json.load(f)

            self.assertEqual(map_object, loaded_map_object)

    def test_anonymize_with_anonymized_file_path(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_anonymized_json = {"k1": "v1", "k2": "v2", "k3": "v3"}

        # Create a temporary directory to save the anonymized JSON file
        with tempfile.TemporaryDirectory() as temp_dir:
            anonymized_file_path = os.path.join(temp_dir, "anonymized.json")

            anonymized_json, map_object = anonymize(input_json, anonymized_file_path=anonymized_file_path)

            # Check if the anonymized JSON file exists at the specified location
            self.assertTrue(os.path.exists(anonymized_file_path))

            # Load the anonymized JSON file and compare it with the anonymized_json
            with open(anonymized_file_path, 'r') as f:
                loaded_anonymized_json = json.load(f)

            self.assertEqual(anonymized_json, loaded_anonymized_json)

    def test_anonymize_no_key_anonymization(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_anonymized_json = {"name": "v1", "age": "v2", "city": "v3"}
        expected_map_object = {
            "keys": {},
            "values": {"John": "v1", "30": "v2", "New York": "v3"}
        }

        anonymized_json, map_object = anonymize(input_json, anonymize_keys=False)

        self.assertEqual(anonymized_json, expected_anonymized_json)
        self.assertEqual(map_object, expected_map_object)


if __name__ == '__main__':
    unittest.main()

