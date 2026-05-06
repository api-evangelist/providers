---
aid: microsoft-azure-front-door
name: Azure Front Door
description: Azure Front Door Service enables you to define, manage, and monitor the global routing for your web traffic. The REST API supports configuring routing rules, backend pools, health probes, caching policies, and WAF rules for secure and performant application delivery at the edge.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CDN
  - Edge
  - Global Routing
  - Load Balancing
  - WAF
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-front-door/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: microsoft-azure-front-door:rest-api
    name: Azure Front Door REST API
    tags:
      - CDN
      - Edge
      - Global Routing
      - Load Balancing
      - WAF
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://management.azure.com/
    humanURL: https://learn.microsoft.com/en-us/rest/api/frontdoor/
    properties:
      - url: https://learn.microsoft.com/en-us/rest/api/frontdoor/
        type: Documentation
    description: Azure Front Door REST API provides management of global load balancing and web application firewall services. It supports configuring routing rules, backend pools, health probes, caching policies, and WAF rules for secure and performant application delivery.
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
