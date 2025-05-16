from fastapi import FastAPI
from inference import load_model
from api.models.iris import PredictRequest, PredictResponse
from inference import predict  # zakładam, że tak się nazywa funkcja

app = FastAPI()
model = load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict_route(request: PredictRequest):
    prediction = predict(request)
    return PredictResponse(prediction=prediction)
