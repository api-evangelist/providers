---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
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
  name: Auto Dev Agentic Access
  operation_count: 5
  slug: auto-dev-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: The Dealers API from Auto.dev — 1 operation(s) for dealers.
  name: Auto.dev Dealers API
  slug: auto-dev-dealers-api
- description: The Listings API from Auto.dev — 2 operation(s) for listings.
  name: Auto.dev Listings API
  slug: auto-dev-listings-api
- description: The Market Value API from Auto.dev — 1 operation(s) for market value.
  name: Auto.dev Market Value API
  slug: auto-dev-market-value-api
- description: The Recalls API from Auto.dev — 1 operation(s) for recalls.
  name: Auto.dev Recalls API
  slug: auto-dev-recalls-api
- description: The VIN Decoding API from Auto.dev — 2 operation(s) for vin decoding.
  name: Auto.dev VIN Decoding API
  slug: auto-dev-vin-decoding-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Auto.dev Dealers API
  slug: open-auto-dev-dealers-api
- collection_type: open
  name: Auto.dev Dealers Listings API
  slug: open-auto-dev-listings-api
- collection_type: open
  name: Auto.dev Dealers Market Value API
  slug: open-auto-dev-market-value-api
- collection_type: open
  name: Auto.dev Dealers Recalls API
  slug: open-auto-dev-recalls-api
- collection_type: open
  name: Auto.dev Dealers VIN Decoding API
  slug: open-auto-dev-vin-decoding-api
- collection_type: open
  name: Auto.dev API
  slug: open-auto-dev
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/auto-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/auto-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/auto-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/drivly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auto-dev
- group: company
  title: ''
  type: Website
  url: https://www.auto.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.auto.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/auto-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/auto-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/auto-dev-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.auto.dev/blog/rss.xml
created: '2026-06-21'
description: Auto.dev provides automotive data APIs for developers and AI agents, including global VIN decoding, used-car vehicle listings with real-time market pricing and dealer data, vehicle specifications, photos, and NHTSA safety recalls. The REST API is served from https://api.auto.dev with API key authentication.
finops:
- name: Auto Dev Finops
  service_category: Web and Data
  slug: auto-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/auto-dev.png
layout: provider
modified: '2026-06-21'
name: Auto.dev
nav: Providers
network: true
overview: 'Auto.dev publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Dealers API, Listings API, Market Value API, and 2 more. Tagged areas include Automotive, Vehicle Data, VIN Decoding, Vehicle Listings, and Recalls.


  Auto.dev''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Auto Dev Plans Pricing
  plan_count: 3
  slug: auto-dev-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Auto Dev Rate Limits
  slug: auto-dev-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -0.9
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/auto-dev/refs/heads/main/screenshots/auto-dev-2026-07-25T201815.png
security:
- kind: authentication
  name: Auto Dev Authentication
  slug: auto-dev-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Auto Dev Domain Security
  slug: auto-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auto-dev
tags:
- Automotive
- Vehicle Data
- VIN Decoding
- Vehicle Listings
- Recalls
website: https://www.auto.dev
---
