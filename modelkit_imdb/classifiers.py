from typing import Optional

import modelkit
import pydantic
import tensorflow as tf


class MovieReviewItem(pydantic.BaseModel):
    text: str
    rating: Optional[float] = None  # could be useful in the future ? but not mandatory


class MovieSentimentItem(pydantic.BaseModel):
    label: str
    score: float


class Classifier(modelkit.Model[MovieReviewItem, MovieSentimentItem]):
    CONFIGURATIONS = {
        "imdb_classifier": {
            "asset": "imdb/classifier:0.0[/model.h5]",
            "model_dependencies": {
                "tokenizer": "imdb_tokenizer",
                "vectorizer": "imdb_vectorizer",
            },
        },
    }
    TEST_CASES = [
        {
            "item": {"text": "i love this film, it's the best I've ever seen"},
            "result": {"score": 0.8402805328369141, "label": "good"},
        },
        {
            "item": {"text": "this movie sucks, it's the worst I have ever seen"},
            "result": {"score": 0.159115731716156, "label": "bad"},
        },
    ]

    def _load(self):
        self.model = tf.keras.models.load_model(
            self.asset_path, custom_objects={"tf": tf}
        )
        self.tokenizer = self.model_dependencies["tokenizer"]
        self.vectorizer = self.model_dependencies["vectorizer"]

    def _predict_batch(self, reviews):
        texts = [review.text for review in reviews]
        tokenized_reviews = self.tokenizer.predict_batch(texts)
        vectorized_reviews = self.vectorizer.predict_batch(tokenized_reviews, length=64)
        predictions_scores = self.model.predict(vectorized_reviews)
        predictions = [
            {"score": score, "label": "good" if score >= 0.5 else "bad"}
            for score in predictions_scores
        ]
        return predictions
