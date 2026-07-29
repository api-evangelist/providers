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
- acting_count: 6
  human_in_the_loop: 0
  name: Messari Agentic Access
  operation_count: 42
  slug: messari-agentic-access
  summary_line: 42 operations · 6 acting
api_count: 12
apis:
- description: Comprehensive REST API exposing /v1, /v2 endpoints for asset metrics (price, market cap, ROI, mining stats, supply, developer activity, ROI), markets, news, Token Unlocks, screener, and curated intel.
  name: Messari REST API
  slug: rest-api
- description: The AI API from Messari — 4 operation(s) for ai.
  name: Messari AI API
  slug: messari-ai-api
- description: The Assets API from Messari — 7 operation(s) for assets.
  name: Messari Assets API
  slug: messari-assets-api
- description: The Datasets API from Messari — 2 operation(s) for datasets.
  name: Messari Datasets API
  slug: messari-datasets-api
- description: The Exchanges API from Messari — 2 operation(s) for exchanges.
  name: Messari Exchanges API
  slug: messari-exchanges-api
- description: The Markets API from Messari — 4 operation(s) for markets.
  name: Messari Markets API
  slug: messari-markets-api
- description: The Monitoring API from Messari — 3 operation(s) for monitoring.
  name: Messari Monitoring API
  slug: messari-monitoring-api
- description: The Networks API from Messari — 3 operation(s) for networks.
  name: Messari Networks API
  slug: messari-networks-api
- description: The News API from Messari — 5 operation(s) for news.
  name: Messari News API
  slug: messari-news-api
- description: The Protocols API from Messari — 5 operation(s) for protocols.
  name: Messari Protocols API
  slug: messari-protocols-api
- description: The Research API from Messari — 3 operation(s) for research.
  name: Messari Research API
  slug: messari-research-api
- description: The Token Unlocks API from Messari — 2 operation(s) for token unlocks.
  name: Messari Token Unlocks API
  slug: messari-token-unlocks-api
artifact_total: 19
collections:
- collection_type: open
  name: Messari API
  slug: open-messari
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/messari-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/messari-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/messari-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/messari
- group: start
  title: ''
  type: Portal
  url: https://messari.io/
- group: docs
  title: ''
  type: Documentation
  url: https://messari.io/api/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://messari.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/messari
- group: commercial
  title: ''
  type: Plans
  url: plans/messari-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/messari-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/messari-finops.yml
created: '2026-05-08'
description: Messari provides crypto research, analytics, fundamentals, intelligence, and asset profiles through a REST API at data.messari.io. Endpoints cover assets metrics, market data, news, Token Unlocks, screener, governance, treasuries, and AI-powered Messari Copilot. Authentication is via the x-messari-api-key header.
finops:
- name: Messari Finops
  service_category: Crypto Research
  slug: messari-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/messari.png
layout: provider
modified: '2026-05-08'
name: Messari
nav: Providers
network: true
overview: 'Messari publishes 11 APIs on the [APIs.io](https://apis.io/) network, including AI API, Assets API, Datasets API, and 8 more. Tagged areas include Web3, Crypto, Research, Analytics, and Asset Data.


  Messari''s developer surface includes authentication, developer portal, documentation, pricing, GitHub presence, and 6 more developer resources.'
plans:
- name: Messari Plans Pricing
  plan_count: 3
  slug: messari-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 4
  name: Messari Rate Limits
  slug: messari-rate-limits
score:
  band: thin
  composite: 40.4
  delta: -2.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.0
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Messari Authentication
  slug: messari-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Messari Domain Security
  slug: messari-domain-security
  summary_line: TLSv1.3 · DMARC
slug: messari
tags:
- Web3
- Crypto
- Research
- Analytics
- Asset Data
- Fundamentals
- News
- Token Unlocks
website: https://messari.io/
---
