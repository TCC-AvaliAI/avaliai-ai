from flask import Flask, request, jsonify
from src.services.AIService import AIService

app = Flask(__name__)

@app.route('/api/ai/response', methods=['POST'])
def generate_response_base():
    data = request.get_json()
    if not data or 'prompt' not in data or 'model' not in data:
        return jsonify({"error": "Os campos 'prompt' e 'model' são obrigatórios"}), 400
    prompt = data['prompt']
    model = data.get('model', 'default')
    api_key = data.get('api_key', None)
    try:
        ai_service = AIService(model=model, api_key=api_key)
        response = ai_service.generate_response(prompt)
        return jsonify({"answer": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ai/response/exam', methods=['POST'])
def generate_response():
    data = request.get_json()
    if not data or 'prompt' not in data or 'model' not in data:
        return jsonify({"error": "Os campos 'prompt' e 'model' são obrigatórios"}), 400
    prompt = data['prompt']
    model = data.get('model', 'default')
    api_key = data.get('api_key', None)
    try:
        ai_service = AIService(model=model, api_key=api_key)
        response = ai_service.generate_response_exam(prompt)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ai/response/question', methods=['POST'])
def generate_response_question():
    data = request.get_json()
    if not data or 'prompt' not in data or 'model' not in data:
        return jsonify({"error": "Os campos 'prompt' e 'model' são obrigatórios"}), 400
    prompt = data['prompt']
    model = data.get('model', 'default')
    api_key = data.get('api_key', None)
    try:
        ai_service = AIService(model=model, api_key=api_key)
        response = ai_service.generate_response_question(prompt)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
