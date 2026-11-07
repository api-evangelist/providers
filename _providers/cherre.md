---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Cherre Agentic Access
  operation_count: 2
  slug: cherre-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.cherre.com/graphql
  baseurl_source: declared
  description: The Auth API from Cherre — 1 operation(s) for auth.
  name: Cherre Auth API
  slug: cherre-auth-api
- baseURL: https://api.cherre.com/graphql
  baseurl_source: declared
  description: The Graph QL API from Cherre — 1 operation(s) for graph ql.
  name: Cherre Graph QL API
  slug: cherre-graph-ql-api
artifact_total: 14
collections:
- collection_type: open
  name: Cherre GraphQL Auth API
  slug: open-cherre-auth-api
- collection_type: open
  name: Cherre Auth GraphQL API
  slug: open-cherre-graphql-api
- collection_type: open
  name: Cherre GraphQL API
  slug: open-cherre
common:
- group: agent
  href: https://artifacts.apis.io/cherre/agentic-access/cherre-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cherre-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cherre/security/cherre-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cherre-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cherre/security/cherre-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cherre-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/cherre/authentication/cherre-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cherre-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cherreco
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cherre
- group: company
  title: ''
  type: Website
  url: https://www.cherre.com
- group: docs
  title: ''
  type: Documentation
  url: https://cherre.com/products/platform/
- group: commercial
  href: https://artifacts.apis.io/cherre/plans/cherre-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cherre-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/cherre/rate-limits/cherre-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cherre-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cherre/finops/cherre-finops.yml
  title: ''
  type: FinOps
  url: finops/cherre-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.cherre.com/feed/
created: '2026-06-21'
description: Cherre is a real-estate data-integration and property-intelligence platform that connects, cleans, and resolves public, third-party, and proprietary real-estate datasets - property characteristics, tax and assessments, recorder and deeds, owners, parcel boundaries, and connected portfolio data - and serves them back through a single GraphQL API built on Hasura.
finops:
- has_sources: true
  method: generated
  name: Cherre Finops
  primary_unit: ''
  service_category: Analytics and Data
  slug: cherre-finops
  template: false
graphqls:
- description: Cherre is a real-estate data-integration and property-intelligence platform. It ingests
  name: Cherre GraphQL API
  slug: cherre-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cherre.png
layout: provider
modified: '2026-06-21'
name: Cherre
nav: Providers
network: true
overview: 'Cherre publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Auth API and Graph QL API. Tagged areas include Real Estate, Property Intelligence, Data Integration, Knowledge Graph, and GraphQL.


  The Cherre catalog on APIs.io includes 1 Spectral governance ruleset.


  Cherre''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Cherre Plans Pricing
  plan_count: 3
  slug: cherre-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Cherre Rate Limits
  slug: cherre-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Cherre API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: cherre-rules
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 51.9
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 30.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cherre/cherre-2026-07-25T205151.png
security:
- kind: authentication
  name: Cherre Authentication
  slug: cherre-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cherre Domain Security
  slug: cherre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cherre Trust Center
  slug: cherre-trust-center
  summary_line: SOC 2, ISO 27001
slug: cherre
tags:
- Real Estate
- Property Intelligence
- Data Integration
- Knowledge Graph
- GraphQL
website: https://www.cherre.com
---
