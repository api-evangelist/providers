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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Wegowise Agentic Access
  operation_count: 33
  slug: wegowise-agentic-access
  summary_line: 33 operations · 16 acting
api_count: 1
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
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Manage apartment and unit records within buildings
  name: WegoWise Apartments API
  slug: wegowise-apartments-api
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Manage commercial building area records
  name: WegoWise Areas API
  slug: wegowise-areas-api
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Manage building records in a portfolio
  name: WegoWise Buildings API
  slug: wegowise-buildings-api
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Manage development (property portfolio group) records
  name: WegoWise Developments API
  slug: wegowise-developments-api
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Track utility meters for buildings, apartments, and areas
  name: WegoWise Meters API
  slug: wegowise-meters-api
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Retrieve and submit raw and aggregated utility usage datapoints
  name: WegoWise Usage Data API
  slug: wegowise-usage-data-api
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Public list of supported utility companies
  name: WegoWise Utility Companies API
  slug: wegowise-utility-companies-api
- baseURL: https://www.wegowise.com
  baseurl_source: spec
  description: Manage automated utility data import credentials
  name: WegoWise Utility Logins API
  slug: wegowise-utility-logins-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WegoWise Apartments API
  slug: open-wegowise-apartments-api
- collection_type: open
  name: WegoWise Apartments Areas API
  slug: open-wegowise-areas-api
- collection_type: open
  name: WegoWise Apartments Buildings API
  slug: open-wegowise-buildings-api
- collection_type: open
  name: WegoWise Apartments Developments API
  slug: open-wegowise-developments-api
- collection_type: open
  name: WegoWise Apartments Meters API
  slug: open-wegowise-meters-api
- collection_type: open
  name: WegoWise Apartments Usage Data API
  slug: open-wegowise-usage-data-api
- collection_type: open
  name: WegoWise Apartments Utility Companies API
  slug: open-wegowise-utility-companies-api
- collection_type: open
  name: WegoWise Apartments Utility Logins API
  slug: open-wegowise-utility-logins-api
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
random_paper: 13
rate_limits:
- limit_count: 1
  name: Wegowise Rate Limits
  slug: wegowise-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: WegoWise API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wegowise-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: WegoWise API Rules
  rule_count: 12
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 10
  slug: wegowise-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 16
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 28.8
    contract_quality: 72.4
    developer_ergonomics: 22.6
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 38.8
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
