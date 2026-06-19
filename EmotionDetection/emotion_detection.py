import json
import requests


def emotion_detector(text_to_analyze):
    """Invia il testo a Watson NLP e gestisce lo status code 400

    restituendo valori None in caso di input vuoto o non valido.
    """
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=myobj, headers=headers)

    # Gestione specifica dello status code 400 (input vuoto)
    if response.status_code == 400:
        result = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
        return result

    # Elaborazione della risposta corretta (status code 200)
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        emotions = formatted_response["emotionPredictions"][0]["emotion"]

        result = {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": max(emotions, key=emotions.get),
        }
        return result

    return f"Error: {response.status_code}"
