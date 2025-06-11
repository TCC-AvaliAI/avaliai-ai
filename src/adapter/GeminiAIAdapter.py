import os
import google.generativeai as genai
from src.interfaces.AIInterface import AIInterface

class GeminiAIAdapter(AIInterface):
    def __init__(self, prompts: dict, model: str) -> None:
        super().__init__(model, prompts, headers={}, url="")
        self._gemini_model = None

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY não está definido no ambiente.")
        
        genai.configure(api_key=api_key)
        self._gemini_model = genai.GenerativeModel(model)

    def generate_response(self, prompt: str) -> str:
        try:  
            res = self._gemini_model.generate_content(f"{self._prompts['default']}\n{prompt}").text
            return res 
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    def generate_response_exam(self, prompt: str) -> str:
        try:  
            res = self._gemini_model.generate_content(f"{self._prompts['exam']}\n{prompt}").text
            return res 
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    def generate_response_question(self, question):
        try:  
            res = self._gemini_model.generate_content(f"{self._prompts['question']}\n{question}").text
            return res 
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."