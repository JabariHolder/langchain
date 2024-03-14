from .config import USE_PYDANTIC_V2

try:
    if USE_PYDANTIC_V2:
        from pydantic.main import *
    else:
        from pydantic.v1.main import *  # noqa: F403
except ImportError:
    from pydantic.main import *  # noqa: F403