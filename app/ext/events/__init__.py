from .events import Events
from .config import CogConfig


def setup(client):
    return Events(client)
