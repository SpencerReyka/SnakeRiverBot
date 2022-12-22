from bot import start_loop
from reader.env_reader import EnvConfigLoader

def main():
    print("Starting runner!")
    loader = EnvConfigLoader()
    loader.set_up_env()
    start_loop()

if __name__ == "__main__":
    main()