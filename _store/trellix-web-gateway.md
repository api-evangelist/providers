---
aid: trellix-web-gateway
name: Trellix Web Gateway
description: Trellix Web Gateway (formerly McAfee Web Gateway) provides advanced threat protection and secure web access for enterprises. It offers URL filtering, malware detection, data loss prevention, SSL inspection, and cloud security capabilities through a comprehensive web security platform with REST APIs for appliance management, policy configuration, and security reporting.
image: https://www.trellix.com/assets/images/trellix-logo.png
url: https://www.trellix.com/products/web-gateway/
created: '2024'
modified: '2026-05-03'
specificationVersion: '0.18'
tags:
  - Cybersecurity
  - Data Loss Prevention
  - Enterprise Security
  - Malware Protection
  - Network Security
  - SSL Inspection
  - Threat Protection
  - URL Filtering
  - Web Gateway
apis:
  - name: Trellix Web Gateway REST API
    description: RESTful API for managing and configuring Trellix Web Gateway appliances, including policy management, system administration, file handling, custom list management, and session-based authentication tasks.
    image: https://www.trellix.com/assets/images/products/web-gateway-icon.png
    humanURL: https://docs.trellix.com/bundle/web-gateway-product-guide
    baseURL: https://<mwg-server>:<port>/Konfigurator/REST
    tags:
      - Appliance Management
      - Configuration Management
      - Enterprise Security
      - Gateway
      - Threat Protection
      - Web Security
    properties:
      - type: Documentation
        url: https://docs.trellix.com/bundle/web-gateway-rest-api-guide
      - type: OpenAPI
        url: https://docs.trellix.com/api/web-gateway/openapi.json
      - type: Authentication
        url: https://docs.trellix.com/bundle/web-gateway-rest-api-guide/page/authentication.html
      - type: PostmanCollection
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
      - type: APIReference
        url: https://docs.trellix.com/api/web-gateway/reporting/
      - type: OpenAPI
        url: openapi/trellix-web-gateway-reporting-openapi.yml
  - name: Trellix Web Gateway Policy API
    description: API for creating, updating, and managing security policies, rules, and configurations for web filtering, anti-malware, SSL inspection, DLP, and threat prevention.
    image: https://www.trellix.com/assets/images/products/web-gateway-icon.png
    humanURL: https://docs.trellix.com/bundle/web-gateway-policy-guide
    baseURL: https://<mwg-server>:<port>/Konfigurator/REST/policy
    tags:
      - Configuration
      - DLP
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
common:
  - type: Getting Started
    url: https://docs.trellix.com/bundle/web-gateway-getting-started
  - type: Developer Portal
    url: https://developer.trellix.com/
  - type: Change Log
    url: https://docs.trellix.com/bundle/web-gateway-release-notes
  - type: Status
    url: https://status.trellix.com/
  - type: Terms of Service
    url: https://www.trellix.com/legal/terms-of-use/
  - type: Privacy Policy
    url: https://www.trellix.com/privacy/
  - type: Portal
    url: https://www.trellix.com/login/
  - type: SDK
    url: https://github.com/trellix-enterprise/mwg-sdk
  - type: JSON-LD
    url: json-ld/trellix-web-gateway-context.jsonld
  - type: JSONSchema
    url: json-schema/trellix-web-gateway-security-event-schema.json
  - type: JSONSchema
    url: json-schema/trellix-web-gateway-rule-set-schema.json
  - type: JSONStructure
    url: json-structure/trellix-web-gateway-security-event-structure.json
  - type: SpectralRules
    url: rules/trellix-web-gateway-spectral-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/web-security-operations.yaml
  - type: NaftikoCapabilities
    url: capabilities/web-policy-management.yaml
  - type: Vocabulary
    url: vocabulary/trellix-web-gateway-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
