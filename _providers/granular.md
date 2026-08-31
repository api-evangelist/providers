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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Granular Agentic Access
  operation_count: 7
  slug: granular-agentic-access
  summary_line: 7 operations
api_count: 1
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
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Granular Farm Management Activities API
  slug: open-granular-activities-api
- collection_type: open
  name: Granular Farm Management Activities Crops API
  slug: open-granular-crops-api
- collection_type: open
  name: Granular Farm Management API
  slug: open-granular-farm-management
- collection_type: open
  name: Granular Farm Management Activities Farms API
  slug: open-granular-farms-api
- collection_type: open
  name: Granular Farm Management Activities Fields API
  slug: open-granular-fields-api
- collection_type: open
  name: Granular Farm Management Activities Financials API
  slug: open-granular-financials-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/granular-capability-edges.yml
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


  Granular (Corteva Agriscience)''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Granular Plans Pricing
  plan_count: 3
  slug: granular-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Granular Rate Limits
  slug: granular-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Granular (Corteva Agriscience) API Rules
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
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 59.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 59.6
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
