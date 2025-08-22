from pydantic import BaseModel

class Reference(BaseModel):
    book: str
    chapter: int
    verse_start: int
    verse_end: int