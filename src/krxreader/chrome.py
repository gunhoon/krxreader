import datetime


def major_version(dt: datetime.datetime = None) -> int:
    """Major version of Chrome Browser

    NotImplemented
    """
    if dt is None:
        dt = datetime.datetime.now(datetime.timezone.utc)

    print(dt)

    return 114


def user_agent(major_ver: int = 0) -> str:
    """Return the user-agent of Chrome Browser"""

    if major_ver <= 0:
        major_ver = major_version()

    agent = f'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{major_ver}.0.0.0 Safari/537.36'

    return agent
