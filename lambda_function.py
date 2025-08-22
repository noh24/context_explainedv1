from app.db import SessionLocal
from app.openai_client import OpenAIClient
from app.db_models.lesson import Lesson
from app.config import settings

def lambda_handler(event, context):
    db = SessionLocal()
    client = OpenAIClient()

    latest_lesson = db.query(Lesson).order_by(Lesson.created_at.desc()).first()
    lst = [latest_lesson.book , latest_lesson.chapter ,':', latest_lesson.verse_start, '-', latest_lesson.verse_end]
    prev_end_ref = " ".join(map(str, lst))

    lesson_data = client.generate_lesson(prev_end_ref=prev_end_ref)

    lesson = Lesson(
        book = lesson_data.reference.book,
        chapter = lesson_data.reference.chapter,
        verse_start = lesson_data.reference.verse_start,
        verse_end= lesson_data.reference.verse_end,
        passage= lesson_data.passage,
        context=lesson_data.context,
        themes=lesson_data.themes,
        reflection=lesson_data.reflection,
        model_used=settings.MODEL_NAME
    )

    db.add(lesson)
    db.commit()
    db.refresh(lesson)

    return {"statusCode":200, "body": f"Saved lesson {lesson.id}"}