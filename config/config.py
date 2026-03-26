from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    user: str = 'postgres'
    password: str = '123456'
    host: str = 'localhost'
    port: str = '5432'
    database: str = 'estadisticos_precio_petroleo'
    DATABASE_URL: str = f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"
    

settings = Settings()