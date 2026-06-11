from fastapi import FastAPI
from multiprocessing import Process
import uvicorn
from utils.utils import get_prediction , load_saved_model , prep_inputs

from api_server.schema import InboundRequest 

class ApiServer:
    def __init__(self, config:dict):
        self.server_process :Process | None = None
        self.app : FastAPI = FastAPI()
        self.address = config["ADDRESS"]
        self.port = config["PORT"]
        self.__setup_routes()
        self.model = load_saved_model(model_name=config["model_name"])


    def __setup_routes(self):
        @self.app.get("/home")
        async def home():
            return {"message": "Welcome to the API"}
        
        @self.app.post("/classify")
        def classify(inbound_request :InboundRequest):
            req = inbound_request.model_dump()
            print(req)
            inputs = prep_inputs(req)
            out = get_prediction(model = self.model, inputs=inputs)
            return {"out" : out}

    def start_server(self):
        def _serve():
            uvicorn.run(self.app, host=self.address, port=self.port)

        # self.server_process = Process(target=_serve)
        # self.server_process.start()
        _serve()
