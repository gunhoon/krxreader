import datetime

from krxreader.chrome import major_version
from krxreader.chrome import user_agent


def test_major_version():
    dt = datetime.datetime.fromisoformat('2023-05-31 00:00:23.283+00:00')
    version = major_version(dt)

    assert version == 114


def test_user_agent():
    agent = user_agent(major_ver=120)
    assert agent == 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

    agent = user_agent(major_ver=1)
    assert agent == 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/1.0.0.0 Safari/537.36'

    agent = user_agent()
    assert agent != 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/0.0.0.0 Safari/537.36'
