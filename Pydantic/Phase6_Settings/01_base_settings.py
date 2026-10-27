"""
=============================================================================
Phase 6: Pydantic Settings
Topic: BaseSettings, Environment Variables & .env Configuration
=============================================================================
Production applications me API keys, database URLs, aur ports ko code me hardcode
nahi kiya jata. Unko .env files ya OS Environment Variables se read kiya jata hai.
Pydantic ka 'pydantic-settings' module:
1. .env file se automatically values load karta hai.
2. Unhe target Python types (int, bool, SecretStr) me convert & validate karta hai.
"""

import os
from pathlib import Path
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

# Current folder ka path nikalna taaki .env aasani se mil jaye
CURRENT_DIR = Path(__file__).resolve().parent
ENV_FILE_PATH = CURRENT_DIR / ".env"

class AppSettings(BaseSettings):
    # Settings configuration: .env file ka path aur encoding
    model_config = SettingsConfigDict(
        env_file=str(ENV_FILE_PATH),
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # 1. Basic App Info
    app_name: str = Field(default="Default App")
    environment: str = Field(default="production")
    debug: bool = Field(default=False)
    port: int = Field(default=8080)

    # 2. Sensitive Keys (SecretStr use karne se logs me key expose nahi hoti)
    openai_api_key: SecretStr
    database_url: str

print("=" * 60)
print("1. Loading Settings from .env File Automatically")
print("=" * 60)

settings = AppSettings()

print(f"App Name    : {settings.app_name}")
print(f"Environment : {settings.environment}")
print(f"Debug Mode  : {settings.debug} (type: {type(settings.debug).__name__})")
print(f"Server Port : {settings.port} (type: {type(settings.port).__name__})")
print(f"Database    : {settings.database_url}")

# SecretStr protection:
print(f"\nSecret Masked Output : {settings.openai_api_key}")
# Asli value access karne ke liye .get_secret_value() use karte hain:
print(f"Actual Secret Value  : {settings.openai_api_key.get_secret_value()[:10]}...")


print("\n" + "=" * 60)
print("2. Overriding via OS Environment Variables")
print("=" * 60)

# Environment variables .env file se zyada priority rakhte hain:
os.environ["PORT"] = "9090"
os.environ["ENVIRONMENT"] = "staging"

dynamic_settings = AppSettings()
print(f"Overridden Port: {dynamic_settings.port}")
print(f"Overridden Env : {dynamic_settings.environment}")
