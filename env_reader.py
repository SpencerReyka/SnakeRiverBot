import os
import json

def read_config_to_json() -> dict:
    filename = os.path.join('config.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

def parse_envs_from_json(config):
    for env in config["EnvVar"]:
        if env not in os.environ: 
            os.environ[env] = config["EnvVar"][env]
            # print("adding " + env + ":[" + config["EnvVar"][env] + "] to env")

def set_up_env(): 
    configs = read_config_to_json()

    for app in configs["App Configs"]:
        parse_envs_from_json(app)

    parse_envs_from_json(configs)