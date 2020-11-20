from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = 'localhost'
    port: int = 15232

    class Config:
        env_prefix = 'fast_api_test_'


settings = Settings()
