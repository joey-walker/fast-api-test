from pydantic import BaseSettings


class Settings(BaseSettings):
    host: str = '0.0.0.0'
    port: int = 15232

    class Config:
        env_prefix = 'fast_api_test_'


settings = Settings()
