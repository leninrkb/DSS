import json
import os

def load() -> dict:
    try:
        with open('setup.json', 'r') as setup_file:
            setup = json.load(setup_file)
            print(type(setup))
            return setup
    except:
        print('cannot read setup.json file')
        return None

def save(setup: dict):
    try:
        with open('setup.json', 'w') as setup_file:
            json.dump(setup, setup_file, indent=4)
    except:
        print('cannot write data in setup.json')
        
load()