---
aid: azure-networking-services
url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/apis.yml
apis:
- aid: azure-networking-services:azure-virtual-networks-api
  name: Azure Virtual Networks API
  description: API for creating and managing Azure Virtual Networks (VNets), subnets, and network peering.
  humanURL: https://azure.microsoft.com/en-us/services/virtual-network/
  baseURL: https://management.azure.com
  tags:
  - Networking
  - Subnets
  - Virtual Network
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/virtual-network/
- aid: azure-networking-services:azure-load-balancer-api
  name: Azure Load Balancer API
  description: API for managing Azure Load Balancers for distributing network traffic.
  humanURL: https://azure.microsoft.com/en-us/services/load-balancer/
  baseURL: https://management.azure.com
  tags:
  - Load Balancer
  - Networking
  - Traffic Distribution
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/rest/api/load-balancer/
name: Azure Networking Services
tags:
- Azure
- Cloud
- Infrastructure
- Microsoft
- Networking
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: A comprehensive collection of Azure networking APIs for managing virtual networks, load balancers, application gateways, VPN gateways, DNS, and other networking resources in the Microsoft Azure cloud.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

