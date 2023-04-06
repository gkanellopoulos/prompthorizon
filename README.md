# Prompt Horizon

**Prompt Horizon** is a Python library for anonymizing and de-anonymizing JSON objects. The library makes it easy for developers to anonymize sensitive data in JSON objects before sharing or storing them (ex.: Sharing a JSON object as part of a prompt for ChatGPT), and later restore the original data using a mapping file.


## Installation

To install the library, use pip:

```
pip install prompthorizon
```

## Usage

Here's a basic example demonstrating how to use the Prompthorizon library:

```python
from prompthorizon.anonymizer import anonymize, save_map
from prompthorizon.de_anonymizer import de_anonymize

# Sample JSON object
input_json = {"name": "John", "age": 30, "city": "New York"}

# Anonymize the JSON object
anonymized_json, map_object = anonymize(input_json)

# Save the map object to a file
save_map(map_object, 'map.json')

# De-anonymize the JSON object using the map object
deanonymized_json = de_anonymize(anonymized_json, map_object=map_object)
```

You can also use file paths instead of JSON objects as input for the \`anonymize\` and `de_anonymize` functions:

```python
# Anonymize a JSON object from a file and save the anonymized object and map object to files
anonymized_json, map_object = anonymize('input.json', map_file_path='map.json')

# De-anonymize the JSON object from a file using a map file
deanonymized_json = de_anonymize('anonymized.json', map_file_path='map.json')
```

## License

This project is licensed under the [MIT License](LICENSE).