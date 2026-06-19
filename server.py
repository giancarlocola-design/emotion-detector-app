from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Inizializzazione dell'applicazione Flask
app = Flask(__name__)


@app.route("/emotionDetector")
def emot_detector():
    """Riceve il testo inviato dall'interfaccia web, lo analizza e gestisce

    la visualizzazione degli errori in caso di input vuoto.
    """
    # Lettura dell'input inviato dal form web (parametro textToAnalyze)
    text_to_analyze = request.args.get("textToAnalyze")

    # Esecuzione dell'analisi delle emozioni
    response = emotion_detector(text_to_analyze)

    # Gestione specifica dell'errore per input vuoto o non valido (quando dominant_emotion è None)
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    # Costruzione del messaggio di output in caso di successo
    output_message = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return output_message


@app.route("/")
def render_index_page():
    """Esegue il rendering della pagina HTML dell'interfaccia utente (index.html)."""
    return render_template("index.html")


if __name__ == "__main__":
    # Esecuzione dell'applicazione sulla porta 5000
    app.run(host="0.0.0.0", port=5000)
