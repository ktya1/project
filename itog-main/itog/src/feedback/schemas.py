from pydantic import BaseModel

class FeedbackCreate(BaseModel):
    name : str
    question: str


class FeedbackRead(BaseModel):
    id: int
    name : str
    question: str