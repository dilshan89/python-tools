import json
import yaml

with open("input/input.json") as j:
    with open("out/output.yaml", 'w') as y:
        json_data = json.loads(j.read())
        converted_json_data = json.dumps(json_data)

        yaml_data = yaml.safe_load(converted_json_data)
        converted_yaml_data = yaml.dump(yaml_data)

        y.write(converted_yaml_data)
