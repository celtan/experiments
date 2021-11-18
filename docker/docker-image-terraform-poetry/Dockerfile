FROM node:lts-alpine3.14 as agent-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv" \
    SYSTEM_USR_PATH="/usr/local/bin" \
    AZ_PATH="/usr/bin"

ENV USER=agent \
    UID=12345 \
    GID=12345 

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$TERRAFORM_PATH:$PATH"

RUN addgroup -S agent -g "$GID"\
  && adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"

RUN apk add --no-cache --virtual .pipeline-deps readline linux-pam \
  && apk add --no-cache bash python3 shadow curl \
  && apk del .pipeline-deps

LABEL "com.azure.dev.pipelines.agent.handler.node.path"="/usr/local/bin/node"

CMD [ "node" ]

from agent-base as agent-builder

ARG TERRAFORM_VERSION=1.0.11
ENV POETRY_VERSION=1.1.10

RUN apk add --no-cache --virtual .pipeline-deps readline linux-pam \
  && apk add --no-cache bash sudo shadow curl \
                        gcc musl-dev python3 python3-dev py3-pip libffi-dev openssl-dev cargo make \
  && ln -sf python3 /usr/bin/python \
  && apk del .pipeline-deps

# Install Poetry 
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

# Install Terraform
RUN echo "===> Installing Terraform ${TERRAFORM_VERSION}..." \
 && curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip\
 &&	unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && mv terraform ${SYSTEM_USR_PATH}/terraform \
 && rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# We copy our Python requirements here to cache them
# and install only runtime deps using poetry
WORKDIR $PYSETUP_PATH
COPY ./pyproject.toml ./
RUN poetry install --no-dev  # respects 

FROM agent-base as azure-agent-builder

COPY --from=agent-builder $VENV_PATH $VENV_PATH
COPY --from=agent-builder $SYSTEM_USR_PATH/terraform $SYSTEM_USR_PATH/terraform

LABEL "com.azure.dev.pipelines.agent.handler.node.path"="/usr/local/bin/node"

USER agent
WORKDIR /agent

CMD [ "node" ]