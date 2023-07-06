from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    print('ToDo List is running')

    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)