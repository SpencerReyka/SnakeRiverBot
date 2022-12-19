import os
import json
from bot import start_loop


def read_secrets() -> dict:
    filename = os.path.join('config.json')
    try:
        with open(filename, mode='r') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {}

def read_and_parse_secrets(): 
    secrets = read_secrets()
    for secret in secrets:
        #print(secrets[secret])
        if secret not in os.environ: 
            os.environ[secret] = secrets[secret]
            #print("adding" + secret + " to env")


def main():
    print("Starting runner!")
    read_and_parse_secrets()
    start_loop()

if __name__ == "__main__":
    main()