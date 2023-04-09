import os
import json
import unittest
import tempfile
from prompt_horizon.de_anonymizer import de_anonymize
from prompt_horizon.anonymizer import anonymize, save_map

class TestDeAnonymizer(unittest.TestCase):
    def test_de_anonymize(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_deanonymized_json = {"name": "John", "age": 30, "city": "New York"}

        anonymized_json, map_object = anonymize(input_json)
        deanonymized_json = de_anonymize(anonymized_json, map_object=map_object)

        self.assertEqual(deanonymized_json, expected_deanonymized_json)

    def test_de_anonymize_with_map_file_path(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_deanonymized_json = {"name": "John", "age": 30, "city": "New York"}

        anonymized_json, map_object = anonymize(input_json)

        # Create a temporary map file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".json") as temp_file:
            save_map(map_object, temp_file.name)
            temp_map_file_path = temp_file.name

        deanonymized_json = de_anonymize(anonymized_json, map_file_path=temp_map_file_path)

        self.assertEqual(deanonymized_json, expected_deanonymized_json)

        # Clean up the temporary file
        os.remove(temp_map_file_path)

    def test_de_anonymize_with_output_file_path(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_deanonymized_json = {"name": "John", "age": 30, "city": "New York"}

        anonymized_json, map_object = anonymize(input_json)

        # Create a temporary output file path
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".json") as temp_file:
            temp_output_file_path = temp_file.name

        de_anonymize(anonymized_json, map_object=map_object, output_file_path=temp_output_file_path)

        # Check if the de-anonymized JSON is saved to the specified file location
        with open(temp_output_file_path, 'r') as f:
            saved_deanonymized_json = json.load(f)

        self.assertEqual(saved_deanonymized_json, expected_deanonymized_json)

        # Clean up the temporary file
        os.remove(temp_output_file_path)

    def test_de_anonymize_with_anonymized_file_input(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_deanonymized_json = {"name": "John", "age": 30, "city": "New York"}

        anonymized_json, map_object = anonymize(input_json)

        # Create a temporary anonymized file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".json") as temp_file:
            json.dump(anonymized_json, temp_file)
            temp_anonymized_file_path = temp_file.name

        deanonymized_json = de_anonymize(temp_anonymized_file_path, map_object=map_object)

        self.assertEqual(deanonymized_json, expected_deanonymized_json)

        # Clean up the temporary file
        os.remove(temp_anonymized_file_path)

    def test_de_anonymize_values_only(self):
        input_json = {"name": "John", "age": 30, "city": "New York"}
        expected_deanonymized_json = {"name": "John", "age": 30, "city": "New York"}

        # Anonymize the input JSON with only values
        anonymized_json, map_object = anonymize(input_json, anonymize_keys=False)

        deanonymized_json = de_anonymize(anonymized_json, map_object=map_object)

        self.assertEqual(deanonymized_json, expected_deanonymized_json)


if __name__ == '__main__':
    unittest.main()
