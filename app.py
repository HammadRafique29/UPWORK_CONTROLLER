
import json
import requests
from datetime import datetime
from flask import Flask, request, jsonify

PROPOSALS = []
app = Flask(__name__)


def download_file(url, file_path):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        print(response.content)
        response = response.content.decode("utf-8").replace('\n', ' ')
        response = json.loads(response)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Failed to download the file: {e}")
        return None




@app.route('/download', methods=['POST'])
def index():
    data = request.get_json()
    url = data.get('url')
    if not url: return jsonify({'error': 'URL is required'}), 400
    try:
        data = download_file(url, "None")
        PROPOSALS.append({'date':datetime.now(), "Data":data})
        return jsonify({'message': f'File Sended'}), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/getProposals', methods=['GET'])
def getProposals():
    data = request.get_json()
    try: return jsonify({'Data': PROPOSALS}), 200
    except requests.RequestException as e: return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
