---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: The Index Fyi Agentic Access
  operation_count: 4
  slug: the-index-fyi-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Approved indie web and small web index sites.
  name: The Index Indexes API
  slug: the-index-fyi-indexes-api
artifact_total: 7
collections:
- collection_type: open
  name: theindex.fyi
  slug: open-the-index-fyi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-index-fyi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-index-fyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://theindex.fyi/
- group: company
  title: ''
  type: AboutUs
  url: https://theindex.fyi/about
- group: docs
  title: ''
  type: Documentation
  url: https://theindex.fyi/api/docs
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/the-index-fyi-openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/the-index-fyi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/the-index-fyi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/the-index-fyi-finops.yml
created: '2026-05-23'
description: theindex.fyi is a maintained meta-index of indie web and small web index sites — a curated catalog of curated catalogs. It tracks ~40 indexes spanning six categories (curated directories, RSS / feed aggregators, search engines, random-discovery tools, constraint-based clubs, and IndieWeb infrastructure), and exposes the catalog through a public, read-only JSON:API.
finops:
- name: The Index Fyi Finops
  service_category: API
  slug: the-index-fyi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-index-fyi.png
layout: provider
modified: '2026-05-23'
name: The Index
nav: Providers
network: true
overview: 'The Index publishes 1 API on the [APIs.io](https://apis.io/) network: Indexes API. Tagged areas include Indie Web, Small Web, Directories, Search, and RSS.


  The Index''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: The Index Fyi Plans Pricing
  plan_count: 1
  slug: the-index-fyi-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 2
  name: The Index Fyi Rate Limits
  slug: the-index-fyi-rate-limits
score:
  band: thin
  composite: 29.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.4
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/the-index-fyi/refs/heads/main/screenshots/the-index-fyi-2026-06-20T195220.png
security:
- kind: domain-security
  name: The Index Fyi Domain Security
  slug: the-index-fyi-domain-security
  summary_line: TLSv1.3
slug: the-index-fyi
tags:
- Indie Web
- Small Web
- Directories
- Search
- RSS
- Webrings
- Open Data
- JSON:API
website: https://theindex.fyi/
---
