---
aid: schematic
name: Schematic
description: Schematic is a feature and entitlement management platform for SaaS companies, providing pricing, packaging, and metering capabilities. It enables engineering and product teams to manage feature flags, define subscription plans, track feature usage, and control customer entitlements without code changes. Schematic raised $6.5M in April 2026 and launched an official Stripe App for entitlement management as a first-class billing primitive. Customers include Plotly, Automox, Florence, Blackcloak, Sema4.ai, and Pagos.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Billing
  - Entitlements
  - Feature Flags
  - Feature Management
  - FinOps
  - Metering
  - Pricing
  - SaaS
url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: schematic:schematic-api
    name: Schematic API
    description: The Schematic REST API enables programmatic management of features, flags, plans, companies, users, entitlements, billing credits, and webhooks. Authentication uses API keys sent in the X-Schematic-Api-Key header. Supports production, staging, and development environments with environment-scoped API keys (sch_prod, sch_stag, sch_dev prefixes).
    humanURL: https://schematichq.com/
    tags:
      - Billing
      - Entitlements
      - Feature Flags
      - Feature Management
      - Metering
      - Plans
      - SaaS
    properties:
      - type: Documentation
        url: https://docs.schematichq.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/openapi/schematic-openapi.yml
      - type: API Reference
        url: https://docs.schematichq.com/api-reference
      - type: Authentication
        url: https://docs.schematichq.com/api-reference/authentication.mdx
      - type: Getting Started
        url: https://docs.schematichq.com/
      - type: GitHub Repository
        url: https://github.com/SchematicHQ
      - type: SDK Python
        url: https://github.com/SchematicHQ/schematic-python
      - type: SDK Node
        url: https://github.com/SchematicHQ/schematic-node
      - type: SDK Go
        url: https://github.com/SchematicHQ/schematic-go
      - type: SDK Ruby
        url: https://github.com/SchematicHQ/schematic-ruby
      - type: SDK Java
        url: https://github.com/SchematicHQ/schematic-java
      - type: SDK PHP
        url: https://github.com/SchematicHQ/schematic-php
      - type: SDK C#
        url: https://github.com/SchematicHQ/schematic-csharp
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/rules/schematic-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/capabilities/feature-management.yaml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/capabilities/customer-management.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/json-schema/schematic-company-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/json-schema/schematic-feature-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/json-schema/schematic-plan-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/json-structure/schematic-api-structure.json
      - type: JSONLd
        url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/json-ld/schematic-context.jsonld
common:
  - type: Website
    url: https://schematichq.com/
  - type: Documentation
    url: https://docs.schematichq.com/
  - type: API Reference
    url: https://docs.schematichq.com/api-reference
  - type: Blog
    url: https://schematichq.com/blog
  - type: GitHub Organization
    url: https://github.com/SchematicHQ
  - type: LinkedIn
    url: https://www.linkedin.com/company/schematichq
  - type: Pricing
    url: https://schematichq.com/pricing
  - type: Changelog
    url: https://schematichq.com/changelog
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/vocabulary/schematic-vocabulary.yml
  - type: Examples
    url: https://raw.githubusercontent.com/api-evangelist/schematic/refs/heads/main/examples/schematic-check-flag-example.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
