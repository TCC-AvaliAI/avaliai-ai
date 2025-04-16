from abc import ABC, abstractmethod

class AIInterface(ABC):
    
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        pass

    @abstractmethod
    def generate_exam_file(self, exam: str) -> str:
        pass