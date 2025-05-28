import ollama
from src.interfaces.AIInterface import AIInterface
from src.factory.AIFactory import AIFactory


class OllamaAdapter(AIInterface):
    def __init__(self, base_prompt: str, model: str) -> None:
        self.model = model
        self.base_prompt = base_prompt

    def generate_response(self, prompt):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.base_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response['message']['content']
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Desculpe. Pensei errado."
        
    def generate_response_question(self, prompt):
        try:
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.base_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            print("Aquiii", response['message']['content'])
            return response['message']['content']
        except Exception as e:
            print(f"Error generating response: {e}")
            return "Desculpe. Pensei errado."