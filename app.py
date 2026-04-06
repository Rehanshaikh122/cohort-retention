from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client.test

@app.get("/cohort-retention")
def get_retention():
    pipeline = [
        {
            "$addFields": {
                "cohort": {
                    "$dateToString": {"format": "%Y-%m", "date": "$created_at"}
                },
                "activityMonth": {
                    "$dateToString": {"format": "%Y-%m", "date": "$last_login"}
                }
            }
        },
        {
            "$addFields": {
                "monthDiff": {
                    "$subtract": [
                        {"$month": "$last_login"},
                        {"$month": "$created_at"}
                    ]
                }
            }
        },
        {
            "$group": {
                "_id": {
                    "cohort": "$cohort",
                    "month": "$monthDiff"
                },
                "users": {"$addToSet": "$user_id"}
            }
        },
        {
            "$project": {
                "cohort": "$_id.cohort",
                "month": "$_id.month",
                "count": {"$size": "$users"}
            }
        },
        {
            "$sort": {"cohort": 1, "month": 1}
        }
    ]

    result = list(db.users.aggregate(pipeline))
    return result
