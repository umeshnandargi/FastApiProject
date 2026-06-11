import os
from api_server.api_server import ApiServer
from utils.utils import read_yaml_file

def main():
    config_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)) , 
                                    "config", 
                                    "server_config.yaml")
    
    server_config = read_yaml_file(config_file_path)

    api_server = ApiServer(config=server_config)
    api_server.start_server()


if __name__ == "__main__":
    main()