from flask import Flask, jsonify, request
app = Flask(__name__)

# In-memory data store
monitoring_data = []

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/readings', methods=['GET'])
def get_readings():
    return jsonify(monitoring_data)

@app.route('/api/readings', methods=['POST'])
def add_reading():
    data = request.json
    monitoring_data.append(data)
    return jsonify({"message": "Reading added"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
