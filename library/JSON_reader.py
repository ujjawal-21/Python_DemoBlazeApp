import json
import os

class JsonReader:
    @staticmethod
    def getJsonData():
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, "Configuration", "config.json")
        
        with open(file_path) as f:
            return json.load(f)