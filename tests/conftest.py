import pytest

import enet
import enet.live
import enet.test


@pytest.fixture(params=[enet.live.LiveAPIWrapper, enet.test.FakeAPIWrapper])
def api(request):
    return request.param(enet.WSDL_URL, enet.AUTH_TOKEN)
