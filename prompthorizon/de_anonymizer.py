import json
import ast

def de_anonymize(anonymized_object, map_object=None, map_file_path=None, output_file_path=None):
    if map_file_path:
        with open(map_file_path, 'r') as f:
            map_object = json.load(f)
    
    if not map_object:
        raise ValueError("A map_object or map_file_path must be provided.")
        
    if isinstance(anonymized_object, str):
        with open(anonymized_object, 'r') as f:
            anonymized_object = json.load(f)

    keys_map = map_object["keys"]
    values_map = map_object["values"]

    def de_anonymize_recursive(obj):
        if isinstance(obj, dict):
            de_anonymized_dict = {}
            for key, value in obj.items():
                orig_key = [k for k, v in keys_map.items() if v == key][0]
                orig_value = de_anonymize_recursive(value)

                de_anonymized_dict[orig_key] = orig_value

            return de_anonymized_dict

        elif isinstance(obj, list):
            return [de_anonymize_recursive(item) for item in obj]

        else:
            value = [k for k, v in values_map.items() if v == obj][0]
            try:
                return ast.literal_eval(value)
            except (ValueError, SyntaxError):
                return value

    de_anonymized_object = de_anonymize_recursive(anonymized_object)

    if output_file_path:
        with open(output_file_path, 'w') as f:
            json.dump(de_anonymized_object, f, indent=2)
    else:
        return de_anonymized_object
