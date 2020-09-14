from typing import Optional, Dict, List
from app.models.pydantic_models import SummaryPayloadSchema
from app.models.tortoise_models import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Optional[Dict]:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def delete(id: int) -> int:
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def get_all() -> List:
    summaries = await TextSummary.all().values()
    return summaries


async def put(id: int, payload: SummaryPayloadSchema) -> Optional[Dict]:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url, summary=payload.summary
    )
    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary[0]
    return None