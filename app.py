from flask import Flask, request, jsonify
from flask_cors import CORS
from fortune_teller import generate_response

app = Flask(__name__)
CORS(app)  # This allows the widget to make requests to your server

@app.route('/api/fortune', methods=['POST'])
def get_fortune():
    data = request.json
    name = data.get('name')
    birthday = data.get('birthday')
    color = data.get('color')
    
    if not all([name, birthday, color, ]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        response = generate_response(name, birthday, color)
        return jsonify({'feedback': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
