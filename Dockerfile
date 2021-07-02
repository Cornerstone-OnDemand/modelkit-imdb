FROM python:3.7-slim-buster

SHELL ["/bin/bash", "-c"]

ENV HOME=/opt/modelkit-imdb \
    USER=modelkit-imdb \
    MODELKIT_ASSETS_DIR=.local_storage \
    MODELKIT_DEFAULT_PACKAGE=modelkit_imdb
    # the following are commented since not useful in this context:
    # the assets are already present in .local_storage
    # MODELKIT_STORAGE_BUCKET=. \
    # MODELKIT_STORAGE_PREFIX=.remote_storage \
    # MODELKIT_STORAGE_PROVIDER=local \

RUN apt-get -qqy update && \
    apt-get -qqy dist-upgrade && \
    apt-get autoremove -qqy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/* /usr/share/man

RUN groupadd -r ${USER} && \
    useradd -g ${USER} -M -r -d ${HOME} ${USER}

ADD modelkit_imdb ${HOME}/modelkit_imdb
ADD .remote_storage ${HOME}/.remote_storage
ADD requirements.txt ${HOME}

RUN mkdir -p ${HOME}/.local_storage && \
    chmod -R u+rX ${HOME} && \
    chown -R ${USER} ${HOME}

USER ${USER}

WORKDIR ${HOME}

RUN python3 -m venv --copies ${HOME} && \
    source ${HOME}/bin/activate && \
    pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -q -r ${HOME}/requirements.txt && \
    pip3 install --no-cache-dir fastapi uvicorn gunicorn

ENV PATH=${PATH}:${HOME}/bin/

# EXPOSE 8000
# commented since not used by Heroku

# using uvicorn
CMD modelkit serve --host 0.0.0.0 --port ${PORT}
# using gunicorn
# CMD gunicorn --workers 4 --bind 0.0.0.0:${PORT} --preload --worker-class=uvicorn.workers.UvicornWorker 'modelkit.api:create_modelkit_app(None)'
