---
aid: microsoft-sentinel
name: Microsoft Sentinel
description: Microsoft Sentinel is a cloud-native security information and event management (SIEM) and security orchestration, automation, and response (SOAR) solution. It provides REST APIs for managing incidents, analytics rules, threat intelligence, and automation playbooks.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Microsoft
  - Security
  - SIEM
  - SOAR
  - Threat Detection
url: https://raw.githubusercontent.com/api-evangelist/microsoft-sentinel/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-sentinel:rest-api
    name: Microsoft Sentinel REST API
    tags:
      - Security
      - SIEM
      - SOAR
      - Threat Detection
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/securityinsights/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/securityinsights/
        type: Documentation
      - url: https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard
        type: Getting Started
    description: The Microsoft Sentinel REST API provides programmatic access to security incident management, threat intelligence, watchlists, analytics rules, and automation playbooks. Developers can manage incidents, configure data connectors, create custom detection rules, and automate security response workflows through Azure Resource Manager endpoints.
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Website
    url: https://azure.microsoft.com/en-us/products/microsoft-sentinel/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/sentinel/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/microsoft-sentinel/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/sentinel/quickstart-onboard
  - type: Authentication
    url: https://learn.microsoft.com/en-us/azure/active-directory/develop/
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Status
    url: https://status.azure.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
