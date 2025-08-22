from pydantic import BaseModel
from app.schemas.reference import Reference

class LessonData(BaseModel):
    reference: Reference
    passage: str
    context: str
    themes: str
    reflection: str

