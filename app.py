from flask import Flask, jsonify, render_template
import requests
import json
app = Flask(__name__)

# Pulling from API, formatting response
url = "YOUR URL HERE"
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)
json_data = response.json()

# Create a dict for each category
categories = {
    'concepts': [],
    'compute': [],
    'storage': [],
    'database': [],
    'security': [],
    'management': [],
    'containers': [],
    'migration': [],
    'networking and content delivery': [],
    'machine learning': [],
    'devtools': [],
    'iot': [],
    'frontend': [],
    'end user computing': [],
    'analytics': [],
    'application integration': [],
    'business applications': [],
    'satellite': [],
    'quantum': [],
    'robotics': [],
    'blockchain': [],
    'game development': [],
    'media services': [],
    'financial services': [],
    'customer engagement': []
}

# Putting data into nested_dicts
for item in json_data['items']:
    category = item.get('category')
    if category in categories:
        categories[category].append(item)

# Creating flashcards for each item in each category
flashcards = []
for category, items in categories.items():
    for item in items:
        flashcard = {
            'category': category,
            'definition': item.get('definition'),
            'item': item.get('item'),
            'id': item.get('id'),
        }
        flashcards.append(flashcard)

# Flask routes
@app.route('/')
def index():
    return render_template('index.html', flashcards=flashcards)
@app.route('/flashcards')
def get_flashcards():
    return jsonify(flashcards)
@app.route('/categories')
def get_categories():
    return jsonify(list(categories.keys()))
@app.route('/category/<category_name>')
def get_category(category_name):
    if category_name in categories:
        return jsonify(categories[category_name])
    else:
        return jsonify({'error': 'Category not found'}), 404
@app.route('/flashcard/<int:flashcard_id>')
def get_flashcard(flashcard_id):
    for flashcard in flashcards:
        if flashcard['id'] == flashcard_id:
            return jsonify(flashcard)
    return jsonify({'error': 'Flashcard not found'}), 404
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 
