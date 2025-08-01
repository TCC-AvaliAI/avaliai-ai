import requests
from src.interfaces.AIInterface import AIInterface

class OpenAiAdapter(AIInterface):
    def __init__(self, prompts: dict, api_key: str, model: str) -> None:
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        url = "https://api.openai.com/v1/chat/completions"
        super().__init__(model, prompts, headers=headers, url=url)
        

    def generate_response(self, prompt: str) -> str:
        return super().generate_response(prompt)
        
    def generate_response_exam(self, prompt: str) -> str:
        return super().generate_response_exam(prompt)
        
    def generate_response_question(self, question) -> str:
        return super().generate_response_question(question)