"""This module contains the Flask server for the Emotion Detector application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emo_detector():
    ''' Detects emotions in the given text and returns the system response.
    Returns:
        str: A formatted string indicating the system response to the given statement.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    # emotions = response['emotionPredictions'][0]['emotion']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    formatted_response = "For the given statement, the system response is "
    for key, value in response.items():
        if key != "dominant_emotion":
            formatted_response += f"'{key}': {value}, "
        else:
            formatted_response += f"and '{key}' is {value}."
    formatted_response = formatted_response.rstrip(", ")

    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
