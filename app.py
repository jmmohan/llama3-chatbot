import json
from fastapi import FastAPI
from pydantic import BaseModel
import subprocess

app = FastAPI()

class EpicRequest(BaseModel):
    epic: str

def generate_user_stories(epic):
    prompt = f"Generate detailed user stories for the following epic:\n\n{epic}"
    
    # Run LLaMA model
    command = f'ollama run llama3 "{prompt}"'
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
    
    print("Raw Model Response:", result.stdout)  # Debugging output
    
    try:
        return json.loads(result.stdout)  # Ensure proper JSON parsing
    except json.JSONDecodeError:
        return {"error": "Invalid response from the model", "raw_output": result.stdout}

@app.post("/generate_user_stories/")
async def get_user_stories(epic_request: EpicRequest):
    stories = generate_user_stories(epic_request.epic)
    return {"user_stories": stories}

