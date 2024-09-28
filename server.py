from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Route for the emotion detector API
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    # Get the input text from the request JSON
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

# Route for the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)