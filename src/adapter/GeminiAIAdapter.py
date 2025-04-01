import os
import google.generativeai as genai
from interfaces.AIInterface import AIInterface

class GeminiAIAdapter(AIInterface):
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=GOOGLE_API_KEY)
    
    def __init__(self,  base_prompt: str, model: str = 'gemini-pro') -> None:
        self._model = genai.GenerativeModel(model)
        self._persona = base_prompt

    def generate_response(self, prompt: str) -> str:
        try:  
            res = self._model.generate_content(f"{self._persona}\n{prompt}").text
            return res 
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."