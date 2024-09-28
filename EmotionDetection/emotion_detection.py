import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check if the input text is empty or just whitespace
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        # Convert response to a dictionary
        emotions = response.json()
        emotion_scores = emotions['emotionPredictions'][0]['emotion']

        # Extracting required emotions
        anger_score = emotion_scores.get('anger', 0)
        disgust_score = emotion_scores.get('disgust', 0)
        fear_score = emotion_scores.get('fear', 0)
        joy_score = emotion_scores.get('joy', 0)
        sadness_score = emotion_scores.get('sadness', 0)

        # Find the dominant emotion
        emotion_dict = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)

        # Return the formatted output
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        # If the server returns an error, return None for all emotions
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }