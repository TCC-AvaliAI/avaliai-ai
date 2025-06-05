import os
from src.interfaces.AIInterface import AIInterface

class GroqAiAdapter(AIInterface):
    def __init__(self, prompts: dict, model: str) -> None:
        api_key = os.getenv("GROQ_API_KEY")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        url = " https://api.groq.com/openai/v1/chat/completions"
        super().__init__(model, prompts, headers=headers, url=url)

    def generate_response(self, prompt: str) -> str:
        return super().generate_response(prompt)
        
    def generate_response_exam(self, prompt: str) -> str:
        return super().generate_response_exam(prompt)
        
    def generate_response_question(self, question):
        return super().generate_response_question(question)