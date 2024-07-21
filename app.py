
import re
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
        if data:
            if 'des' in data:
                text = data['des']
                budget_pattern = r'Budget\s*:\s*\$([\d,]+)'
                posted_date_pattern = r'Posted On\s*:\s*([\w\s,:\d]+ UTC)'
                skills_pattern = r'Skills\s*:(.+?)\s*Country'
                country_pattern = r'Country\s*:\s*(.+?)\s*click'
                category_pattern = r'Category\s*:\s*(.+?)\s*Skills'
                try:
                    budget = posted_date = skills = country = category = None 
                    budget = re.search(budget_pattern, text).group(1)
                    posted_date = re.search(posted_date_pattern, text).group(1)
                    skills = re.search(skills_pattern, text).group(1).strip()
                    country = re.search(country_pattern, text).group(1).strip()
                    category = re.search(category_pattern, text).group(1).strip()
                except: pass
                
                data['budget'] = budget if budget else "None"
                data['posted_date'] = posted_date if posted_date else "None"
                data['skills'] = skills if skills else "None"
                data['country'] = country if country else "None"
                data['category'] = category if category else "None"
                    
        PROPOSALS.append(data)
        return jsonify({'message': f'File Sended'}), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500


@app.route('/getProposals', methods=['GET'])
def getProposals():
    # data = request.get_json()
    try: return jsonify({'Data': PROPOSALS}), 200
    except requests.RequestException as e: return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
