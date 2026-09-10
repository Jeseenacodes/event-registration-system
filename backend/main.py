# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def home():
# return {"message": "Event Registration API is running"} 

from fastapi import FastAPI

app = FastAPI(title="Event Registration API")


@app.get("/api/events")
def get_events():
    return [
        {
            "event_id": 1,
            "name": "AI for Community Organizations",
            "event_date": "2026-10-15",
            "location": "Seattle"
        },
        {
            "event_id": 2,
            "name": "Responsible AI Workshop",
            "event_date": "2026-11-05",
            "location": "Virtual"
        }
    ]



