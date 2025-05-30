import requests
from src.interfaces.AIInterface import AIInterface

class OpenAiAdapter(AIInterface):
    def __init__(self, prompts: dict, api_key: str, model: str) -> None:
        self._prompts = prompts
        self.url = "https://api.openai.com/v1/chat/completions"
        self.__headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        self.messageData = {
            "model": model,
            "max_tokens": 1000,
            "temperature": 0.7,
            "messages": []
        }

    def generate_response(self, prompt: str) -> str:
        try:
            self.messageData["messages"].extend([
                {
                    "role": "system",
                    "content": self._prompts["default"]
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ])
            res = requests.post(self.url, headers=self.__headers, json=self.messageData)
            return res.json().get('choices', [{}])[0].get('message', {}).get('content', 'Desculpe, não consegui entender a resposta.')
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    def generate_response_exam(self, prompt: str) -> str:
        try:
            self.messageData["messages"].extend([
                {
                    "role": "system",
                    "content": self._prompts["exam"]
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ])
            res = requests.post(self.url, headers=self.__headers, json=self.messageData)
            return res.json().get('choices', [{}])[0].get('message', {}).get('content', 'Desculpe, não consegui entender a resposta.')
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    def generate_response_question(self, question):
        try:
            self.messageData["messages"].extend([
                {
                    "role": "system",
                    "content": self._prompts["question"]
                },
                {
                    "role": "user",
                    "content": question
                }
            ])
            res = requests.post(self.url, headers=self.__headers, json=self.messageData)
            return res.json().get('choices', [{}])[0].get('message', {}).get('content', 'Desculpe, não consegui entender a resposta.')
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."