# 🗳️ Political Party & Sentiment Prediction with LSTM 🧠

Welcome to the Political Party and Sentiment Prediction project!  
This repository contains code and models to classify political orientation and sentiment from tweets using deep learning (LSTM/BiLSTM) in TensorFlow/Keras.

---

## 📦 Project Structure

- `LSTM.ipynb` — Main Jupyter notebook with all data processing, model training, and prediction code.
- `Data/` — Folder containing training, validation, and test CSVs for party classification.
- `tweet-sentiment-extraction-data/` — Sentiment dataset (train/test CSVs).
- `models/` — Saved Keras models for party and sentiment prediction.

---

## 🚀 Features

- **Party Prediction:**  
  Classifies tweets into one of five US political parties:
  - Kamala Harris : Democratic Party
  - Jill Stein : Green Party
  - Robert Kennedy Jr. : Independent
  - Chase Oliver : Libertarian Party
  - Donald Trump : Republican Party

- **Sentiment Analysis:**  
  Classifies tweets as:
  - Positive 😊
  - Neutral 😐
  - Negative 😠

- **Interactive Prediction:**  
  Enter a tweet and get both the predicted political orientation and sentiment!

---

## 🛠️ Requirements

- Python 3.8+
- TensorFlow / Keras
- scikit-learn
- pandas, numpy, matplotlib, seaborn

Install requirements:
```bash
pip install tensorflow scikit-learn pandas numpy matplotlib seaborn
```

---

## 📊 How It Works

1. **Data Preprocessing:**  
   - Tokenization and padding of tweets.
   - Label encoding and one-hot encoding for both party and sentiment.

2. **Model Training:**  
   - LSTM for party prediction.
   - BiLSTM for sentiment analysis.

3. **Evaluation:**  
   - Confusion matrix, accuracy, and classification report for both tasks.

4. **Prediction:**  
   - Enter your own tweet and see the predicted party and sentiment.

---

## 📝 Example Usage

```python
new_tweet = input('Give a new tweet: ')
# ...see notebook for full prediction code...
```

**Example Output:**
```
Predicted political orientation: Donald Trump : Republican Party
Party prediction probabilities: [[0.01 0.01 0.01 0.01 0.96]]
Predicted sentiment (mapped): positive
Sentiment prediction probabilities: [[0.02 0.05 0.93]]
```

---

## 💡 Sample Tweets

- "Trump is the best president we ever had."
- "Kamala Harris is a strong and inspiring leader."
- "Green Party offers the best solutions for climate change."
- "Robert Kennedy Jr. is bringing a fresh perspective."
- "Libertarian ideals are what Chase Oliver stands for."

---

## 📈 Results

- Confusion matrices and classification reports are generated for both tasks.
- Visualizations with seaborn heatmaps.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📄 License

MIT License

---

## ✨ Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [scikit-learn](https://scikit-learn.org/)
- [Kaggle Sentiment Dataset](https://www.kaggle.com/competitions/tweet-sentiment-extraction/data)

---

Enjoy exploring political and sentiment analysis with deep learning! 🚀
