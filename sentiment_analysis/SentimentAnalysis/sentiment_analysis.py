import requests,json

# BERT based Sentiment Analysis function of the Watson NLP Library.
def sentiment_analyzer(text_to_analyze):
    # if not text_to_analyze:
    #     return "Input text cannot be blank"
        
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label': label, 'score': score}

    