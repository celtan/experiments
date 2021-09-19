
- [Experiments](#experiments)
  - [cdktf](#cdktf)
    - [Sub-heading](#sub-heading)
      - [Sub-sub-heading](#sub-sub-heading)
  - [Heading](#heading)
    - [Sub-heading](#sub-heading-1)
      - [Sub-sub-heading](#sub-sub-heading-1)
  - [Heading](#heading-1)
    - [Sub-heading](#sub-heading-2)
      - [Sub-sub-heading](#sub-sub-heading-2)


# Experiments

> This repository contains experimental examples of how-tos and notes for whatever catches my interest

<!-- toc -->

## [cdktf](cdktf)

Main Reference Links:
- [CDK for Terraform](https://github.com/hashicorp/terraform-cdk) 
- [modules](https://github.com/hashicorp/terraform-cdk/docs/working-with-cdk-for-terraform/using-modules.md)
- [providers](https://github.com/hashicorp/terraform-cdk/docs/working-with-cdk-for-terraform/using-providers.md) 
- [functions](./docs/working-with-cdk-for-terraform/terraform-functions.md) 
- [synthesizes](./docs/working-with-cdk-for-terraform/synthesizing-config.md) 
- [python-examples](https://github.com/hashicorp/terraform-cdk/examples/python)
- Install and run a quick start tutorial at [HashiCorp Learn](https://learn.hashicorp.com/terraform/cdktf/cdktf-install

Experimentation: 
- [cdk/azure](cdktf/azure) contains some samples for creating resources in python for azure

```bash
# install 
brew install cdktf

# usage
mkdir <new-directory-for-new-project>
cd <new-directory-for-new-project>

# create a new project
cdktf init --template="python-pip" --local

# update the cdktf.json to add the azure providers that will be needed.  Note these are the 
# same providers and versions used in HCL
# for example for azurerm

# cdktf.json
{
  "language": "python",
  "app": "python3 ./main.py",
  "projectId": "7f8da6a9-b9ec-4abc-a7c2-16ddb6f8ee92",
  "terraformProviders": [
    "azurerm@~> 2.75.0"
  ],
  "terraformModules": [],
  "codeMakerOutput": "imports",
  "context": {
    "excludeStackIdFromLogicalIds": "true",
"allowSepCharsInLogicalIds": "true"
  }
}

# python env set up if required
virtualenv -p python3.8 venv
source venv/bin/activate

# deactivate
deactivate

# get providers, modules and api tokens etc
cdktf get

# synthesizes terraform code for the given app to a directory
cdktf synth

# deploy
cdktf deploy

# difference (==terraform plan)
cdktf diff

# list
cdktf list

# destroy 
cdktf destroy

# help
cdktf help

```
