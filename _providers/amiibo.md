---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Amiibo Agentic Access
  operation_count: 7
  slug: amiibo-agentic-access
  summary_line: 7 operations
api_count: 3
apis:
- description: Endpoints for retrieving Amiibo figure data
  name: Amiibo API Amiibo API
  slug: amiibo-amiibo-api
- description: API metadata endpoints
  name: Amiibo API Metadata API
  slug: amiibo-metadata-api
- description: Reference data endpoints for types, series, characters, and game series
  name: Amiibo API Reference API
  slug: amiibo-reference-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amiibo API
  slug: open-amiibo-amiibo-api
- collection_type: open
  name: Amiibo Metadata API
  slug: open-amiibo-metadata-api
- collection_type: open
  name: Amiibo Reference API
  slug: open-amiibo-reference-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amiibo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amiibo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amiiboapi.org/
- group: docs
  title: ''
  type: Documentation
  url: https://amiiboapi.org/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/N3evin/AmiiboAPI
- group: commercial
  title: ''
  type: Plans
  url: plans/amiibo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/amiibo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/amiibo-finops.yml
created: '2026-06-13'
description: AmiiboAPI is a free RESTful API providing comprehensive data about Nintendo Amiibo figures, including character details, game series, amiibo series classifications, regional release dates, and compatible game information across 3DS, Wii U, and Nintendo Switch platforms. The API requires no authentication and supports filtering by name, character, game series, type, and hexadecimal identifiers.
examples:
- key_count: 1
  name: Amiibo Example
  slug: amiibo-example
- key_count: 1
  name: Amiibo Full Example
  slug: amiibo-full-example
- key_count: 4
  name: Reference Example
  slug: reference-example
finops:
- name: Amiibo Finops
  service_category: ''
  slug: amiibo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amiibo.png
json_schemas:
- name: Amiibo API Schemas
  property_count: 0
  slug: amiibo
layout: provider
modified: '2026-06-13'
name: Amiibo API
nav: Providers
network: true
overview: 'Amiibo API publishes 3 APIs on the [APIs.io](https://apis.io/) network: Amiibo API, Metadata API, and Reference API. Tagged areas include Nintendo, Amiibo, Gaming, Figures, and Characters.


  The Amiibo API catalog on APIs.io includes 1 Spectral governance ruleset.


  Amiibo API''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Amiibo Plans Pricing
  plan_count: 1
  slug: amiibo-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Amiibo Rate Limits
  slug: amiibo-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Amiibo API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: amiibo-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.8
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 56.5
    developer_ergonomics: 9.5
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amiibo/refs/heads/main/screenshots/amiibo-2026-06-20T171931.png
security:
- kind: domain-security
  name: Amiibo Domain Security
  slug: amiibo-domain-security
  summary_line: no transport/DNS hardening detected
slug: amiibo
tags:
- Nintendo
- Amiibo
- Gaming
- Figures
- Characters
- Video Games
- REST
website: https://amiiboapi.org/
---
