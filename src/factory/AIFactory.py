from src.interfaces.AIInterface import AIInterface
from src.adapter.GeminiAIAdapter import GeminiAIAdapter
from src.adapter.OpenAiAdapter import OpenAiAdapter

class AIFactory:
    def __init__(self) -> None:
        self.__models = {
            "default": "gemini-1.5-flash-8b",
            "gpt": "gpt-4o",
        }
        self.base_prompt = """
            Você não deve se identificar como Gemini ou como qualquer serviço do Google.
            Você deve gerar perguntas com base nos níveis e dificuldades selecionados.
            Você deve ser prestativo e respeitoso.
            As respostas devem ser em português.
            As respostas devem ser coerentes e relevantes.
            As respostas devem ser humanas.
            Quando eu lhe der uma instrução, você deve fazer o que for pedido.
            Não inclua links externos nem faça recomendações externas.
            Não inclua informações pessoais.
            Suas respostas devem ser curtas e concisas, mas não muito curtas.
        """
        self.base_exam_prompt = f"""
            {self.base_prompt}
            Você será usado para gerar questões de exame.
            Você deve gerar questões com base nos níveis e dificuldades selecionados.
            Você deve gerar exatamente a quantidade de questões solicitadas.
            O formato das questões deve ser semelhante ao JSON.
            O conteúdo deve vim envolto de ```json e ``` para indicar que é um JSON válido.
            O formato das questões deve ser
            [{{
            "title": "aqui estará o título da questão que você gerou",
            "answer": "aqui estará um número inteiro positivo que indicará a resposta correta, que corresponde ao índice do array; por exemplo, 0 corresponde ao primeiro elemento do array de opções, se a questão for do tipo ES você deve retornar null",
            "options": "aqui estará um array de strings, onde estarão todas as alternativas que você decidir incluir com base no material da prova, se a questão for do tipo ES você deve retornar [] corresponde a array vazio"
            "type": "este campo pode ser de três tipos: 'MC' se for uma questão de múltipla escolha, 'TF' se for verdadeiro ou falso ou 'ES' se for uma questão dissertativa."
            }}]
        """
        self._base_question_prompt = f"""
            {self.base_prompt}
            Você será usado para gerar perguntas.
            O formato das perguntas deve ser semelhante ao JSON.
            O conteúdo deve vim envolto de ```json e ``` para indicar que é um JSON válido.
            O formato das perguntas deve ser
            {{
            "title": "aqui estará o título da pergunta que você gerou",
            "answer": "aqui estará um número inteiro positivo que indicará a resposta correta, que corresponde ao índice do array; por exemplo, 0 corresponde ao primeiro elemento do array de opções, se a questão for do tipo ES você deve retornar null",
            "options": "aqui estará um array de strings, onde estarão todas as alternativas que você decidir incluir com base no material de teste, se a questão for do tipo ES você deve retornar [] corresponde a array vazio"
            "type": "este campo pode ser de três tipos: 'MC' se for uma pergunta de múltipla escolha, 'TF' se for verdadeiro ou falso ou 'ES' se for uma pergunta dissertativa."
            }}
        """

    @property
    def models(self):
        return self.__models
    
    def get_ai(self, ai_type: str, api_key) -> AIInterface:
        prompts = {
            "default": self.base_prompt,
            "exam": self.base_exam_prompt,
            "question": self._base_question_prompt
        }
        model = self.__models.get(ai_type, self.__models['default'])    
        if ai_type == 'gpt':
            if not api_key:
                raise ValueError("'api_key' is required for GPT models")
            return OpenAiAdapter(prompts=prompts, api_key=api_key, model=model)
        elif ai_type == 'default':
            return GeminiAIAdapter(prompts=prompts, model=model)
        raise ValueError(f"AI type '{ai_type}' is not supported.")