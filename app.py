from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

model = load_model(r'C:\Users\alibe\OneDrive\Desktop\chatapp\NLP_Project-2024_US_Election_Sentiment_on_X\models\my_model2_candidate_prediction (1).h5')
secmodel = load_model(r'C:\Users\alibe\OneDrive\Desktop\chatapp\NLP_Project-2024_US_Election_Sentiment_on_X\models\my_model2_sentiment_prediction.h5')

app = Flask(__name__)

def processing(text):
    # Use the correct max_len for both models (assuming both use the same)
    max_len = text.shape[1]

    new_seq = tokenizer.texts_to_sequences([text])
    new_padded = pad_sequences(new_seq, maxlen=max_len, padding='post')

    # Predict party
    party_pred = model.predict(new_padded)
    party_class = np.argmax(party_pred, axis=1)[0]

    party_names = {
        0: "Kamala Harris : Democratic Party",
        1: "Jill Stein : Green Party",
        2: "Robert Kennedy Jr. : Independent",
        3: "Chase Oliver : Libertarian Party",
        4: "Donald Trump : Republican Party"
    }
    party_result = party_names.get(party_class, 'Unknown')

    # Predict sentiment
    sentiment_pred = secmodel.predict(new_padded)
    sentiment_class = np.argmax(sentiment_pred, axis=1)[0]
    sentiment_names = {
        0: "negative",
        1: "neutral",
        2: "positive"
    }
    sentiment_result = sentiment_names.get(sentiment_class, 'Unknown')

    return party_result, sentiment_result

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    party = None
    keyword = None
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        if keyword:
            party, sentiment = processing(keyword)
    return render_template('index.html', sentiment=sentiment, party=party, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)