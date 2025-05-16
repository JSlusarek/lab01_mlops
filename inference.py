import joblib
import numpy as np
from api.models.iris import PredictRequest

_model = None  # globalny cache modelu


def load_model(path="model.joblib"):
    global _model
    if _model is None:
        _model = joblib.load(path)
    return _model


def predict(request: PredictRequest) -> str:
    model = load_model()
    features = np.array(
        [
            [  # zachowaj odpowiednią kolejność cech
                request.sepal_length,
                request.sepal_width,
                request.petal_length,
                request.petal_width,
            ]
        ]
    )
    prediction_index = model.predict(features)[0]
    class_names = model.classes_
    return str(class_names[prediction_index])
