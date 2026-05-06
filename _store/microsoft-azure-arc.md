---
aid: microsoft-azure-arc
name: Azure Arc
description: Operation groups for the Hybrid Compute REST API.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-arc/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
tags:
  - Arc
  - Hybrid Cloud
  - Kubernetes
  - Multi-Cloud
  - Server Management
apis:
  - aid: microsoft-azure-arc:rest-api
    name: Azure Arc REST API
    tags:
      - Arc
      - Hybrid Cloud
      - Kubernetes
      - Multi-Cloud
      - Server Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/hybridcompute/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/hybridcompute/
        type: Documentation
    description: Azure Arc REST API enables management of servers, Kubernetes clusters, and data services running outside Azure. It supports onboarding hybrid resources, applying Azure policies, enabling monitoring, and extending Azure management capabilities to on-premises and multi-cloud environments.
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
