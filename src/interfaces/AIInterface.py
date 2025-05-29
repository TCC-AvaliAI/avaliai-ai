from abc import ABC, abstractmethod

class AIInterface(ABC):
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

    @abstractmethod
    def generate_response_exam(self, prompt: str) -> str:
        pass

    @abstractmethod
    def generate_response_question(self, question: str) -> str:
        pass