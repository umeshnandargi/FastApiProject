# FastApiProject

A lightweight FastAPI server, configured via YAML, for serving machine learning models built with PyTorch.

Given the dependencies in `requirements.txt` (FastAPI, Uvicorn, PyYAML, PyTorch, NumPy), this project exposes a FastAPI-based HTTP API that serves predictions from one or more PyTorch models stored under `ml_models/`.

## Requirements

- Python 3.9+ (recommended)
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/umeshnandargi/FastApiProject.git
   cd FastApiProject
   ```

2. Create and activate a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Server settings are defined in `config/server_config.yaml`. This file is loaded automatically at startup and passed to `ApiServer`. Update it with your desired host, port, and any model-related settings before running the server.

## Running the Server

```bash
python main.py
```

This loads the configuration and starts the API server. Once running, if it's a standard FastAPI setup, interactive API docs should be available at:

- Swagger UI: `http://localhost:<port>/docs`
- ReDoc: `http://localhost:<port>/redoc`

(Replace `<port>` with the value configured in `server_config.yaml`.)


## Contributing

Contributions are welcome. Please open an issue or submit a pull request with a clear description of your changes.
