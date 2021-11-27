FROM python:3.8.12-slim-bullseye AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/agent/.venv" \
    SYSTEM_USR_PATH="/usr/local/bin" \
    AZ_PATH="/usr/bin" \
    WORKDIR=/agent \
    POETRY_VERSION=1.1.10 \
    TERRAFORM_VERSION=0.13.7

RUN mkdir -p ${WORKDIR}
WORKDIR ${WORKDIR}
RUN apt-get update \
    && apt-get -y install curl unzip jq git vim\ 
    && rm -rf /var/lib/apt/lists/*

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$TERRAFORM_PATH:$PATH"

FROM base AS builder

RUN apt-get update \
    && apt-get -f -y install lsb-release gnupg \ 
    && curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.asc.gpg && \
    CLI_REPO=$(lsb_release -cs) \
    && echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ ${CLI_REPO} main" \
    > /etc/apt/sources.list.d/azure-cli.list \
    && apt-get update \
    && apt-get install -y azure-cli=2.29.2-1~bullseye\ 
    && rm -rf /var/lib/apt/lists/*

COPY ./pyproject.toml ./

# Install Terraform
RUN curl -ssL https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip\
 &&	unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && mv terraform ${SYSTEM_USR_PATH}/terraform \
 && rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Install jfrog
RUN curl -fL https://getcli.jfrog.io|sh \
    && chmod +x jfrog \
    && mv jfrog /usr/bin/jfrog

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -

FROM builder AS agent

WORKDIR ${WORKDIR}

COPY --from=builder ${POETRY_HOME} ${POETRY_HOME}
COPY --from=builder /usr/bin/az /usr/bin/az
COPY --from=builder /usr/local/bin/terraform /usr/local/bin/terraform

# RUN poetry install --no-dev  
# RUN . /agent/.venv/bin/activate