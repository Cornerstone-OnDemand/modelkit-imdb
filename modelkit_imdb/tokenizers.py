import typing

import modelkit
import spacy


class Tokenizer(modelkit.Model[str, typing.List[str]]):
    CONFIGURATIONS: typing.Dict[str, typing.Dict] = {"imdb_tokenizer": {}}
    TEST_CASES = [
        {"item": "", "result": []},
        {"item": "NLP 101", "result": ["nlp"]},
        {
            "item": "I'm loving the spaCy 101 course !!!ù*`^@😀",
            "result": ["loving", "spacy", "course"],
        },
        {
            "item": "<br/>prepare things for IMDB<br/>",
            "result": ["prepare", "things", "imdb"],
        },
        {
            "item": "<br/>a b c data<br/>      e scientist",
            "result": ["data", "scientist"],
        },
    ]

    def _load(self):
        self.nlp = spacy.load(
            "en_core_web_sm",
            disable=[
                "parser",
                "ner",
                "tagger",
                "lemmatizer",
                "tok2vec",
                "attribute_ruler",
            ],
        )

    def _predict_batch(self, texts):
        texts = [
            " ".join(text.replace("<br", "").replace("/>", "").split())
            for text in texts
        ]
        return [
            [
                t.lower_
                for t in text
                if t.is_ascii
                and len(t) > 1
                and not (t.is_punct or t.is_stop or t.is_digit)
            ]
            for text in self.nlp.pipe(texts, batch_size=len(texts))
        ]
