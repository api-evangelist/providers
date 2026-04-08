---
aid: trellix-web-gateway
url: https://raw.githubusercontent.com/api-evangelist/trellix-web-gateway/refs/heads/main/apis.yml
apis:
- name: Trellix Web Gateway REST API
  description: RESTful API for managing and configuring Trellix Web Gateway appliances, including policy management, reporting, threat intelligence, and system administration tasks.
  image: https://www.trellix.com/assets/images/products/web-gateway-icon.png
  humanURL: https://docs.trellix.com/bundle/web-gateway-product-guide
  baseURL: https://<mwg-server>:<port>/Konfigurator/REST
  tags:
  - Enterprise Security
  - Gateway
  - Threat Protection
  - URL Filtering
  - Web Security
  properties:
  - type: Documentation
    url: https://docs.trellix.com/bundle/web-gateway-rest-api-guide
  - type: OpenAPI
    url: https://docs.trellix.com/api/web-gateway/openapi.json
  - type: Authentication
    url: https://docs.trellix.com/bundle/web-gateway-rest-api-guide/page/authentication.html
  - type: Postman Collection
    url: https://www.postman.com/trellix/workspace/trellix-public/collection/web-gateway-api
  - type: OpenAPI
    url: openapi/trellix-web-gateway-rest-openapi.yml
  contact:
  - type: Support
    url: https://www.trellix.com/support/
  - type: Email
    email: support@trellix.com
- name: Trellix Web Gateway Reporting API
  description: API for accessing web traffic logs, security events, threat analytics, and generating custom reports from Web Gateway data.
  image: https://www.trellix.com/assets/images/products/web-gateway-icon.png
  humanURL: https://docs.trellix.com/bundle/web-gateway-reporting-guide
  baseURL: https://<mwg-server>:<port>/reporter/api
  tags:
  - Analytics
  - Logs
  - Reporting
  - Security Events
  properties:
  - type: Documentation
    url: https://docs.trellix.com/bundle/web-gateway-reporting-api
  - type: API Reference
    url: https://docs.trellix.com/api/web-gateway/reporting/
  - type: OpenAPI
    url: openapi/trellix-web-gateway-reporting-openapi.yml
- name: Trellix Web Gateway Policy API
  description: API for creating, updating, and managing security policies, rules, and configurations for web filtering and threat prevention.
  image: https://www.trellix.com/assets/images/products/web-gateway-icon.png
  humanURL: https://docs.trellix.com/bundle/web-gateway-policy-guide
  baseURL: https://<mwg-server>:<port>/Konfigurator/REST/policy
  tags:
  - Configuration
  - Policy Management
  - Rules
  - Security Policies
  properties:
  - type: Documentation
    url: https://docs.trellix.com/bundle/web-gateway-policy-api
  - type: Examples
    url: https://github.com/trellix-enterprise/mwg-api-examples
  - type: OpenAPI
    url: openapi/trellix-web-gateway-policy-openapi.yml
name: Trellix Web Gateway
tags:
- Cybersecurity
- Data Loss Prevention
- Enterprise Security
- Malware Protection
- Network Security
- Threat Protection
- URL Filtering
- Web Gateway
type: Contract
image: https://www.trellix.com/assets/images/trellix-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Trellix Web Gateway (formerly McAfee Web Gateway) provides advanced threat protection and secure web access for enterprises. It offers URL filtering, malware detection, data loss prevention, and cloud security capabilities through a comprehensive web security platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

