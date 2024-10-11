from flask import Flask, request, jsonify

app = Flask(__name__)

motivational_books = [
    {"title": "Man’s Search for Meaning", "author": "Victor E. Frankl"},
    {"title": "Awaken the Giant Within", "author": "Anthony Robbins"},
    {"title": "The 7 Habits of Highly Effective People", "author": "Stephen R. Covey"},
    {"title": "Think and Grow Rich", "author": "Napoleon Hill"},
    {"title": "The Power of Positive Thinking", "author": "Norman Vincent Peale"},
    {"title": "The Magic of Thinking Big", "author": "David J. Schwartz"},
    {"title": "The Four Agreements", "author": "Don Miguel Ruiz"},
    {"title": "The Alchemist", "author": "Paulo Coelho"},
    {"title": "The Secret", "author": "Rhonda Byrne"},
    {"title": "Make Your Bed", "author": "Admiral William H. McRaven"}
]

@app.route('/recommend', methods=['GET'])
def recommend_books():
    preferences = request.args.get('preferences')
    recommendations = [book for book in motivational_books if preferences.lower() in book['title'].lower() or preferences.lower() in book['author'].lower()]
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
