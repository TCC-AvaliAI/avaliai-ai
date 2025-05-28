from flask import Flask, request, jsonify
from src.services.AIService import AIService

app = Flask(__name__)

@app.route('/api/ai/response/', methods=['POST'])
def generate_response():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "O campo 'prompt' é obrigatório."}), 400
    
    model = data.get('model', 'gemini')
    prompt = data['prompt']
    
    try:
        service = AIService(model=model)
        response = service.generate_response(prompt)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ai/response/question', methods=['POST'])
def generate_response_question():
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "O campo 'question' é obrigatório."}), 400
    
    model = data.get('model', 'gemini')
    question = data['question']
    
    try:
        service = AIService(model=model)
        response = service.generate_response_question(question)
        return jsonify({"answer": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500