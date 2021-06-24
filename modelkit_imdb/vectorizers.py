from typing import List

import modelkit
import numpy as np


class Vectorizer(modelkit.Model[List[str], List[int]]):
    CONFIGURATIONS = {
        "imdb_vectorizer": {"asset": "imdb/vectorizer:0.0[/vocabulary.txt]"}
    }
    TEST_CASES = [
        {"item": [], "result": []},
        {"item": [], "keyword_args": {"length": 10}, "result": [0] * 10},
        {"item": ["movie"], "result": [888]},
        {"item": ["unknown_token"], "result": []},
        {
            "item": ["unknown_token"],
            "keyword_args": {"drop_oov": False},
            "result": [1],
        },
        {"item": ["movie", "unknown_token", "scenes"], "result": [888, 1156]},
        {
            "item": ["movie", "unknown_token", "scenes"],
            "keyword_args": {"drop_oov": False},
            "result": [888, 1, 1156],
        },
        {
            "item": ["movie", "unknown_token", "scenes"],
            "keyword_args": {"length": 10},
            "result": [888, 1156, 0, 0, 0, 0, 0, 0, 0, 0],
        },
        {
            "item": ["movie", "unknown_token", "scenes"],
            "keyword_args": {"length": 10, "drop_oov": False},
            "result": [888, 1, 1156, 0, 0, 0, 0, 0, 0, 0],
        },
    ]

    def _load(self):
        self.vocabulary = {}
        with open(self.asset_path, "r", encoding="utf-8") as f:
            for i, k in enumerate(f):
                self.vocabulary[k.strip()] = i + 2
        self._vectorizer = np.vectorize(lambda x: self.vocabulary.get(x, 1))

    def _predict(self, tokens, length=None, drop_oov=True):
        vectorized = (
            np.array(self._vectorizer(tokens), dtype=np.int)
            if tokens
            else np.array([], dtype=int)
        )
        if drop_oov and len(vectorized):
            vectorized = np.delete(vectorized, vectorized == 1)
        if not length:
            return vectorized.tolist()
        result = np.zeros(length)
        vectorized = vectorized[:length]
        result[: len(vectorized)] = vectorized
        return result.tolist()
