from fastapi import APIRouter, Query, HTTPException
from datetime import datetime, timedelta
from app.models.schemas import UsageResponse, Error

router = APIRouter(tags=["Account"])

@router.get(
    "/usage",
    response_model=UsageResponse,
    responses={
        401: {"model": Error},
        403: {"model": Error}
    }
)
async def get_usage(
    startDate: str = Query(..., description="Start date for usage statistics (YYYY-MM-DD)"),
    endDate: str = Query(..., description="End date for usage statistics (YYYY-MM-DD)")
):
    try:
        start = datetime.strptime(startDate, "%Y-%m-%d")
        end = datetime.strptime(endDate, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format (use YYYY-MM-DD)")

    usage = {
        "period": {
            "startDate": startDate,
            "endDate": endDate
        },
        "totalCharacters": 0,
        "totalAudioSeconds": 0,
        "voiceCreations": 0,
        "usageByDay": [
            {
                "date": startDate,
                "characters": 0,
                "audioSeconds": 0
            }
        ]
    }

    return usage
