from src.interfaces.AIInterface import AIInterface
from src.adapter.GeminiAIAdapter import GeminiAIAdapter

class AIFactory:
    def __init__(self) -> None:
        self.base_prompt = """
            You must not identify yourself as Gemini or any Google service.
            You must generate questions based on the levels and difficulties selected.
            You must be helpful and respectful.
            Answers must be in Portuguese.
            Answers must be coherent and relevant.
            Answers must be human.
            When I give you a prompt, you must do what is asked.
            Do not include external links or make external recommendations.
            Do not include personal information.
            Your answers should be short and concise, but not too short.
        """
        self.base_exam_prompt = f"""
            {self.base_prompt}
            You will be used to generate exam questions.
            The format of the questions should be similar to JSON.
            The format of the questions should be
            [{{
            "title": "here will be the title of the question you generated",
            "answer": "here will be a positive integer that will indicate the correct answer, which corresponds to the index of the array; for example, 0, corresponds to the first element of the options array",
            "options": "here will be an array of strings, where will be all the alternatives that you decide to include based on the test's furniture"
            "type": "this field can be of three types: 'MC' if it is a multiple choice question, 'TF' if it is true or false or 'ES', if it is an essay question."
            }}]
        """
        self._base_question_prompt = f"""
            {self.base_prompt}
            You will be used to generate questions.
            The format of the questions should be similar to JSON.
            The format of the questions should be
            {{
            "title": "here will be the title of the question you generated",
            "answer": "here will be a positive integer that will indicate the correct answer, which corresponds to the index of the array; for example, 0, corresponds to the first element of the options array",
            "options": "here will be an array of strings, where will be all the alternatives that you decide to include based on the test furniture"
            "type": "this field can be of three types: 'MC' if it is a multiple choice question, 'TF' if it is true or false or 'ES', if it is an essay question." 
            }}
        """
    def get_ai(self, ai_type: str, model: str = "gemini-1.5-flash-8b") -> AIInterface:
        prompts = {
            "response": self.base_prompt,
            "exam": self.base_exam_prompt,
            "question": self._base_question_prompt
        }
        if ai_type == 'gemini':
            return GeminiAIAdapter(prompts=prompts, model=model)
        else:
            raise ValueError("Invalid AI type")