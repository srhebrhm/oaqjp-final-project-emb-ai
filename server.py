from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Import your emotion detection function
app = Flask(__name__)
# Route for the emotion detector API
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    # Get the input text from the request JSON
    data = request.get_json()
    text_to_analyze = data.get('text', '')
    if not text_to_analyze:
        return jsonify({"error": "No text provided"}), 400
    # Get the emotion analysis from the function
    result = emotion_detector(text_to_analyze)
    # Formatting the response as per the customer request
    response = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }
    # Return the response in the required format
    formatted_response = (f"For the given statement, the system response is "
                          f"'anger': {response['anger']}, "
                          f"'disgust': {response['disgust']}, "
                          f"'fear': {response['fear']}, "
                          f"'joy': {response['joy']} and "
                          f"'sadness': {response['sadness']}. "
                          f"The dominant emotion is {response['dominant_emotion']}.")
    return formatted_response
# Route for the homepage (index.html)
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
