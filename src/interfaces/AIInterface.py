import requests
from abc import ABC, abstractmethod
from .BaseAIAdapter import BaseAIAdapter

class AIInterface(BaseAIAdapter):
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        try:
            self._message_data["messages"] = [
                {
                    "role": "system",
                    "content": self._prompts["default"]
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
            res = requests.post(self.url, headers=self._headers, json=self._message_data)
            return res.json().get('choices', [{}])[0].get('message', {}).get('content', 'Desculpe, não consegui entender a resposta.')
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    @abstractmethod
    def generate_response_exam(self, prompt: str) -> str:
        try:
            self._message_data["messages"] = [
                {
                    "role": "system",
                    "content": self._prompts["exam"]
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
            res = requests.post(self.url, headers=self._headers, json=self._message_data)
            return res.json().get('choices', [{}])[0].get('message', {}).get('content', 'Desculpe, não consegui entender a resposta.')
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."
        
    @abstractmethod    
    def generate_response_question(self, question):
        try:
            self._message_data["messages"] = [
                {
                    "role": "system",
                    "content": self._prompts["question"]
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
            res = requests.post(self.url, headers=self._headers, json=self._message_data)
            return res.json().get('choices', [{}])[0].get('message', {}).get('content', 'Desculpe, não consegui entender a resposta.')
        except Exception as e:
            print(e)
            return "Desculpe. Pensei errado."