from typing import TypedDict

from typing_extensions import NotRequired


class SupportState(TypedDict):
    user_query: str

    category: NotRequired[str]
    department: NotRequired[str]
    response: NotRequired[str]