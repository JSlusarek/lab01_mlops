import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import os
from dotenv import load_dotenv
from settings import Settings


def test_settings_loaded_correctly():
    load_dotenv(dotenv_path=".env.test")  # <- Ładujemy testową konfigurację
    s = Settings()
    assert s.ENVIRONMENT == "test"
    assert s.APP_NAME == "TestApp"
    assert s.DB_PASSWORD == "super-secret-test"
