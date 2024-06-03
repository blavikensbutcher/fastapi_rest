import fastapi_cli.cli
from fastapi import FastAPI
from pathlib import Path
import os
import dotenv
dotenv.load_dotenv()

file_path = Path(os.path.abspath("api/user_api.py"))

app = FastAPI()

if __name__ == '__main__':
    fastapi_cli.cli.dev(Path(file_path))
