from flask import Flask, jsonify


if __name__ =='__main__':
    app = Flask(__name__)

    @app.route('/status', methods=['GET'])
    def status():
        return jsonify({'status': 'OK'})

    @app.route('/health', methods=['GET'])
    def health():
        return jsonify({'status': 'OK', 'message': 'All services are running'})

    app.run(debug=True)