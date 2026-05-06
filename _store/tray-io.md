---
aid: tray-io
name: Tray.io
description: Tray.io (now also known as Tray.ai) is an AI-ready integration platform as a service (iPaaS) that enables businesses to integrate and automate workflows across cloud applications using a visual editor, pre-built connectors, and API-level access. The platform includes Merlin Agent Builder for building AI agents and a Universal Automation Cloud for connecting data and systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - API Aggregation
  - Automation
  - Connectors
  - Integration
  - iPaaS
  - Workflow Automation
url: https://raw.githubusercontent.com/api-evangelist/tray-io/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - aid: tray-io:tray-platform-api
    name: Tray.io Platform API
    description: The Tray.io Platform API allows developers to leverage the power of Tray's service connectors without using the Builder UI, enabling native integration of third-party APIs into applications without worrying about different protocols and data formats.
    humanURL: https://developer.tray.ai/openapi/trayapi-introduction/
    baseURL: https://api.tray.io/core/v1
    tags:
      - API Management
      - Automation
      - Connectors
      - Integration
      - iPaaS
    properties:
      - type: Documentation
        url: https://developer.tray.ai/openapi/trayapi-introduction/
      - type: Developer Portal
        url: https://developer.tray.ai/
      - type: OpenAPI
        url: openapi/tray-io-platform-api-openapi.yml
      - type: JSONSchema
        url: json-schema/tray-io-connector-schema.json
      - type: JSONSchema
        url: json-schema/tray-io-authentication-schema.json
      - type: JSONSchema
        url: json-schema/tray-io-workspace-schema.json
      - type: JSONLD
        url: json-ld/tray-io-context.jsonld
      - type: JSONStructure
        url: json-structure/tray-io-connector-structure.json
      - type: Example
        url: examples/tray-io-list-connectors-example.json
      - type: Example
        url: examples/tray-io-call-connector-example.json
      - type: SpectralRuleset
        url: rules/tray-io-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/platform-api.yaml
  - aid: tray-io:tray-embedded-api
    name: Tray.io Embedded API
    description: The Tray.io Embedded API provides GraphQL-based APIs for embedding Tray's automation capabilities into your own products, enabling end users to configure and manage integrations directly.
    humanURL: https://embedded-api-docs.tray.io/
    tags:
      - Embedded Integration
      - GraphQL
      - White Label
    properties:
      - type: Documentation
        url: https://embedded-api-docs.tray.io/
      - type: Developer Portal
        url: https://developer.tray.ai/
common:
  - type: Website
    url: https://tray.ai
  - type: Documentation
    url: https://tray.ai/documentation
  - type: Developer Portal
    url: https://developer.tray.ai/
  - type: Pricing
    url: https://tray.ai/pricing
  - type: LinkedIn
    url: https://www.linkedin.com/company/tray-io
  - type: X (Twitter)
    url: https://x.com/tray
  - type: NaftikoCapability
    url: capabilities/integration-platform.yaml
  - type: Vocabulary
    url: vocabulary/tray-io-vocabulary.yml
  - type: Features
    data:
      - 'Tray Advantage: foundational tier (custom)'
      - 'Tray Advantage Plus: expanded services (custom)'
      - Per-workspace + task pricing model
      - Quarterly billing cycles
      - Tasks = automated actions executed
      - 650+ pre-built connectors
      - Tray Embedded for SaaS vendors
      - Merlin AI for workflow generation
      - Visual workflow builder + JSONata data mapping
      - Webhook triggers + scheduled triggers
      - 'API requests: 600 req/min/workspace'
      - 'Webhook trigger: 100 req/sec/workflow'
      - Concurrent execution scales with tier
      - Connector SDK for custom integrations
      - SOC 2 Type 2 compliant
      - HIPAA + GDPR-ready
    sources:
      - https://tray.ai/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
