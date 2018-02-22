import requests

from . import Notifier
from ..exceptions import NotifierException

class Webhook(Notifier):
    def __init__(self, url):
        self.url = url

    def notify(self, message, **kwargs):
        parameters = dict(kwargs, message=message)
        respoonse = requests.get(self.url, params=parameters)
        respoonse.raise_for_status()