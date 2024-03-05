import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # can try multi language
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
    elif response.status_code == 400:
        emotions = None
        dominant_emotion = None

    if emotions is not None:
        return {
            "anger": emotions.get('anger', 0),
            "disgust": emotions.get('disgust', 0),
            "fear": emotions.get('fear', 0),
            "joy": emotions.get('joy', 0),
            "sadness": emotions.get('sadness', 0),
            "dominant_emotion": dominant_emotion
        }
    else:
        return {
            "anger": 0,
            "disgust": 0,
            "fear": 0,
            "joy": 0,
            "sadness": 0,
            "dominant_emotion": None
        }