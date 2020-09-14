from pydantic import BaseModel, AnyHttpUrl
from app.models.tortoise_models import TextSummary
from tortoise.contrib.pydantic import pydantic_model_creator


class SummaryPayloadSchema(BaseModel):
    url: AnyHttpUrl


class SummaryResponseSchema(SummaryPayloadSchema):
    id: int


class SummaryUpdatePayloadSchema(SummaryPayloadSchema):
    summary: str


SummarySchema = pydantic_model_creator(TextSummary)
