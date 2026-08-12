---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Wegowise Agentic Access
  operation_count: 33
  slug: wegowise-agentic-access
  summary_line: 33 operations · 16 acting
api_count: 11
apis:
- description: The WegoPro API for multifamily and commercial property portfolios. Provides endpoints for buildings, apartments, areas, meters, raw data, and monthly normalized usage data. The primary API for proper
  name: WegoWise Pro API
  slug: wegowise-pro
- description: 'The WegoData API for data-only accounts. Enables meter management and automated utility data import without the full building structure hierarchy. Supports all utility types: Electric, Gas, Oil, Water'
  name: WegoWise Data API
  slug: wegowise-data
- description: Public endpoints accessible without authentication. Provides a list of utility companies supported for automated data import, useful for finding utility_company_id values when configuring meters.
  name: WegoWise Public API
  slug: wegowise-public
- description: Manage apartment and unit records within buildings
  name: WegoWise Apartments API
  slug: wegowise-apartments-api
- description: Manage commercial building area records
  name: WegoWise Areas API
  slug: wegowise-areas-api
- description: Manage building records in a portfolio
  name: WegoWise Buildings API
  slug: wegowise-buildings-api
- description: Manage development (property portfolio group) records
  name: WegoWise Developments API
  slug: wegowise-developments-api
- description: Track utility meters for buildings, apartments, and areas
  name: WegoWise Meters API
  slug: wegowise-meters-api
- description: Retrieve and submit raw and aggregated utility usage datapoints
  name: WegoWise Usage Data API
  slug: wegowise-usage-data-api
- description: Public list of supported utility companies
  name: WegoWise Utility Companies API
  slug: wegowise-utility-companies-api
- description: Manage automated utility data import credentials
  name: WegoWise Utility Logins API
  slug: wegowise-utility-logins-api
artifact_total: 26
collections:
- collection_type: open
  name: WegoWise API
  slug: open-wegowise
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wegowise-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wegowise-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wegowise-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wegowise
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wegowise-inc
- group: docs
  title: ''
  type: Documentation
  url: https://www.wegowise.com/api
- group: company
  title: ''
  type: Website
  url: https://www.wegowise.com
- group: other
  title: ''
  type: Product Tour
  url: https://www.wegowise.com/tour
- group: other
  title: ''
  type: Energy Service Providers
  url: https://www.wegowise.com/customer-profiles/energy-service-providers
- group: auth
  title: ''
  type: Compliance
  url: https://www.wegowise.com/compliance
- group: company
  title: ''
  type: Blog
  url: http://blog.wegowise.com/
- group: design
  title: ''
  type: SpectralRules
  url: rules/wegowise-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wegowise-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/wegowise-context.jsonld
created: '2025-05-02'
description: WegoWise (now Comply by Measurabl) is a building energy and water benchmarking platform enabling property owners, managers, and energy service providers to programmatically manage building portfolios, track utility meter data, and benchmark energy and water performance. The REST API supports building management, apartment and commercial area tracking, utility meter data import, and normalized monthly usage analytics across multifamily and commercial properties.
examples:
- key_count: 4
  name: Wegowise Building Data Example
  slug: wegowise-building-data-example
- key_count: 4
  name: Wegowise List Buildings Example
  slug: wegowise-list-buildings-example
finops:
- name: Wegowise Finops
  service_category: Building Energy / Benchmarking SaaS
  slug: wegowise-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wegowise.png
json_schemas:
- name: WegoWise Building
  property_count: 11
  slug: wegowise-building
- name: WegoWise Utility Meter
  property_count: 10
  slug: wegowise-meter
json_structures:
- name: Wegowise Building Structure
  property_count: 0
  slug: wegowise-building-structure
jsonld:
- class_count: 0
  name: Wegowise Context
  property_count: 24
  slug: wegowise-context
layout: provider
modified: '2026-05-19'
name: WegoWise
nav: Providers
network: true
overview: 'WegoWise publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Apartments API, Areas API, Buildings API, and 5 more. Tagged areas include Benchmarking, Building Energy, Energy Efficiency, Multifamily, and Property Management.


  The WegoWise catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WegoWise''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Wegowise Plans Pricing
  plan_count: 1
  slug: wegowise-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 1
  name: Wegowise Rate Limits
  slug: wegowise-rate-limits
rules:
- name: WegoWise API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wegowise-jsonschema-spectral-rules
- name: WegoWise API Rules
  rule_count: 12
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 10
  slug: wegowise-rules
score:
  band: thin
  composite: 41.5
  delta: -8.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 75.7
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 29.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/wegowise/refs/heads/main/screenshots/wegowise-2026-06-20T201345.png
security:
- kind: authentication
  name: Wegowise Authentication
  slug: wegowise-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wegowise Domain Security
  slug: wegowise-domain-security
  summary_line: TLSv1.2
slug: wegowise
tags:
- Benchmarking
- Building Energy
- Energy Efficiency
- Multifamily
- Property Management
- Utility Data
website: https://www.wegowise.com
---
