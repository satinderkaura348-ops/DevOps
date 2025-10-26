terraform {
 required_providers {
  azurerm = {
   source = "hashicorp/azurerm"
   version = "4.50.0"
   }
  aws = {
   source = "hashicorp/aws"
   version = "~> 6.0"
}
     }
       }

provider "aws" {
 region = "ap-southeast-2"
}
