from abc import ABC

class BaseAIAdapter(ABC):
    def __init__(self, model: str, prompts: dict, headers: dict, url: str) -> None:
        self.url = url
        self._headers = headers
        self._prompts = prompts
        self._model = model
        self._message_data = {
            "model": model,
            "max_tokens": 1000,
            "temperature": 0.7,
            "messages": []
        }
