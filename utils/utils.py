import yaml
from ml_models.model import Model
import torch
import os

def read_yaml_file(file_path:str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data if data is not None else {}

def load_saved_model(model_name:str = "depression_model") -> None:
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                "ml_models" ,
                                "saved_model_files", model_name)
    model = Model(9,12,12,24,16,2)
    if os.path.exists(model_path): 
        model.load_state_dict(torch.load(model_path))
        print(model.eval())
        return model
    else : 
        raise FileNotFoundError(model_path)

def get_prediction(model : Model, inputs : dict):
    inputs = torch.tensor(inputs)
    print(model.eval())
    with torch.no_grad():
      prediction = model.forward(inputs)

    return prediction.argmax().item()

def prep_inputs(request: dict) -> list:
    prepared_inputs = [float(value) for value in request.values()]
    return prepared_inputs

    