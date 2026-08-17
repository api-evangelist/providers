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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Finnhub Agentic Access
  operation_count: 15
  slug: finnhub-agentic-access
  summary_line: 15 operations
api_count: 7
apis:
- description: The Company News API from Finnhub — 1 operation(s) for company news.
  name: Finnhub Company News API
  slug: finnhub-company-news-api
- description: The Crypto API from Finnhub — 3 operation(s) for crypto.
  name: Finnhub Crypto API
  slug: finnhub-crypto-api
- description: The Forex API from Finnhub — 3 operation(s) for forex.
  name: Finnhub Forex API
  slug: finnhub-forex-api
- description: The News API from Finnhub — 1 operation(s) for news.
  name: Finnhub News API
  slug: finnhub-news-api
- description: The Quote API from Finnhub — 1 operation(s) for quote.
  name: Finnhub Quote API
  slug: finnhub-quote-api
- description: The Search API from Finnhub — 1 operation(s) for search.
  name: Finnhub Search API
  slug: finnhub-search-api
- description: The Stock API from Finnhub — 5 operation(s) for stock.
  name: Finnhub Stock API
  slug: finnhub-stock-api
artifact_total: 26
asyncapis:
- description: AsyncAPI specification for Finnhub's real-time streaming WebSocket APIs. A single WebSocket endpoint (wss://ws.finnhub.io) multiplexes three documented streams selected by the envelope `type` field on
  name: Finnhub WebSocket API
  slug: finnhub-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Finnhub Company News API
  slug: open-finnhub-company-news-api
- collection_type: open
  name: Finnhub Company News Crypto API
  slug: open-finnhub-crypto-api
- collection_type: open
  name: Finnhub Company News Forex API
  slug: open-finnhub-forex-api
- collection_type: open
  name: Finnhub Company News API
  slug: open-finnhub-news-api
- collection_type: open
  name: Finnhub Company News Quote API
  slug: open-finnhub-quote-api
- collection_type: open
  name: Finnhub Company News Search API
  slug: open-finnhub-search-api
- collection_type: open
  name: Finnhub Company News Stock API
  slug: open-finnhub-stock-api
- collection_type: open
  name: Finnhub API
  slug: open-finnhub-swagger-original
- collection_type: open
  name: Finnhub API
  slug: open-finnhub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/finnhub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finnhub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/finnhub-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/finnhub-swagger-original.json
- group: build
  title: ''
  type: Packages
  url: packages/finnhub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/finnhub-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/finnhub-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/finnhub-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finnhub-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/finnhub-swagger-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/finnhub-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finnhub-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finnhub-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finnhub-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finnhub-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/finnhub-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/finnhub-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/finnhub-finops.yml
- group: build
  title: ''
  type: Postman
  url: collections/finnhub.postman_collection.json
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/finnhub
- group: company
  title: ''
  type: Website
  url: https://finnhub.io/
- group: docs
  title: ''
  type: Documentation
  url: https://finnhub.io/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://finnhub.io/docs/api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Finnhub-Stock-API
- group: operate
  title: ''
  type: Support
  url: mailto:support@finnhub.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finnhub.io/terms-of-service
- group: commercial
  title: ''
  type: Pricing
  url: https://finnhub.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://finnhub.io/register
created: '2025-02-08'
description: With the sole mission of democratizing financial data, we are proud to offer a FREE realtime API for stocks, forex and cryptocurrency. With this API, you can access realtime market data from stock exchanges, 10 forex brokers, and 15+ crypto exchanges.
finops:
- name: Finnhub Finops
  service_category: API
  slug: finnhub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/finnhub.png
layout: provider
mcp_servers:
- description: ''
  name: finnhub-mcp.yml
  slug: finnhub-mcpyml
modified: '2026-07-22'
name: Finnhub
nav: Providers
network: true
overview: 'Finnhub publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Company News API, Crypto API, Forex API, and 4 more. Tagged areas include Financial, Market Data, Stocks, Forex, and Cryptocurrency.


  The Finnhub catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Finnhub''s developer surface includes authentication, documentation, API reference, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Finnhub Plans Pricing
  plan_count: 3
  slug: finnhub-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Finnhub Rate Limits
  slug: finnhub-rate-limits
rules:
- name: Finnhub API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: finnhub-asyncapi-spectral-rules
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 53.1
    operational_transparency: 13.2
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 45.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finnhub/refs/heads/main/screenshots/finnhub-2026-06-20T181219.png
security:
- kind: authentication
  name: Finnhub Authentication
  slug: finnhub-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Finnhub Domain Security
  slug: finnhub-domain-security
  summary_line: TLSv1.2
slug: finnhub
tags:
- Financial
- Market Data
- Stocks
- Forex
- Cryptocurrency
- Fundamentals
- News
- WebSocket
website: https://finnhub.io/
---
