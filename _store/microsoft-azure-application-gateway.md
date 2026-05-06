---
aid: microsoft-azure-application-gateway
name: Azure Application Gateway
description: Learn how the Application Gateway is a Network Service which provides HTTP Load balancing as a Service to Azure customers.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-application-gateway/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
tags:
  - Layer 7
  - Load Balancing
  - Reverse Proxy
  - WAF
apis:
  - aid: microsoft-azure-application-gateway:rest-api
    name: Azure Application Gateway REST API
    tags:
      - Layer 7
      - Load Balancing
      - Reverse Proxy
      - WAF
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/application-gateway/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/application-gateway/
        type: Documentation
    description: Azure Application Gateway REST API enables management of layer-7 load balancers with SSL termination, URL-based routing, multi-site hosting, and web application firewall capabilities for protecting web applications.
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
