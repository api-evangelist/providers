---
aid: trelica
name: Trelica
description: Trelica is a SaaS management platform (now part of 1Password SaaS Manager) providing application discovery, license optimization, contract management, and workflow automation for IT teams. The platform offers a REST API covering applications, users, people, contracts, workflows, assets, and audit logs with OAuth 2.0 authentication using Client Credentials and Authorization Code flows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Contract Management
  - IT Management
  - License Management
  - SaaS Management
  - Software Asset Management
url: https://raw.githubusercontent.com/api-evangelist/trelica/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trelica:trelica
    name: Trelica REST API
    description: The Trelica REST API provides programmatic access to the core areas of the Trelica SaaS management platform, including applications, people, contracts, workflows, assets, audit logs, and user management. The API uses OAuth 2.0 with either Client Credentials (for integrations) or Authorization Code flow (for third-party developer apps). The Users endpoint follows the SCIM protocol.
    humanURL: https://trelica.gitbook.io/trelica-api
    baseURL: https://app.trelica.com/api
    tags:
      - Application Discovery
      - Contract Management
      - IT Management
      - License Management
      - SaaS Management
      - Software Asset Management
    properties:
      - type: Documentation
        url: https://trelica.gitbook.io/trelica-api
      - type: Documentation
        url: https://help.trelica.com/hc/en-us/sections/7739034184093-API
      - type: Authentication
        url: https://help.trelica.com/hc/en-us/articles/7739283478941-Trelica-API
      - type: OpenAPI
        url: openapi/trelica-rest-api-openapi.yml
      - type: GitHubOrganization
        url: https://github.com/trelica
      - type: GitHubRepository
        url: https://github.com/trelica/trelica-api-sdk
      - type: GitHubRepository
        url: https://github.com/trelica/powershell
      - type: GitHubRepository
        url: https://github.com/trelica/node
common:
  - type: Website
    url: https://www.trelica.com
  - type: Documentation
    url: https://trelica.gitbook.io/trelica-api
  - type: HelpCenter
    url: https://help.trelica.com/hc/en-us/sections/7739034184093-API
  - type: Authentication
    url: https://help.trelica.com/hc/en-us/articles/7739283478941-Trelica-API
  - type: GitHubOrganization
    url: https://github.com/trelica
  - type: SDK
    url: https://github.com/trelica/trelica-api-sdk
  - type: SDK
    url: https://github.com/trelica/node
  - type: SDK
    url: https://github.com/trelica/powershell
  - type: JSONSchema
    url: json-schema/trelica-application-schema.json
  - type: JSONSchema
    url: json-schema/trelica-person-schema.json
  - type: JSONSchema
    url: json-schema/trelica-contract-schema.json
  - type: JSONStructure
    url: json-structure/trelica-application-structure.json
  - type: JSON-LD
    url: json-ld/trelica-context.jsonld
  - type: SpectralRules
    url: rules/trelica-spectral-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/saas-management.yaml
  - type: Vocabulary
    url: vocabulary/trelica-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
