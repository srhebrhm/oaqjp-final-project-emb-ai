"""
server.py - A Flask application for emotion detection using Watson NLP.
"""

from flask import Flask, request, render_template  # Removed unused jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """
    Handle the POST request for emotion detection.
    
    Returns:
        str: The formatted emotion analysis for the input text.
    """
    data = request.get_json()
    text_to_analyze = data.get('text', '')

    # Get the emotion analysis from the function
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again.", 400

    # Formatting the response as per the customer request
    formatted_response = (f"For the given statement, the system response is "
                          f"'anger': {result['anger']}, "
                          f"'disgust': {result['disgust']}, "
                          f"'fear': {result['fear']}, "
                          f"'joy': {result['joy']} and "
                          f"'sadness': {result['sadness']}. "
                          f"The dominant emotion is {result['dominant_emotion']}.")

    return formatted_response

@app.route('/')
def index():
    """
    Serve the homepage (index.html).
    
    Returns:
        str: The HTML content of the homepage.
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
