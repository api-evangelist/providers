---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sentera Agentic Access
  operation_count: 2
  slug: sentera-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.sentera.com/graphql
  baseurl_source: declared
  description: The Graph QL API from Sentera — 1 operation(s) for graph ql.
  name: Sentera Graph QL API
  slug: sentera-graph-ql-api
artifact_total: 11
collections:
- collection_type: open
  name: Sentera FieldAgent GraphQL API
  slug: open-sentera-graphql-api
- collection_type: open
  name: Sentera FieldAgent API
  slug: open-sentera
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/deere/
- group: agent
  href: https://artifacts.apis.io/sentera/agentic-access/sentera-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sentera-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sentera/security/sentera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sentera-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sentera/authentication/sentera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sentera-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sentera
- group: company
  title: ''
  type: Website
  url: https://sentera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.sentera.com/api/getting_started/introduction.html
- group: commercial
  href: https://artifacts.apis.io/sentera/plans/sentera-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sentera-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sentera/rate-limits/sentera-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sentera-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sentera/finops/sentera-finops.yml
  title: ''
  type: FinOps
  url: finops/sentera-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://sentera.com/feed/
created: '2026-06-20'
description: Sentera is a precision-agriculture company building aerial imagery sensors, drones, and the FieldAgent platform for capturing, processing, and analyzing in-season field data. The FieldAgent API is a single-endpoint GraphQL interface (https://api.sentera.com/graphql) that gives customers and integration partners programmatic access to fields, surveys, flight tasks, imagery, mosaics, plot analytics, and orders. Sentera was acquired by John Deere in 2025.
finops:
- has_sources: true
  method: generated
  name: Sentera Finops
  primary_unit: ''
  service_category: Precision Agriculture and Geospatial Analytics
  slug: sentera-finops
  template: false
graphqls:
- description: Sentera's FieldAgent API is a **GraphQL** API, not a resource-oriented REST API.
  name: Sentera FieldAgent GraphQL API
  slug: sentera-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sentera.png
layout: provider
modified: '2026-06-20'
name: Sentera
nav: Providers
network: true
overview: 'Sentera publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Graph QL API. Tagged areas include Precision Agriculture, Aerial Imagery, Drones, Sensors, and Analytics.


  The Sentera catalog on APIs.io includes 1 Spectral governance ruleset.


  Sentera''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sentera Plans Pricing
  plan_count: 3
  slug: sentera-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Sentera Rate Limits
  slug: sentera-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Sentera API Rules
  rule_count: 56
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 1
  slug: sentera-rules
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 51.4
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sentera/sentera-2026-06-20T193707.png
security:
- kind: authentication
  name: Sentera Authentication
  slug: sentera-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sentera Domain Security
  slug: sentera-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: sentera
tags:
- Precision Agriculture
- Aerial Imagery
- Drones
- Sensors
- Analytics
- GraphQL
website: https://sentera.com/
---
