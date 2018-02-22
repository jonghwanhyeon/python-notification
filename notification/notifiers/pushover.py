import requests

from . import Notifier
from ..exceptions import NotifierException

pushover_url = 'https://api.pushover.net/1/messages.json'
allowed_parameters = { 'attachment', 'device', 'title', 'url', 'url_title', 'priority', 'sound', 'timestamp' }

class Pushover(Notifier):
    def __init__(self, user, token):
        self.user = user
        self.token = token

    def notify(self, message, **kwargs):
        for key in kwargs:
            if key not in allowed_parameters:
                raise ValueError('Invalid parameter: {key}'.format(key=key))

        parameters = dict(kwargs, user=self.user, token=self.token, message=message)

        files = None
        if 'attachment' in parameters:
            files = { 'attachment': ('attachment.jpg', parameters['attachment'], 'image/jpeg') }

        respoonse = requests.post(pushover_url, data=parameters, files=files)
        respoonse_as_json = respoonse.json()

        if respoonse.status_code != 200:
            raise NotifierException(respoonse_as_json['errors'][0])

        return respoonse_as_json['request']