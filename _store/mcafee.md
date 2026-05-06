---
aid: mcafee
name: McAfee (Trellix)
description: APIs for McAfee Enterprise security products and services. McAfee Enterprise rebranded as Trellix in 2022, but its on-premises and SaaS platforms (ePO, MVISION, ESM, Web Gateway, TIE, DXL) continue to expose REST APIs documented here for centralized security management, threat intelligence, EDR, messaging, and SIEM integration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/mcafee/refs/heads/main/apis.yml
created: '2024-01-20'
modified: '2026-04-28'
specificationVersion: '0.20'
tags:
  - Antivirus
  - Cybersecurity
  - Endpoint Protection
  - Security
  - Threat Intelligence
apis:
  - aid: mcafee:mcafee-epo-api
    name: McAfee ePO API
    description: McAfee ePolicy Orchestrator (ePO) REST API for centralized security management, including system management, policy assignment, task scheduling, query execution, and threat event retrieval across managed endpoints.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.trellix.com/products/epo/
    baseURL: https://your-epo-server:8443/remote
    tags:
      - Endpoint Management
      - Policy Orchestrator
      - Security Management
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/epolicy-orchestrator-web-api-reference-guide
      - type: Authentication
        url: https://docs.trellix.com/bundle/epolicy-orchestrator-web-api-reference-guide
      - type: OpenAPI
        url: openapi/mcafee-epo-openapi.yml
  - aid: mcafee:mcafee-mvision-api
    name: McAfee MVISION API
    description: Cloud-native security platform API for endpoint detection and response (EDR), threat prevention, device management, and incident investigation.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.trellix.com/
    baseURL: https://api.mvision.mcafee.com
    tags:
      - Cloud Security
      - EDR
      - MVISION
      - Threat Detection
    properties:
      - type: Documentation
        url: https://developer.mcafee.com/
      - type: OpenAPI
        url: openapi/mcafee-mvision-openapi.yml
  - aid: mcafee:mcafee-tie-api
    name: McAfee Threat Intelligence Exchange (TIE) API
    description: Real-time threat intelligence sharing and reputation services API.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.trellix.com/
    baseURL: https://your-tie-server/api
    tags:
      - Malware Analysis
      - Reputation
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://opendxl.github.io/opendxl-tie-client-python/
      - type: SDK
        url: https://github.com/opendxl/opendxl-tie-client-python
  - aid: mcafee:mcafee-dxl-api
    name: McAfee Data Exchange Layer (DXL) API
    description: Messaging fabric for real-time security data exchange and integration.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.trellix.com/
    baseURL: https://your-dxl-broker
    tags:
      - Data Exchange
      - Fabric
      - Integration
      - Messaging
    properties:
      - type: Documentation
        url: https://opendxl.github.io/opendxl-client-python/
      - type: GitHub
        url: https://github.com/opendxl
      - type: SDK - Python
        url: https://github.com/opendxl/opendxl-client-python
      - type: SDK - JavaScript
        url: https://github.com/opendxl/opendxl-client-javascript
  - aid: mcafee:mcafee-web-gateway-api
    name: McAfee Web Gateway API
    description: Web security gateway REST API for managing rule sets, URL filtering lists, SSL inspection settings, and monitoring proxy traffic and appliance health.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.trellix.com/
    baseURL: https://your-mwg-server/Konfigurator/REST
    tags:
      - Proxy
      - Web Gateway
      - Web Security
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/web-gateway-product-guide
      - type: OpenAPI
        url: openapi/mcafee-web-gateway-openapi.yml
  - aid: mcafee:mcafee-esm-api
    name: McAfee ESM API
    description: Enterprise Security Manager SIEM REST API for managing security events, alarms, watchlists, data sources, cases, and executing queries against the event database.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.trellix.com/
    baseURL: https://your-esm-server/rs/esm
    tags:
      - Log Management
      - Security Events
      - SIEM
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/enterprise-security-manager-api-reference-guide
      - type: OpenAPI
        url: openapi/mcafee-esm-openapi.yml
common:
  - type: Developer Portal
    url: https://developer.mcafee.com
  - type: Website
    url: https://www.trellix.com/
  - type: Support
    url: https://www.trellix.com/support/
  - type: Terms of Service
    url: https://www.trellix.com/about/legal/
  - type: Privacy Policy
    url: https://www.trellix.com/about/legal/privacy/
  - type: JSON-LD
    url: json-ld/mcafee-context.jsonld
  - type: JSONSchema
    url: json-schema/mcafee-threat-event-schema.json
  - type: JSONSchema
    url: json-schema/mcafee-endpoint-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
