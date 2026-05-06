---
aid: checkpoint
name: Check Point
description: Check Point Software Technologies is a global cybersecurity vendor providing network, cloud, endpoint, mobile, and email security through its Quantum, CloudGuard, and Harmony product families. Check Point exposes a wide range of REST APIs for security automation, including the Smart-1 Management API, Gaia OS API, CloudGuard cloud security posture API, Identity Awareness API, Spark and Zero Touch device management APIs, Harmony Email and Collaboration API, Threat Hunting (TH) API, and CloudGuard WAF API.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/checkpoint/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - Cloud Security
  - Cybersecurity
  - Endpoint Security
  - Firewall
  - Identity Awareness
  - Mobile Security
  - Network Security
  - Security
  - Threat Prevention
  - WAF
created: '2025-01-08'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: checkpoint:management-api
    name: Check Point Management API
    description: REST API for the Smart-1 Security Management Server. Automates policy and object management including host/network/service objects, access and NAT rulebases, and publish/install operations.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sc1.checkpoint.com/documents/latest/APIs/
    baseURL: https://management.example.com/web_api
    tags:
      - Firewall
      - Management
      - Network Security
    properties:
      - type: Documentation
        url: https://sc1.checkpoint.com/documents/latest/APIs/
      - type: OpenAPI
        url: openapi/checkpoint-management-api-openapi.yml
  - aid: checkpoint:gaia-api
    name: Check Point Gaia API
    description: REST API for the Check Point Gaia operating system. Manages gateway interfaces, routing, system info, and configuration.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sc1.checkpoint.com/documents/latest/GaiaAPIs/
    baseURL: https://gateway.example.com/gaia_api
    tags:
      - Gaia
      - Operating System
    properties:
      - type: Documentation
        url: https://sc1.checkpoint.com/documents/latest/GaiaAPIs/
      - type: OpenAPI
        url: openapi/checkpoint-gaia-api-openapi.yml
  - aid: checkpoint:cloudguard-api
    name: Check Point CloudGuard API
    description: REST API for CloudGuard Native cloud security posture management, cloud account onboarding, compliance findings, and rulesets across AWS, Azure, and GCP.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.cgn.portal.checkpoint.com/reference/introduction
    baseURL: https://api.dome9.com/v2
    tags:
      - Cloud Security
      - Compliance
      - Posture Management
    properties:
      - type: Documentation
        url: https://docs.cgn.portal.checkpoint.com/
      - type: OpenAPI
        url: openapi/checkpoint-cloudguard-api-openapi.yml
  - aid: checkpoint:identity-awareness-api
    name: Check Point Identity Awareness API
    description: REST API for posting and revoking user-to-IP identity associations on Check Point gateways, enabling identity-aware policy enforcement.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sc1.checkpoint.com/documents/latest/IdentityAPIs/
    baseURL: https://gateway.example.com/_IA_MU_Agent
    tags:
      - Identity
      - Network Security
    properties:
      - type: Documentation
        url: https://sc1.checkpoint.com/documents/latest/IdentityAPIs/
      - type: OpenAPI
        url: openapi/checkpoint-identity-awareness-api-openapi.yml
  - aid: checkpoint:spark-management-api
    name: Check Point Spark Management API
    description: REST API for centrally managing Check Point Quantum Spark SMB appliances including configuration and policy.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sc1.checkpoint.com/documents/latest/SmpAPIs/
    tags:
      - SMB
      - Spark
    properties:
      - type: Documentation
        url: https://sc1.checkpoint.com/documents/latest/SmpAPIs/
  - aid: checkpoint:zero-touch-api
    name: Check Point Zero Touch API
    description: REST API for the Zero Touch deployment service that streamlines bring-up of new Check Point appliances.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sc1.checkpoint.com/documents/Appliances/Zero_Touch_REST_API_Guide/EN/Content/Topics-API/Overview.htm
    tags:
      - Deployment
      - Zero Touch
    properties:
      - type: Documentation
        url: https://sc1.checkpoint.com/documents/Appliances/Zero_Touch_REST_API_Guide/EN/Content/Topics-API/Overview.htm
  - aid: checkpoint:harmony-email-api
    name: Check Point Harmony Email API
    description: REST API for Harmony Email and Collaboration (formerly Avanan) surfacing email security events, quarantined items, and admin actions.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sc1.checkpoint.com/documents/Harmony_Email_and_Collaboration_API_Reference/Topics-HEC-Avanan-API-Reference-Guide/Overview/API-Overview.htm
    baseURL: https://smart-api.avanan.net/v2.0
    tags:
      - Email Security
      - Harmony
    properties:
      - type: Documentation
        url: https://sc1.checkpoint.com/documents/Harmony_Email_and_Collaboration_API_Reference/Topics-HEC-Avanan-API-Reference-Guide/Overview/API-Overview.htm
      - type: OpenAPI
        url: openapi/checkpoint-harmony-email-api-openapi.yml
  - aid: checkpoint:th-api
    name: Check Point Threat Hunting API
    description: REST API for the Check Point Threat Hunting (TH) platform exposing threat intelligence, indicators, and hunting queries.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://sc1.checkpoint.com/documents/latest/ThAPIs/index.html
    tags:
      - Threat Hunting
      - Threat Intelligence
    properties:
      - type: Documentation
        url: https://sc1.checkpoint.com/documents/latest/ThAPIs/index.html
  - aid: checkpoint:cloudguard-waf-api
    name: Check Point CloudGuard WAF API
    description: Management API for the CloudGuard WAF cloud-native web application and API protection product.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://waf-doc.inext.checkpoint.com/references/management-api
    tags:
      - WAF
      - Web Security
    properties:
      - type: Documentation
        url: https://waf-doc.inext.checkpoint.com/
common:
  - type: Website
    url: https://www.checkpoint.com/
  - type: Documentation
    url: https://sc1.checkpoint.com/documents/
  - type: Support
    url: https://www.checkpoint.com/support-services/
  - type: Login
    url: https://portal.checkpoint.com/
  - type: Blog
    url: https://blog.checkpoint.com/
  - type: GitHub
    url: https://github.com/CheckPointSW
  - type: TermsOfService
    url: https://www.checkpoint.com/about-us/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.checkpoint.com/about-us/privacy-statement/
  - type: JSONLD
    url: json-ld/checkpoint-context.jsonld
  - type: JSONSchema
    url: json-schema/checkpoint-host-schema.json
  - type: JSONSchema
    url: json-schema/checkpoint-access-rule-schema.json
  - type: Spectral
    url: spectral/checkpoint-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/checkpoint-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
