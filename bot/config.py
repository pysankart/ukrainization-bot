from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    """
    Config class.
    """
    API_TOKEN: str


config = Config(API_TOKEN=getenv('API_TOKEN'))
