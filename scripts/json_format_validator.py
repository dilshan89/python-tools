import json

def validateJsonText(jsonTxt):
    try:
        json.loads(jsonTxt)
    except ValueError as err:
        print(err)
        return False
    return True

invalidText = """{"name": "Dilshan", "age": 30, "gender": "Male", }"""
print("JSON string validation: ", validateJsonText(invalidText))

validText = """{"name": "Dilshan", "age": 30, "gender": "Male" }"""
print("JSON string validation: ", validateJsonText(validText))


def validateJsonFile(jsonFile):
    try:
        json.load(jsonFile)
    except ValueError as err:
        print(err)
        return False
    return True

# with open("input/input.json") as f:
#     print("JSON file validation: ", validateJsonFile(f))