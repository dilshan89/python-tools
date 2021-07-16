import json
import yaml

with open("input/input.yaml") as y:
    with open("out/output.json", 'w') as j:
        yaml_data = yaml.safe_load(y.read())
        converted_json_data = json.dumps(yaml_data, indent=2)

        j.write(converted_json_data)
