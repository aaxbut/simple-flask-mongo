from pydantic import BaseSettings


class Settings(BaseSettings):

    DATABASE_NAME: str = 'test_db'
    DATABASE_HOST: str = 'mongodb'
    DATABASE_USER: str = 'test_user'
    DATABASE_PASS: str = 'test_pass'
    DATABASE_PORT: str = 27017

    @property
    def URI_DB(self):
        return (
            f"mongodb://{self.DATABASE_HOST}:{self.DATABASE_PORT}"
        )

    @property
    def AUTH_URI_DB(self):
        return (
            f"mongodb://{self.DATABASE_USER}:{self.DATABASE_PASS}@"
            f"{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )

# mongodb://my_user:my_password@127.0.0.1:27017/my_db

settings = Settings()
