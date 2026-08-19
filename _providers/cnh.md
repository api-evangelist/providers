---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cnh Agentic Access
  operation_count: 13
  slug: cnh-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 8
apis:
- description: The CNH Developer Portal at develop.cnh.com hosts onboarding, authentication guidance, API guides, Postman collections, and curated SwaggerHub documentation for FieldOps and related CNH APIs. Develope
  name: CNH Developer Portal
  slug: cnh-developer-portal
- description: Fleet and equipment details.
  name: CNH Equipment API
  slug: cnh-equipment-api
- description: Grower, farm, field, and boundary management.
  name: CNH Farm Setup API
  slug: cnh-farm-setup-api
- description: Operations by vehicle.
  name: CNH Operations API
  slug: cnh-operations-api
- description: Send prescription Rx files to vehicles or FieldOps.
  name: CNH Prescriptions API
  slug: cnh-prescriptions-api
- description: OAuth refresh and access token management.
  name: CNH Tokens API
  slug: cnh-tokens-api
- description: ISO 15143-3 vehicle telemetry, fault codes, and metrics.
  name: CNH Vehicle Telemetry API
  slug: cnh-vehicle-telemetry-api
- description: Subscribe to FieldOps event notifications.
  name: CNH Webhooks API
  slug: cnh-webhooks-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CNH FieldOps Equipment API
  slug: open-cnh-equipment-api
- collection_type: open
  name: CNH FieldOps Equipment Farm Setup API
  slug: open-cnh-farm-setup-api
- collection_type: open
  name: CNH FieldOps API
  slug: open-cnh-fieldops
- collection_type: open
  name: CNH FieldOps Equipment Operations API
  slug: open-cnh-operations-api
- collection_type: open
  name: CNH FieldOps Equipment Prescriptions API
  slug: open-cnh-prescriptions-api
- collection_type: open
  name: CNH FieldOps Equipment Tokens API
  slug: open-cnh-tokens-api
- collection_type: open
  name: CNH FieldOps Equipment Vehicle Telemetry API
  slug: open-cnh-vehicle-telemetry-api
- collection_type: open
  name: CNH FieldOps Equipment Webhooks API
  slug: open-cnh-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cnh-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cnh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cnh-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cnh-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cnh
- group: company
  title: ''
  type: Website
  url: https://www.cnhindustrial.com/
- group: start
  title: ''
  type: Portal
  url: https://develop.cnh.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://develop.cnh.com/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://develop.cnh.com/api-guides
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/cnh-fieldops-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cnh-equipment-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cnh-telemetry-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/cnh-context.jsonld
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/cnh-rules.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cnhindustrial.com/en-us/privacy/pages/default.aspx
created: '2025-03-01'
description: CNH Industrial is a global leader in the manufacturing and distribution of agricultural and construction equipment, with brands including Case IH, New Holland, STEYR, Case CE, and New Holland Construction. Through develop.cnh.com CNH operates a developer portal that exposes the FieldOps API - a unified, ISO 15143-3 compliant REST API for vehicle telemetry, equipment management, farm/grower hierarchy, operations, prescription Rx delivery, and webhook subscriptions across both agronomic machinery and construction equipment.
finops:
- name: Cnh Finops
  service_category: API
  slug: cnh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cnh.png
json_schemas:
- name: CNH FieldOps Equipment
  property_count: 7
  slug: cnh-equipment
- name: CNH FieldOps Vehicle Telemetry
  property_count: 13
  slug: cnh-telemetry
jsonld:
- class_count: 31
  name: Cnh Context
  property_count: 0
  slug: cnh-context
layout: provider
modified: '2026-05-19'
name: CNH
nav: Providers
network: true
overview: 'CNH publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Equipment API, Farm Setup API, Operations API, and 4 more. Tagged areas include Agriculture, Construction, Telematics, Equipment, and FieldOps.


  The CNH catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  CNH''s developer surface includes authentication, developer portal, getting-started guide, documentation, and 11 more developer resources.'
plans:
- name: Cnh Plans Pricing
  plan_count: 3
  slug: cnh-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Cnh Rate Limits
  slug: cnh-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: CNH API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cnh-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: CNH API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: cnh-rules
scopes:
- name: Cnh Scopes
  scope_count: 5
  slug: cnh-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 38.9
  delta: -6.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 65.7
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 45.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cnh/refs/heads/main/screenshots/cnh-2026-06-20T174635.png
security:
- kind: authentication
  name: Cnh Authentication
  slug: cnh-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cnh Domain Security
  slug: cnh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cnh
tags:
- Agriculture
- Construction
- Telematics
- Equipment
- FieldOps
website: https://www.cnhindustrial.com/
---
