FROM alpine:3.14.3 


ARG TERRAFORM_VERSION=1.0.11
ENV SYSTEM_USR_PATH="/usr/local/bin" \
    AZ_PATH="/usr/bin"
ENV USER=agent
ENV UID=12345
ENV GID=12345

ENV PATH="$SYSTEM_USR_PATH:$PATH"

RUN apk add --no-cache --virtual .pipeline-deps readline linux-pam \
  && apk add --no-cache bash curl unzip\
  && apk del .pipeline-deps


# Install Terraform
RUN addgroup -S agent -g "$GID"\
  && adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "$USER" \
    --no-create-home \
    --uid "$UID" \
    "$USER"
 
RUN echo "===> Installing Terraform ${TERRAFORM_VERSION}..." \
 && curl https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip -o terraform_${TERRAFORM_VERSION}_linux_amd64.zip\
 &&	unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip \
 && mv terraform /usr/local/bin/terraform \
 && rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

USER agent
WORKDIR /agent