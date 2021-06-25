<p align="center">
  <a href="https://github.com/clustree/modelkit">
    <img src="https://raw.githubusercontent.com/clustree/modelkit/main/.github/resources/logo.svg" alt="Logo" width="80" height="80" />
</a><span style="font-size:30px; margin: 0px 20px 0px 10px; padding-bottom: 100px">x</span>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg" width="100" height="80"/>
</p>

<h1 align="center">How to deploy a NLP pipeline</h1>
<h3 align="center">leveraging <a href="https://github.com/clustree/modelkit">modelkit</a> and the IMDB reviews dataset</h3>

---

<h4 align="center">
  <em>Features Covered: Project Organization, CI, Assets Management, CLIs, REST API Serving</em>
</h4>

This sample project aims at illustrating modelkit's powerful features, based on the documentation tutorial: [NLP x Sentiment Analysis](https://clustree.github.io/modelkit/examples/nlp_sentiment/intro.html).

It also serves as a sandbox for any developer willing to try out modelkit in _real conditions_, from the package organization to the Github CI and through the use of CLIs and HTTP serving.



## Installation

First, please `source .env` or run the following: 
```bash
export MODELKIT_ASSETS_DIR=.local_storage
export MODELKIT_STORAGE_BUCKET=.
export MODELKIT_STORAGE_PREFIX=.remote_storage
export MODELKIT_STORAGE_PROVIDER=local
```

Once done, let's create a new python virtual environment and install the dev requirements:
```bash 
pip install -r requirements-dev.txt
```

## Quickstart

...