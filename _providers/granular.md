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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Granular Agentic Access
  operation_count: 7
  slug: granular-agentic-access
  summary_line: 7 operations
api_count: 6
apis:
- description: Granular Insights provides analytics and reporting APIs for farm operations, enabling agronomic analysis, yield benchmarking, and field performance reporting for precision agriculture workflows.
  name: Granular Insights API
  slug: granular-insights-api
- description: Field activities — planting, application, harvest
  name: Granular (Corteva Agriscience) Activities API
  slug: granular-activities-api
- description: Crop plans and variety information
  name: Granular (Corteva Agriscience) Crops API
  slug: granular-crops-api
- description: Farm entity management
  name: Granular (Corteva Agriscience) Farms API
  slug: granular-farms-api
- description: Field boundary and attribute management
  name: Granular (Corteva Agriscience) Fields API
  slug: granular-fields-api
- description: Farm financial records and cost tracking
  name: Granular (Corteva Agriscience) Financials API
  slug: granular-financials-api
artifact_total: 17
collections:
- collection_type: open
  name: Granular Farm Management API
  slug: open-granular-farm-management
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/granular-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/granular-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/granular-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/granular-scopes.yml
description: Granular is a farm management platform now part of Corteva Agriscience, providing APIs for crop planning, field records management, financial analysis, and farm operational tracking. The platform serves commercial agriculture operations with data-driven decision support tools.
finops:
- name: Granular Finops
  service_category: API
  slug: granular-finops
image: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/image.png
json_schemas:
- name: Granular Farm Field
  property_count: 15
  slug: granular-field
jsonld:
- class_count: 9
  name: Granular Context
  property_count: 16
  slug: granular-context
layout: provider
modified: '2026-04-28'
name: Granular (Corteva Agriscience)
nav: Providers
network: true
overview: 'Granular (Corteva Agriscience) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Crops API, Farms API, and 2 more. Tagged areas include Agriculture, Farm Management, Financial, Crop Planning, and Agronomy.


  The Granular (Corteva Agriscience) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Granular (Corteva Agriscience)''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Granular Plans Pricing
  plan_count: 3
  slug: granular-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 5
  name: Granular Rate Limits
  slug: granular-rate-limits
rules:
- name: Granular (Corteva Agriscience) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: granular-jsonschema-spectral-rules
scopes:
- name: Granular Scopes
  scope_count: 2
  slug: granular-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.3
  delta: -3.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/granular/refs/heads/main/screenshots/granular-2026-06-20T182321.png
security:
- kind: authentication
  name: Granular Authentication
  slug: granular-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Granular Domain Security
  slug: granular-domain-security
  summary_line: TLSv1.2 · DMARC
slug: granular
tags:
- Agriculture
- Farm Management
- Financial
- Crop Planning
- Agronomy
---
