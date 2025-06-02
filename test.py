from ensure import ensure_annotations
from pathlib import Path
from box import ConfigBox
import yaml
from box.exceptions import BoxValueError
import json

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
  try:
    with open(path_to_yaml) as yaml_file:
      contents = yaml.safe_load(yaml_file)
      return ConfigBox(contents)
  except BoxValueError:
    raise ValueError("yaml file is empty")
  except Exception as e:
    raise e

@ensure_annotations
def save_json(path: Path, data: dict):
  with open(path, 'w') as file:
    json.dump(data, file, indent = 4)

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
  with open(path) as f:
    content = json.load(f)
    return ConfigBox(content)
  

# get = read_yaml(Path("config/config.yaml"))
# print(get)

# dicto = {"Name": "Tareq", 'Age': 23}
# save_json(Path('test.json'), dicto)

# print(load_json(Path("test.json")))

  