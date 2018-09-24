import os

from .base import BaseAPIWrapper

WSDL_URL = os.getenv(
    'ENET_WSDL_URL',
    'https://webservice.enet.eu/Webservice/V3/MarktpartnerService.svc?wsdl'
)
AUTH_TOKEN = os.getenv('ENET_AUTH_TOKEN')
TESTING_SUB = os.getenv('ENET_TESTING_STUB', '0') in ['1', 'true', 'True']

if not TESTING_SUB and AUTH_TOKEN is None:
    raise EnvironmentError("The environment variable \"ENET_AUTH_TOKEN\" is not set")


__all__ = ('api',)


def get_enet_api(wsdl_url: str = WSDL_URL, auth_token: str = AUTH_TOKEN) -> BaseAPIWrapper:
    if TESTING_SUB:
        from .test import FakeAPIWrapper as APIWrapper
    else:
        from .live import LiveAPIWrapper as APIWrapper

    return APIWrapper(wsdl_url, auth_token)


api: BaseAPIWrapper = get_enet_api()
