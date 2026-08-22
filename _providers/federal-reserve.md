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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Reserve Agentic Access
  operation_count: 13
  slug: federal-reserve-agentic-access
  summary_line: 13 operations
api_count: 8
apis:
- description: The Category API from Federal Reserve — 3 operation(s) for category.
  name: Federal Reserve Category API
  slug: federal-reserve-category-api
- description: The Related Tags API from Federal Reserve — 1 operation(s) for related tags.
  name: Federal Reserve Related Tags API
  slug: federal-reserve-related-tags-api
- description: The Release API from Federal Reserve — 2 operation(s) for release.
  name: Federal Reserve Release API
  slug: federal-reserve-release-api
- description: The Releases API from Federal Reserve — 1 operation(s) for releases.
  name: Federal Reserve Releases API
  slug: federal-reserve-releases-api
- description: The Series API from Federal Reserve — 3 operation(s) for series.
  name: Federal Reserve Series API
  slug: federal-reserve-series-api
- description: The Source API from Federal Reserve — 1 operation(s) for source.
  name: Federal Reserve Source API
  slug: federal-reserve-source-api
- description: The Sources API from Federal Reserve — 1 operation(s) for sources.
  name: Federal Reserve Sources API
  slug: federal-reserve-sources-api
- description: The Tags API from Federal Reserve — 1 operation(s) for tags.
  name: Federal Reserve Tags API
  slug: federal-reserve-tags-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Federal Reserve FRED Category API
  slug: open-federal-reserve-category-api
- collection_type: open
  name: Federal Reserve FRED API
  slug: open-federal-reserve-fred
- collection_type: open
  name: Federal Reserve FRED Category Related Tags API
  slug: open-federal-reserve-related-tags-api
- collection_type: open
  name: Federal Reserve FRED Category Release API
  slug: open-federal-reserve-release-api
- collection_type: open
  name: Federal Reserve FRED Category Releases API
  slug: open-federal-reserve-releases-api
- collection_type: open
  name: Federal Reserve FRED Category Series API
  slug: open-federal-reserve-series-api
- collection_type: open
  name: Federal Reserve FRED Category Source API
  slug: open-federal-reserve-source-api
- collection_type: open
  name: Federal Reserve FRED Category Sources API
  slug: open-federal-reserve-sources-api
- collection_type: open
  name: Federal Reserve FRED Category Tags API
  slug: open-federal-reserve-tags-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-reserve-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-reserve-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/federal-reserve-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-reserve-board
- group: company
  title: ''
  type: Website
  url: https://www.federalreserve.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://fred.stlouisfed.org/docs/api/fred
- group: company
  title: ''
  type: Blog
  url: https://www.federalreserve.gov/feeds/press_all.xml
created: '2024-12-03'
description: The FRED API is a web service that allows developers to write programs and build applications that retrieve economic data from the FRED and ALFRED websites hosted by the Economic Research Division of the Federal Reserve Bank of St. Louis.
finops:
- name: Federal Reserve Finops
  service_category: API
  slug: federal-reserve-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-reserve.png
layout: provider
modified: '2026-05-19'
name: Federal Reserve
nav: Providers
network: true
overview: 'Federal Reserve publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Category API, Related Tags API, Release API, and 5 more. Tagged areas include Economics, Federal Government, and Finance.


  Federal Reserve''s developer surface includes authentication, documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Federal Reserve Plans Pricing
  plan_count: 3
  slug: federal-reserve-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Federal Reserve Rate Limits
  slug: federal-reserve-rate-limits
score:
  band: thin
  composite: 27.6
  delta: 0.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 23.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.0
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
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-reserve/refs/heads/main/screenshots/federal-reserve-2026-06-20T181129.png
security:
- kind: authentication
  name: Federal Reserve Authentication
  slug: federal-reserve-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Federal Reserve Domain Security
  slug: federal-reserve-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: federal-reserve
tags:
- Economics
- Federal Government
- Finance
website: https://www.federalreserve.gov/
---
