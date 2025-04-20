from datetime import datetime, timedelta
from fastapi import HTTPException

# Simulate usage stats for /usage endpoint
async def get_usage(start_date: str, end_date: str):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format (use YYYY-MM-DD)")

    usage = {
        "period": {
            "startDate": start_date,
            "endDate": end_date
        },
        "totalCharacters": 12000,
        "totalAudioSeconds": 450,
        "voiceCreations": 3,
        "usageByDay": [
            {
                "date": (start + timedelta(days=i)).strftime("%Y-%m-%d"),
                "characters": 2000 + i * 100,
                "audioSeconds": 30 + i * 5
            } for i in range((end - start).days + 1)
        ]
    }

    return usage
