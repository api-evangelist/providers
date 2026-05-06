---
aid: leanix
name: LeanIX
description: LeanIX (now SAP LeanIX) is an enterprise architecture and SaaS management platform providing IT portfolio management, application portfolio rationalization, SaaS discovery, and technology risk management. The platform exposes REST APIs for integrating with the fact sheet inventory, running inbound and outbound synchronizations, and managing workspace data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise Architecture
  - SaaS Management
  - IT Portfolio Management
  - Application Portfolio
  - Technology Risk
url: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: leanix:integration-api
    name: LeanIX Integration API
    description: The LeanIX Integration API exposes a generic interface for inbound and outbound data synchronization with the LeanIX workspace. It supports processor configurations, starter and advanced examples, and managing synchronization runs that move fact sheet data in and out of LeanIX.
    humanURL: https://help.sap.com/docs/leanix/ea
    baseURL: https://app.leanix.net/services/integration-api/v1
    tags:
      - Integration
      - Synchronization
      - Enterprise Architecture
    properties:
      - type: Documentation
        url: https://help.sap.com/docs/leanix/ea
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/leanix/refs/heads/main/openapi/leanix-openapi.json
common:
  - type: Website
    url: https://www.leanix.net
  - type: Documentation
    url: https://help.sap.com/docs/leanix/ea
  - type: GitHub Organization
    url: https://github.com/leanix
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
