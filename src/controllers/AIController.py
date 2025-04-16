from flask import Flask, request, jsonify
from src.services.AIService import AIService

app = Flask(__name__)
ai_service = AIService()

@app.route('/api/ai/response/', methods=['POST'])
def generate_response():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({"error": "O campo 'prompt' é obrigatório."}), 400
    prompt = data['prompt']
    try:
        response = ai_service.generate_response(prompt)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/ai/exam/markdown/', methods=['POST'])
def generate_exam_file():
    data = request.get_json()
    if not data or 'exam' not in data:
        return jsonify({"error": "O campo 'exam' é obrigatório."}), 400
    exam = data['exam']
    try:
        response = ai_service.generate_exam_file(exam)
        return jsonify({"response": response}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500