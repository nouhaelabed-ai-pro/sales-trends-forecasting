from fastapi import FastAPI

app = FastAPI(
    title="Sales Trends Forecasting",
    description="An API for sales trend analysis and forecasting",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to Sales Trends Forecasting API"}
