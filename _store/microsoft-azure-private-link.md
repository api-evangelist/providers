---
aid: microsoft-azure-private-link
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-private-link/refs/heads/main/apis.yml
apis:
  - aid: microsoft-azure-private-link:rest-api
    name: Azure Private Link REST API
    tags:
      - Network Security
      - Private Endpoint
      - Private Link
      - VNet
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/privatelink/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/privatelink/
        type: Documentation
    description: Azure Private Link REST API provides management of private endpoints and private link services for accessing Azure PaaS services over private IP addresses within virtual networks, eliminating exposure to the public internet.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
modified: '2026-04-28'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
description: Microsoft Azure Private Link enables access to Azure PaaS services and Azure-hosted customer-owned services over a private endpoint in a virtual network, eliminating exposure to the public internet.
---
