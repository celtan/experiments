#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformOutput, Token
from imports.azurerm import AzurermProvider, ResourceGroup, VirtualNetwork, StorageAccount, StorageAccountConfig

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, ns: str):
        super().__init__(scope, ns)
        # define resources here
        self.location="eastus2"
        self.add_space=["10.12.0.0/27"]
        self.rg_name="storage_rg"
        self.storage_vnet_name="storage_vnet"
        self.storage_account_name="storagev2terraformback"
                
        self.tag = {
                "ENV": "Dev",
                "PROJECT": "AZ_TF"
            }
        
        AzurermProvider(self, "Azurerm",\
            features=[{}]
            )

        storage_rg = ResourceGroup(self, self.rg_name,\
            name=self.rg_name, 
            location = self.location,
            tags = self.tag
            )

        storage_vnet = VirtualNetwork(self, self.storage_vnet_name,\
            depends_on =[storage_rg],
            name=self.storage_vnet_name,
            location=self.location,
            address_space=self.add_space,
            resource_group_name=Token().as_string(storage_rg.name),
            tags = self.tag
            )
        storage_account = StorageAccount(self, self.storage_account_name, \
            depends_on=[storage_vnet],
            resource_group_name=storage_rg.name,
            location=self.location,
            account_kind="StorageV2",
            access_tier="Hot",
            account_replication_type="LRS",
            name=self.storage_account_name,
            account_tier="Standard"
            tags=self.tags,
            min_tls_version="TLS1_2",
            network_rules="None"
            )

        TerraformOutput(self, 'vnet_id',
            value=storage_vnet.id
        )
        
        TerraformOutput(self, 'resource_group_name',
            value=storage_rg.name
        )

        TerraformOutput(self, 'storage_account_id',
            value=storage_account.id
        )

app = App()
MyStack(app, "storage-stack")

app.synth()
