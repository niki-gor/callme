from pydantic import BaseSettings, PostgresDsn, SecretStr


class Config(BaseSettings):
    dsn: PostgresDsn
    min_connection_count: int = 10
    max_connection_count: int = 50