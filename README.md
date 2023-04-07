# Prompt-Horizon

**Prompt-Horizon** is a Python library that enables developers to anonymize JSON objects by creating placeholders for keys and values, while generating a reversible mapping to restore the original JSON data. The purpose of this library is to facilitate data sharing while preserving privacy and allowing for the de-anonymization of the data when required.

*Note: I had the idea for this library when I was trying to find a way to obfuscate data objects such as JSON to include them as contextual information in prompts (hence the name).*

**Prompt-Horizon is not designed to specifically identify and anonymize PII (personally identifiable information) or other sensitive data within the JSON objects.**

<br>

## Installation

```bash
pip install prompt-horizon
```

## Usage

### Anonymize JSON

<br>

```python
from prompt_horizon import anonymize

input_json = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "favorites": ["pizza", "basketball"]
}

#This line will return the anonymized JSON object and the mapping object.
anonymized_json, map_object = anonymize(input_json)
```

Original JSON:

```json
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "favorites": ["pizza", "basketball"]
}
```

Anonymized JSON:

```json
{
    "a1": "a2",
    "a3": "a4",
    "a5": "a6",
    "a7": ["a8", "a9"]
}
```
<br>

#### input and output file handling is supported

```python
from prompt_horizon import anonymize

#This line will read the JSON data from "input.json", anonymize it, and save the anonymized JSON to "anonymized.json".
anonymized_json, map_object = anonymize("input.json", output_file_path="anonymized.json")
```

<br>

### De-anonymize JSON

<br>

```python
from prompt_horizon import de_anonymize

#This line will return the de-anonymized JSON object, which should be the same as the original input JSON.
deanonymized_json = de_anonymize(anonymized_json, map_object=map_object)
```

#### input and output files are supported

```python
from prompt_horizon import de_anonymize

#This will read the anonymized JSON data from "anonymized.json", the mapping object from "map_file.json", de-anonymize the JSON data, and save the de-anonymized JSON to "deanonymized.json".
deanonymized_json = de_anonymize("anonymized.json", map_file_path="map_file.json", output_file_path="deanonymized.json")
```



<br>

### Saving and loading the map

<br>

## License

This project is licensed under the [MIT License](LICENSE).
