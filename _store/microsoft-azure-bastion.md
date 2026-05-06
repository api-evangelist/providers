---
aid: microsoft-azure-bastion
name: Azure Bastion
description: Learn more about [Virtual Networks Bastion Hosts Operations]. How to [Create Or Update,Delete,Get,List,List By Resource Group,Update Tags].
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-bastion/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
tags:
  - Bastion
  - RDP
  - Remote Access
  - Secure Access
  - SSH
apis:
  - aid: microsoft-azure-bastion:rest-api
    name: Azure Bastion REST API
    tags:
      - Bastion
      - RDP
      - Remote Access
      - Secure Access
      - SSH
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/bastion-hosts
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/virtualnetwork/bastion-hosts
        type: Documentation
    description: Azure Bastion REST API enables management of fully managed PaaS service for secure RDP and SSH access to virtual machines directly through the Azure portal without exposing public IP addresses.
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
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
