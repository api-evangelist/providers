---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Finnhub Agentic Access
  operation_count: 15
  slug: finnhub-agentic-access
  summary_line: 15 operations
api_count: 2
apis:
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The Company News API from Finnhub — 1 operation(s) for company news.
  name: Finnhub Company News API
  slug: finnhub-company-news-api
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The Crypto API from Finnhub — 3 operation(s) for crypto.
  name: Finnhub Crypto API
  slug: finnhub-crypto-api
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The Forex API from Finnhub — 3 operation(s) for forex.
  name: Finnhub Forex API
  slug: finnhub-forex-api
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The News API from Finnhub — 1 operation(s) for news.
  name: Finnhub News API
  slug: finnhub-news-api
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The Quote API from Finnhub — 1 operation(s) for quote.
  name: Finnhub Quote API
  slug: finnhub-quote-api
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The Search API from Finnhub — 1 operation(s) for search.
  name: Finnhub Search API
  slug: finnhub-search-api
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The Stock API from Finnhub — 5 operation(s) for stock.
  name: Finnhub Stock API
  slug: finnhub-stock-api
- baseURL: https://finnhub.io/api/v1
  baseurl_source: declared
  description: The Default API from Finnhub — 117 operation(s) for default.
  name: Finnhub Default API
  slug: finnhub-default-api
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
  type: X-MCPServerCandidate
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
modified: '2026-07-22'
name: Finnhub
nav: Providers
network: true
overview: 'Finnhub publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Company News API, Crypto API, Forex API, and 5 more. Tagged areas include Financial, Market Data, Stocks, Forex, and Cryptocurrency.


  The Finnhub catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Finnhub''s developer surface includes authentication, documentation, API reference, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Finnhub Plans Pricing
  plan_count: 3
  slug: finnhub-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Finnhub Rate Limits
  slug: finnhub-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Finnhub API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: finnhub-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 15.9
    contract_quality: 55.7
    developer_ergonomics: 43.5
    discoverability: 68.5
    governance: 15.9
    operational_transparency: 10.5
  previous_composite: 44.2
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
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
