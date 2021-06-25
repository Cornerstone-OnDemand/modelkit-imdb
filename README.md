<p align="center">
  <a href="https://github.com/clustree/modelkit">
    <img src="https://raw.githubusercontent.com/clustree/modelkit/main/.github/resources/logo.svg" alt="Logo" width="80" height="80" />
</a><span style="font-size:30px; margin: 0px 20px 0px 10px; padding-bottom: 100px">x</span>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/IMDB_Logo_2016.svg" width="100" height="80"/>
</p>

<h1 align="center">How to deploy a NLP pipeline</h1>
<h3 align="center">leveraging <a href="https://github.com/clustree/modelkit">modelkit</a> and the IMDB reviews dataset</h3>

<h4 align="center">
  <em>Features Covered: Project Organization, CI, Assets Management, CLIs, REST API Serving</em>
</h4>

---

<p align="center">
  <a href="https://github.com/clustree/modelkit-imdb/actions?query=branch%3Amain+"><img src="https://img.shields.io/github/workflow/status/clustree/modelkit-imdb/CI/main" /></a>
  <a href="https://github.com/clustree/modelkit-imdb/actions/workflows/main.yml?query=branch%3Amain+"><img src="docs/badges/tests.svg" /></a>
  <a href="https://clustree.github.io/modelkit-imdb/coverage/index.html"><img src="docs/badges/coverage.svg" /></a>
<img src="https://img.shields.io/static/v1?label=python&message=3.7&color=blue" />
  <a href="https://github.com/clustree/modelkit-imdb/blob/main/LICENSE"><img src="https://img.shields.io/github/license/clustree/modelkit-imdb" /></a>
</p>

This sample project aims at illustrating modelkit's powerful features, based on the documentation tutorial: [NLP x Sentiment Analysis](https://clustree.github.io/modelkit/examples/nlp_sentiment/intro.html).

It also serves as a sandbox for any developer willing to try out modelkit in _real conditions_, from the package organization to the Github CI and through the use of CLIs and HTTP serving.

## Installation

First, please `source .env` or run the following:

```bash
export MODELKIT_ASSETS_DIR=.local_storage
export MODELKIT_STORAGE_BUCKET=.
export MODELKIT_STORAGE_PREFIX=.remote_storage
export MODELKIT_STORAGE_PROVIDER=local
export MODELKIT_DEFAULT_PACKAGE=modelkit_imdb  # shortcut for CLIs
```

Once done, let's create a new python virtual environment and install the dev requirements:

```bash
pip install -r requirements-dev.txt
```

## Describe

Before going further, let's remind us of the models that are available in the `modelkit_imdb` package with the following CLI:

```
modelkit describe
```

<img src=".github/resources/describe.gif" style="margin: 20px" />

## REST API serving

The following CLI will start a single worker which will expose all the models found under the `modelkit_imdb` package leveraging `uvicorn` and `FastAPI`:

```
modelkit serve
```

Voilà: the `uvicorn` worker is now running at `http://localhost:8000`.

Check out the generated `SwaggerUI` at http://localhost:8000/docs to see all the endpoints and try them out:

<img src=".github/resources/swagger.gif" alt="modelkit swagger" style="margin: 20px">

You can also `POST` your request on the endpoint of your choice:

```bash
curl -X 'POST' \
  'http://localhost:8000/predict/imdb_classifier' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "This movie sucks! It is the worst I have ever seen in my entire life"
}'
# {"label":"bad","score": 0.1530771553516388}
```
