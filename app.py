
import re
import json
import pytz
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


@app.route('/update', methods=['POST'])
def index():
    data = request.get_json()
    data = data.get('data')
    if not data: return jsonify({'error': 'Data is required'}), 400
    try:
        # data = download_file(url, "None")
        if data:
            print(data.keys())
            if 'des' in data.keys():
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
                
                data['date'] = f"{datetime.now().date().today()} {datetime.now().hour}:{datetime.now().minute}:{datetime.now().second}"
                data['budget'] = budget if budget else "None"
                data['posted_date'] = posted_date if posted_date else "None"
                data['skills'] = skills if skills else "None"
                data['country'] = country if country else "None"
                data['category'] = category if category else "None"
                    
        PROPOSALS.append(data)
        return jsonify({'message': f'File Sended'}), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500



# Function to parse the date string
def parse_date(date_string):
    return datetime.strptime(date_string, '%a, %d %b %Y %H:%M:%S %z')

# Function to convert the date to Asia/Karachi timezone
def convert_to_asia_karachi(date):
    asia_karachi = pytz.timezone('Asia/Karachi')
    return date.astimezone(asia_karachi).strftime('%a, %d %b %Y %H:%M:%S %z')

@app.route('/getProposals', methods=['GET'])
def getProposals():
    try:
        # Filter out proposals without a 'time' key
        valid_proposals = [p for p in PROPOSALS if 'time' in p]
        
        # Sort the proposals based on the parsed date in descending order
        sorted_proposals = sorted(valid_proposals, key=lambda x: parse_date(x['time']), reverse=True)
        
        # Convert each proposal's time to Asia/Karachi timezone
        for proposal in sorted_proposals:
            proposal['time'] = convert_to_asia_karachi(parse_date(proposal['time']))
        
        return jsonify({'Data': sorted_proposals}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True)
