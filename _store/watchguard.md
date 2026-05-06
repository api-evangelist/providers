---
aid: watchguard
name: WatchGuard
description: WatchGuard provides cloud-managed network and endpoint security solutions including Firebox next-generation firewalls, WatchGuard Endpoint Security (WES), AuthPoint multi-factor authentication, and WatchGuard Wi-Fi. WatchGuard Cloud is the unified management platform exposing RESTful APIs for account management, device activation, asset allocation, endpoint device management, security event monitoring, and operator administration.
url: https://www.watchguard.com
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Security
  - Endpoint Security
  - Firewall
  - MFA
  - Network Security
  - Zero Trust
created: '2025-02-17'
modified: '2026-05-03'
specificationVersion: '0.19'
type: Index
apis:
  - aid: watchguard:watchguard-cloud-platform-api
    name: WatchGuard Cloud Platform API
    description: RESTful API for managing WatchGuard Cloud accounts, sub-accounts, and users. Provides account creation and management, audience token generation for managed account access, hardware/license activation, asset allocation, and operator management. Uses OAuth 2.0 bearer tokens and WatchGuard API Key header authentication.
    humanURL: https://www.watchguard.com/help/docs/API/Content/en-US/watchguard-cloud/watchguard-cloud.html
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://www.watchguard.com/help/docs/API/Content/en-US/watchguard-cloud/watchguard-cloud.html
      - type: OpenAPI
        url: openapi/watchguard-cloud-platform-openapi.yml
      - type: SpectralRules
        url: rules/watchguard-rules.yml
    tags:
      - Account Management
      - Activation
      - Allocation
      - Operators
      - Platform
  - aid: watchguard:watchguard-endpoint-security-api
    name: WatchGuard Endpoint Security Management API
    description: RESTful API for managing WatchGuard Endpoint Security (WES) devices and security operations. Provides device listing and protection status, device isolation and release, immediate scan initiation, security event counters and exports, security overview, risk assessment summaries, and configuration management.
    humanURL: https://www.watchguard.com/help/docs/API/Content/en-US/endpoint_security/WES_endpoint_security/v1/WES_endpoint_security.html
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    properties:
      - type: Documentation
        url: https://www.watchguard.com/help/docs/API/Content/en-US/endpoint_security/WES_endpoint_security/v1/WES_endpoint_security.html
      - type: OpenAPI
        url: openapi/watchguard-endpoint-security-openapi.yml
    tags:
      - Device Management
      - Endpoint Security
      - Incident Response
      - Risk Assessment
common:
  - type: Website
    url: https://www.watchguard.com
  - type: Documentation
    url: https://www.watchguard.com/help/docs/API/
  - type: Developer Portal
    url: https://developer.cloud.watchguard.com/
  - type: Getting Started
    url: https://www.watchguard.com/help/docs/API/Content/en-US/api_get_started/get_started.html
  - type: OpenAPI
    url: openapi/watchguard-cloud-platform-openapi.yml
  - type: OpenAPI
    url: openapi/watchguard-endpoint-security-openapi.yml
  - type: SpectralRules
    url: rules/watchguard-rules.yml
  - type: JSONSchema
    url: json-schema/watchguard-device-schema.json
  - type: JSONStructure
    url: json-structure/watchguard-device-structure.json
  - type: JSON-LD
    url: json-ld/watchguard-context.jsonld
  - type: Vocabulary
    url: vocabulary/watchguard-vocabulary.yml
  - type: NaftikoCapabilities
    url: capabilities/endpoint-threat-response.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
