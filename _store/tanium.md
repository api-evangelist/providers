---
aid: tanium
name: Tanium
description: Tanium is a unified endpoint management and security platform that provides real-time visibility and control across all endpoints. It offers a suite of APIs including a GraphQL-based API Gateway and platform REST APIs for integrating with endpoint management, security, compliance, and threat response capabilities.
type: Index
position: Consumer
access: 3rd-Party
image: https://www.tanium.com/images/tanium-logo.png
tags:
  - Compliance
  - Endpoint Management
  - Patch Management
  - Security
  - Threat Detection
  - Unified Endpoint Management
created: '2025-02-06'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tanium/refs/heads/main/apis.yml
specificationVersion: '0.18'
apis:
  - aid: tanium:api-gateway
    name: Tanium API Gateway
    description: The Tanium API Gateway is a GraphQL interface for querying data and taking action in Tanium. It is the preferred method for integrating with Tanium, supporting asset queries, endpoint actions, and data retrieval across the platform.
    humanURL: https://docs.tanium.com/api_gateway/api_gateway/overview.html
    tags:
      - API Gateway
      - Endpoints
      - GraphQL
      - Integration
      - Queries
    properties:
      - type: Documentation
        url: https://docs.tanium.com/api_gateway/api_gateway/overview.html
      - type: Reference
        url: https://docs.tanium.com/api_gateway/api_gateway/api_gateway_examples.html
      - type: GettingStarted
        url: https://docs.tanium.com/api_gateway/api_gateway/api_gateway.html
      - type: GraphQLSchema
        url: https://developer.tanium.com/site/global/apis/graphql/schema/
  - aid: tanium:platform-rest-api
    name: Tanium Platform REST API
    description: The Tanium Platform REST API provides access to core platform functionality including gathering endpoint information, deploying actions, evaluating deployment health, managing certificates, updating packages, and downloading audit logs.
    humanURL: https://developer.tanium.com/apis/api_intro
    tags:
      - Actions
      - Endpoints
      - Platform
      - REST API
      - Security
    properties:
      - type: Documentation
        url: https://developer.tanium.com/apis/api_intro
      - type: IntegrationGuide
        url: https://developer.tanium.com/guides/core-platform/integration_methods
      - type: Authentication
        url: https://docs.tanium.com/platform_user/platform_user/console_api_tokens.html
      - type: OpenAPI
        url: openapi/tanium-platform-rest-api-openapi.yml
  - aid: tanium:threat-response-api
    name: Tanium Threat Response API
    description: The Tanium Threat Response REST API enables starting investigations, viewing Recorder events, gathering evidence, and performing file and directory operations on endpoints for threat detection and incident response.
    humanURL: https://developer.tanium.com/site/global/docs/how_tos/tr_actions/index.gsp
    tags:
      - Incident Response
      - Investigations
      - Security
      - Threat Detection
      - Threat Response
    properties:
      - type: Documentation
        url: https://developer.tanium.com/site/global/docs/how_tos/tr_actions/index.gsp
      - type: GettingStarted
        url: https://help.tanium.com/bundle/ug_threat_response_cloud/page/threat_response/gettingstarted.html
      - type: OpenAPI
        url: openapi/tanium-threat-response-api-openapi.yml
  - aid: tanium:connect-api
    name: Tanium Connect API
    description: The Tanium Connect REST API allows creating, editing, and managing connections for delivering endpoint data to downstream systems via files, syslog, webhooks, and other destination types on a schedule or triggered by events.
    humanURL: https://docs.tanium.com/connect/connect/index.html
    tags:
      - Connections
      - Data Delivery
      - Integration
      - Syslog
      - Webhooks
    properties:
      - type: Documentation
        url: https://docs.tanium.com/connect/connect/index.html
      - type: OpenAPI
        url: openapi/tanium-connect-api-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: JSONSchema
    url: json-schema/tanium-endpoint-schema.json
  - type: JSONSchema
    url: json-schema/tanium-question-schema.json
  - type: JSONSchema
    url: json-schema/tanium-alert-schema.json
  - type: JSONSchema
    url: json-schema/tanium-sensor-schema.json
  - type: JSONSchema
    url: json-schema/tanium-package-schema.json
  - type: JSONSchema
    url: json-schema/tanium-action-schema.json
  - type: JSONSchema
    url: json-schema/tanium-connection-schema.json
  - type: JSONStructure
    url: json-structure/tanium-endpoint-structure.json
  - type: JSONStructure
    url: json-structure/tanium-action-structure.json
  - type: JSONLD
    url: json-ld/tanium-context.jsonld
  - type: SpectralRules
    url: rules/tanium-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/endpoint-management.yaml
  - type: Vocabulary
    url: vocabulary/tanium-vocabulary.yml
  - type: Portal
    url: https://developer.tanium.com/
  - type: Documentation
    url: https://help.tanium.com/
  - type: GettingStarted
    url: https://developer.tanium.com/apis/api_intro
  - type: Authentication
    url: https://docs.tanium.com/platform_user/platform_user/console_api_tokens.html
  - type: Blog
    url: https://www.tanium.com/p/tanium-blog/
  - type: Support
    url: https://community.tanium.com/s/
  - type: TermsOfService
    url: https://www.tanium.com/terms-of-use/
  - type: PrivacyPolicy
    url: https://www.tanium.com/privacy/
  - type: GitHubOrganization
    url: https://github.com/tanium
  - type: Community
    url: https://community.tanium.com/s/
  - type: Website
    url: https://www.tanium.com/
  - type: Login
    url: https://community.tanium.com/s/login/
  - type: SignUp
    url: https://community.tanium.com/CommunitiesSelfReg
  - type: SDKs
    url: https://tanium.github.io/pytan/
  - type: IntegrationGuide
    url: https://developer.tanium.com/guides/core-platform/integration_methods
  - type: UseCases
    url: https://developer.tanium.com/use_cases
  - type: ChangeLog
    url: https://help.tanium.com/bundle/releasenotes/page/releasenotes/index.html
  - type: Contact
    url: https://www.tanium.com/contact/
---
