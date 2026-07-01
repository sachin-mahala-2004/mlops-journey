import os
import json
def load_config(path, default=None):
    # If file exists → load and return it
    if os.path.exists:
        with open(path,"r") as f:
            return json.load(f)
    # If not → return default
    else:
        return default
    pass

print(load_config("config.json"))