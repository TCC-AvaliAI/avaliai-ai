import os
import google.generativeai as genai
from src.interfaces.AIInterface import AIInterface
from dotenv import load_dotenv

load_dotenv()
class GeminiAIAdapter(AIInterface):
    def __init__(self, prompts: dict, model: str = 'gemini-1.5-flash-8b') -> None:
        self._prompts = prompts
        self._model = None

        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY não está definido no ambiente.")
        
        genai.configure(api_key=api_key)
        self._model = genai.GenerativeModel(model)

    def generate_response(self, prompt: str) -> str:
        try:  
            res = self._model.generate_content(f"{self._prompts["response"]}\n{prompt}").text
            return res 
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    def generate_response_exam(self, prompt: str) -> str:
        try:  
            res = self._model.generate_content(f"{self._prompts["exam"]}\n{prompt}").text
            return res 
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    def generate_response_question(self, question):
        try:  
            res = self._model.generate_content(f"{self._prompts["question"]}\n{question}").text
            return res 
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."