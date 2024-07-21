import requests
import json

def send_File():
    url = 'http://131.186.0.242:5000/download'
    payload = {'url': 'https://zapier-dev-files.s3.amazonaws.com/cli-platform/19925/MjDPmwosAMxsN_kmR8d0aylZFgD0AOQeqUwMamqmei9KYMBcGgvdahBkz7kq7OBEBCacLNTGj1AAj1T3apF0ttxOHC0hfq_6zltN_Q3A5stEuhwRiSvY0_Kwb7o1SeZeQ4JABSO-kfsv8gcB9mhTXKM5XIE8jOvbsOwTOpODwKg'}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, json=payload, headers=headers)
    print(response.json())
    
def getProposals():
    url = 'http://131.186.0.242:5000/getProposals'
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, headers=headers)
    response = response.json()
    print(response)
    print(response['Data'])
    # print(response.json())

if __name__ == '__main__':
    # send_File()
    getProposals()
    
    import re
    text = """We're seeking an experienced Python developer to build the backend for SureCopy.ai, an innovative AI-powered sales letter generation system. This project leverages advanced language models to create high-quality, long-form sales letters for professional marketers and agencies.  The system will be entirely email based, no web interface of any kind for this initial launch.  Precise job details have been attached to this post.  Unique Opportunity:  You'll have access to our Claude AI and ChatGPT teams to accelerate development, as well as other AI-powered tools to assist in the process. This is a chance to work at the cutting edge of AI-assisted software development.  If you're excited about pushing the boundaries of AI in SaaS and have the skills we're looking for, we'd love to hear from you.  Budget : $3,000  Posted On : July 21, 2024 12:43 UTC  Category : Back-End Development  Skills :MongoDB, Python, API, Artificial Intelligence  Country : United States  click to apply"""
    # Define the regex patterns
    budget_pattern = r'Budget\s*:\s*\$([\d,]+)'
    posted_date_pattern = r'Posted On\s*:\s*([\w\s,:\d]+ UTC)'
    skills_pattern = r'Skills\s*:(.+?)\s*Country'
    country_pattern = r'Country\s*:\s*(.+?)\s*click'
    category_pattern = r'Category\s*:\s*(.+?)\s*Skills'

    # Extract the information using regex
    budget = re.search(budget_pattern, text).group(1)
    posted_date = re.search(posted_date_pattern, text).group(1)
    skills = re.search(skills_pattern, text).group(1).strip()
    country = re.search(country_pattern, text).group(1).strip()
    category = re.search(category_pattern, text).group(1).strip()

    # Clean the string by removing the extracted parameters
    text = re.sub(budget_pattern, '', text)
    text = re.sub(posted_date_pattern, '', text)
    text = re.sub(skills_pattern, '', text)
    text = re.sub(country_pattern, '', text)
    text = re.sub(category_pattern, '', text)
    
    # Print the extracted information
    print(f"Budget: ${budget}")
    print(f"Posted Date: {posted_date}")
    print(f"Skills: {skills}")
    print(f"Country: {country}")
    print(f"Category: {category}")

    # Print the cleaned text
    print("\nCleaned Text:")
    print(text.strip())

    
    
