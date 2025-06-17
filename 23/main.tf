provider "azurerm" {
  features {}
  
  subscription_id = "e76bf4c3-a610-4a4a-b695-9c03019cd2a3"

}

resource "azurerm_virtual_network" "vnet" {
    name                = "${var.resource_group_name}-vnet"
    address_space       = ["10.0.0.0/16"]
    location            = var.location
    resource_group_name = var.resource_group_name
  
}

resource "azurerm_subnet" "subnet" {
    name                 = "${var.resource_group_name}-subnet"
    resource_group_name  = var.resource_group_name
    virtual_network_name = azurerm_virtual_network.vnet.name
    address_prefixes     = ["10.0.1.0/24"]
  
}

resource "azurerm_public_ip" "public_ip" {
    name = "${var.resource_group_name}-public-ip"
    location            = var.location
    resource_group_name = var.resource_group_name
    sku = "Basic"
    allocation_method   = "Dynamic"
  
}

resource "azurerm_network_interface" "nic" {
    name                = "${var.resource_group_name}-nic"
    location            = var.location
    resource_group_name = var.resource_group_name
  
    ip_configuration {
        name                          = "internal"
        subnet_id                     = azurerm_subnet.subnet.id
        private_ip_address_allocation = "Dynamic"
        public_ip_address_id          = azurerm_public_ip.public_ip.id
    }
}

resource "azurerm_linux_virtual_machine" "vm" {
    name = "${var.resource_group_name}-vm"
    resource_group_name = var.resource_group_name
    location            = var.location
    size                = "Standard_B1s"
    admin_username      = "adm_darius"
    admin_password      = "P@ssw0rd123"
    disable_password_authentication = false
    network_interface_ids = [azurerm_network_interface.nic.id] 
    os_disk {
        caching              = "ReadWrite"
        storage_account_type = "Standard_LRS"
    }
    source_image_reference {
        publisher = "canonical"
        offer     = "0001-com-ubuntu-server-jammy"
        sku       = "22_04-lts"
        version   = "latest"
    }
}