import json
import re
from src.factory.AIFactory import AIFactory

class AIService:
    def __init__(self, model='gemini'):
        self.ai = AIFactory().get_ai(model)
    
    def proccess_and_parse_response(self, response):
        match = re.search(r'```json\n(.*?)\n```', response, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1))
            except json.JSONDecodeError:
                raise ValueError("Erro ao decodificar JSON da resposta.")
        raise ValueError("Nenhum JSON válido encontrado na resposta.")
    
    def proccess_and_parse_markdown(self, response):
        match = re.search(r'```markdown\n(.*?)\n```', response, re.DOTALL)
        if match:
            return match.group(1)
        return "Nenhum markdown válido encontrado na resposta."

    def generate_response(self, prompt):
        response = self.ai.generate_response(prompt)
        return self.proccess_and_parse_response(response)
    
    def generate_exam_file(self, exam):
        response = self.ai.generate_exam_file(exam)
        return self.proccess_and_parse_markdown(response)
