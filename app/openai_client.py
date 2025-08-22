from openai import OpenAI
from .config import settings
from app.schemas.lesson_data import LessonData

class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.prompt_template = settings.LESSON_PROMPT
    
    def generate_lesson(self, prev_end_ref: str = "Genesis 1:1-5") -> LessonData:
        prompt = self.prompt_template.format(prev_end_ref=prev_end_ref)

        resp = self.client.chat.completions.parse(
            model=settings.MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            response_format=LessonData
        )

        data = resp.choices[0].message.parsed
        print(data)
        return LessonData.model_validate(data)

