import dagster as dg
import requests
from ..configs.config import SUCCESS_CHANNEL, FAILURE_CHANNEL
from dagster import ConfigurableResource

class NftyResource(ConfigurableResource):
    def success(self, message: str) -> None:
        requests.post(SUCCESS_CHANNEL, data=message.encode(encoding='utf-8'))

    def failure(self, message: str) -> None:
        requests.post(FAILURE_CHANNEL, data=message.encode(encoding='utf-8'))


