from .test import Test
from .config import CogConfig


def setup(client):
    return Test(client)
