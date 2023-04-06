import json
from collections.abc import MutableMapping

def anonymize(json_input, map_file_path=None, anonymized_file_path=None):
    key_counter = 1
    value_counter = 1
    keys_map = {}
    values_map = {}

    if isinstance(json_input, str):
        with open(json_input, 'r') as f:
            json_object = json.load(f)
    else:
        json_object = json_input

    def anonymize_recursive(obj):
        nonlocal key_counter, value_counter

        if isinstance(obj, dict):
            anonymized_dict = {}
            for key, value in obj.items():
                if key not in keys_map:
                    keys_map[key] = f"k{key_counter}"
                    key_counter += 1

                anon_key = keys_map[key]
                anon_value = anonymize_recursive(value)

                anonymized_dict[anon_key] = anon_value

            return anonymized_dict

        elif isinstance(obj, list):
            return [anonymize_recursive(item) for item in obj]

        else:
            str_obj = str(obj)
            if str_obj not in values_map:
                values_map[str_obj] = f"v{value_counter}"
                value_counter += 1

            return values_map[str_obj]

    anonymized_object = anonymize_recursive(json_object)
    map_object = {"keys": keys_map, "values": values_map}

    # Save the map file if a path is provided
    if map_file_path:
        save_map(map_object, map_file_path)

    # Save the anonymized JSON object if a path is provided
    if anonymized_file_path:
        with open(anonymized_file_path, 'w') as f:
            json.dump(anonymized_object, f, indent=2)

    return anonymized_object, map_object

def save_map(map_object, filename):
    with open(filename, 'w') as f:
        json.dump(map_object, f, indent=2)