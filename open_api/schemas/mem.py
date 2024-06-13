from pydantic import BaseModel


class MemSchema(BaseModel):
    uuid: str
    url: str | None
    text: str
