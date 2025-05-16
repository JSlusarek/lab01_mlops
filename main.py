# main.py
import os
import argparse
import yaml
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    # 1. Wczytaj odpowiedni .env plik
    dotenv_file = f".env.{environment}"
    if not os.path.exists(dotenv_file):
        raise FileNotFoundError(f"No such .env file: {dotenv_file}")
    load_dotenv(dotenv_file)

    # 2. Wczytaj odszyfrowany plik secrets.yaml i ustaw zmienne środowiskowe
    if os.path.exists("secrets.yaml"):
        with open("secrets.yaml", "r", encoding="utf-8") as f:
            secrets = yaml.safe_load(f)
            for key, value in secrets.items():
                os.environ[key] = str(value)
    else:
        raise FileNotFoundError(
            "secrets.yaml not found. Did you decrypt it with `sops`?"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables and secrets."
    )
    parser.add_argument(
        "--environment", type=str, default="dev", help="dev, test, prod"
    )
    args = parser.parse_args()

    export_envs(args.environment)

    settings = Settings()
    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("DB_PASSWORD: ", settings.DB_PASSWORD)  # <- sprawdzenie sekretu
