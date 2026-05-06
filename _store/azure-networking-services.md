---
aid: azure-networking-services
name: Azure Networking Services
description: A comprehensive collection of Azure networking APIs for managing virtual networks, load balancers, application gateways, VPN gateways, DNS, and other networking resources in the Microsoft Azure cloud.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Azure
  - Cloud
  - Infrastructure
  - Microsoft
  - Networking
url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
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
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/openapi/azure-networking-services-virtual-network-openapi.yaml
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/openapi/azure-networking-services-load-balancer-openapi.yaml
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
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/openapi/azure-networking-services-virtual-network-openapi.yaml
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/openapi/azure-networking-services-load-balancer-openapi.yaml
common:
  - type: Portal
    url: https://portal.azure.com
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/networking/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/networking/
  - type: Authentication
    url: https://learn.microsoft.com/en-us/rest/api/azure/
  - type: Status
    url: https://status.azure.com/
  - type: Support
    url: https://azure.microsoft.com/en-us/support/
  - type: Terms of Service
    url: https://azure.microsoft.com/en-us/support/legal/
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/rules/azure-networking-services-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/vocabulary/azure-networking-services-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/json-ld/azure-networking-services-context.jsonld
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/capabilities/azure-networking-services-management.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/azure-networking-services/refs/heads/main/capabilities/shared/azure-networking-services.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
