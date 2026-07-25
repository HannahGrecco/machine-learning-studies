from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

class RequestBody(BaseModel):
    experience_time: int
    sales_count: int
    seasonal_factor: int

model_poly = joblib.load("./sales_revenue_model.pkl")


@app.post("/predict")
def predict(data: RequestBody):

    pred_df = pd.DataFrame([{
        "experience_time": data.experience_time,
        "sales_count": data.sales_count,
        "seasonal_factor": data.seasonal_factor
    }])

    y_pred = float(model_poly.predict(pred_df)[0])

    return {
        "predicted_revenue": float(y_pred)
    }