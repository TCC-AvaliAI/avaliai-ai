from src.controllers.AIController import app
from src.factory.AIFactory import AIFactory
from src.adapter.GeminiAIAdapter import GeminiAIAdapter
from src.adapter.OllamaAdapter import OllamaAdapter


if __name__ == '__main__':
    AIFactory.register_adapter("gemini", GeminiAIAdapter)
    AIFactory.register_adapter("gemma", OllamaAdapter)
    AIFactory.register_adapter("deepseek", OllamaAdapter)
        
    app.run(debug=True, port=5000, host='0.0.0.0')