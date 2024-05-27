import fastapi as FastAPI
import torch 
from utils.model import CNN
from utils.preprocessor import preprocessor

app = FastAPI.FastAPI()

model = CNN(num_classes=2)
model.load_state_dict(torch.load("models/model.pt"))
model.eval()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/predict")
def predict(data: str):
    """
    Predicts if a tumor is present in an image

    Args:
        data (str): path to image

    Returns:
        dict: A dictionary containing the prediction
    """
    image = preprocessor(data)
    output = model(image)
    _, predicted = torch.max(output, 1)
    if predicted.item() == 0:
        return {"prediction": "negative: no tumor detected"}
    else:
        return {"prediction": "positive: tumor detected"}
    
