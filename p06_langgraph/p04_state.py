from typing import TypedDict
from typing_extensions import NotRequired


class ContentState(TypedDict):

    topic: str
    
    content: NotRequired[str]
    review_attempts: NotRequired[int]
    review_status: NotRequired[str]
    review_feedback: NotRequired[str]
    final_status: NotRequired[str]