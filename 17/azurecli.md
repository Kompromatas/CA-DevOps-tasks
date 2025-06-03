# Azure CLI Basic Usage

The Azure Command-Line Interface (Azure CLI) is a set of commands used to create and manage Azure resources.

## Installation

See the official docs:  
https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

## Login

```sh
az login
```

## List Subscriptions

```sh
az account list --output table
```

## Set Subscription

```sh
az account set --subscription "<subscription-name-or-id>"
```

## List Resource Groups

```sh
az group list --output table
```

## Create a Resource Group

```sh
az group create --name MyResourceGroup --location eastus
```

## Create a Virtual Machine

```sh
az vm create \
    --resource-group MyResourceGroup \
    --name MyVM \
    --image UbuntuLTS \
    --admin-username azureuser \
    --generate-ssh-keys
```

## Delete a Resource Group

```sh
az group delete --name MyResourceGroup
```

## Get Help

```sh
az --help
az <command> --help
```

For more details, visit the [Azure CLI documentation](https://docs.microsoft.com/en-us/cli/azure/).