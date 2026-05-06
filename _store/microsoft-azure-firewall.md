---
aid: microsoft-azure-firewall
name: Azure Firewall
description: Azure Firewall is a managed cloud-based network security service that protects your Azure Virtual Network resources. The REST API supports configuring network rules, application rules, NAT rules, and DNS proxy settings, with built-in high availability, unrestricted cloud scalability, and threat intelligence-based filtering.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Security
  - Firewall
  - Network Security
  - Threat Protection
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-firewall/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-firewall:rest-api
    name: Azure Firewall REST API
    tags:
      - Cloud Security
      - Firewall
      - Network Security
      - Threat Protection
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/firewall/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/firewall/
        type: Documentation
    description: Azure Firewall REST API provides management of cloud-native network security with built-in high availability, unrestricted cloud scalability, and threat intelligence-based filtering. It supports configuring network rules, application rules, NAT rules, and DNS proxy settings.
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
