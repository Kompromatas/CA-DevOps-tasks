#! /bin/bash    

GROUP='ca-devops-1'
LOCATION='eastus'
IMAGE='Canonical:ubuntu-24_04-lts:server:latest'
SIZE='Standard_B1s'

az storage account create --name storageacc181 --resource-group $GROUP --location $LOCATION --sku Standard_LRS

az storage container create --name blob18 --account-name storageacc181

az network nsg create --resource-group $GROUP --name nsg18

az network nsg rule create --resource-group $GROUP --nsg-name nsg18 --name allow-SSH --protocol Tcp --priority 102 --destination-port-range 22 --access Allow --direction Inbound --source-address-prefix '*' --source-port-range '*' --destination-address-prefix '*'

az vm create \
  --resource-group $GROUP \
  --name 'vm-devops-18-2' \
  --image $IMAGE \
  --admin-username 'adm_darius' \
  --generate-ssh-keys \
  --location $LOCATION \
  --size $SIZE \
  --nsg nsg18  

az storage blob upload --account-name storageacc181 --container-name blob18 --file ./1.sh --name azure-1.sh

