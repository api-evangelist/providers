---
aid: mcafee
url: https://raw.githubusercontent.com/api-evangelist/mcafee/refs/heads/main/apis.yml
apis:
- name: McAfee ePO API
  description: McAfee ePolicy Orchestrator (ePO) REST API for centralized security management, including system management, policy assignment, task scheduling, query execution, and threat event retrieval across managed endpoints.
  image: https://www.mcafee.com/content/dam/consumer/en-us/assets/mcafee-logo.png
  humanURL: https://www.mcafee.com/enterprise/en-us/products/epolicy-orchestrator.html
  baseURL: https://your-epo-server:8443/remote
  tags:
  - Endpoint Management
  - Policy Orchestrator
  - Security Management
  properties:
  - type: Documentation
    url: https://docs.mcafee.com/bundle/epolicy-orchestrator-web-api-reference-guide
  - type: OpenAPI
    url: https://your-epo-server:8443/remote/swagger.json
  - type: Authentication
    url: https://docs.mcafee.com/bundle/epolicy-orchestrator-web-api-reference-guide/page/GUID-authentication.html
  - type: OpenAPI
    url: openapi/mcafee-epo-openapi.yml
- name: McAfee MVISION API
  description: Cloud-native security platform API for endpoint detection and response (EDR), threat prevention, device management, and incident investigation.
  image: https://www.mcafee.com/content/dam/consumer/en-us/assets/mcafee-logo.png
  humanURL: https://www.mcafee.com/enterprise/en-us/products/mvision.html
  baseURL: https://api.mvision.mcafee.com
  tags:
  - Cloud Security
  - Edr
  - Mvision
  - Threat Detection
  properties:
  - type: Documentation
    url: https://developer.mvision.mcafee.com/
  - type: Authentication
    url: https://developer.mvision.mcafee.com/authentication
  - type: OpenAPI
    url: openapi/mcafee-mvision-openapi.yml
- name: McAfee Threat Intelligence Exchange (TIE) API
  description: Real-time threat intelligence sharing and reputation services API.
  image: https://www.mcafee.com/content/dam/consumer/en-us/assets/mcafee-logo.png
  humanURL: https://www.mcafee.com/enterprise/en-us/products/threat-intelligence-exchange.html
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
- name: McAfee Data Exchange Layer (DXL) API
  description: Messaging fabric for real-time security data exchange and integration.
  image: https://www.mcafee.com/content/dam/consumer/en-us/assets/mcafee-logo.png
  humanURL: https://www.mcafee.com/enterprise/en-us/products/data-exchange-layer.html
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
- name: McAfee Web Gateway API
  description: Web security gateway REST API for managing rule sets, URL filtering lists, SSL inspection settings, and monitoring proxy traffic and appliance health.
  image: https://www.mcafee.com/content/dam/consumer/en-us/assets/mcafee-logo.png
  humanURL: https://www.mcafee.com/enterprise/en-us/products/web-gateway.html
  baseURL: https://your-mwg-server/Konfigurator/REST
  tags:
  - Proxy
  - Web Gateway
  - Web Security
  properties:
  - type: Documentation
    url: https://docs.mcafee.com/bundle/web-gateway-product-guide
  - type: OpenAPI
    url: openapi/mcafee-web-gateway-openapi.yml
- name: McAfee ESM API
  description: Enterprise Security Manager SIEM REST API for managing security events, alarms, watchlists, data sources, cases, and executing queries against the event database.
  image: https://www.mcafee.com/content/dam/consumer/en-us/assets/mcafee-logo.png
  humanURL: https://www.mcafee.com/enterprise/en-us/products/enterprise-security-manager.html
  baseURL: https://your-esm-server/rs/esm
  tags:
  - Log Management
  - Security Events
  - Siem
  properties:
  - type: Documentation
    url: https://docs.mcafee.com/bundle/enterprise-security-manager-api-reference-guide
  - type: OpenAPI
    url: openapi/mcafee-esm-openapi.yml
name: McAfee
tags:
- Antivirus
- Cybersecurity
- Endpoint Protection
- Security
- Threat Intelligence
type: Contract
image: https://www.mcafee.com/content/dam/consumer/en-us/assets/mcafee-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: APIs for McAfee security products and services.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

