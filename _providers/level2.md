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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Level2 Agentic Access
  operation_count: 15
  slug: level2-agentic-access
  summary_line: 15 operations · 7 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Endpoints for running backtests on strategies against historical market data to validate performance before live deployment.
  name: level2 Backtesting API
  slug: level2-backtesting-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Endpoints for discovering similar stocks and retrieving company fundamental summaries.
  name: level2 Discovery API
  slug: level2-discovery-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Endpoints for retrieving historical OHLC price data for financial instruments across global exchanges.
  name: level2 Market Data API
  slug: level2-market-data-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Endpoints for managing user trading strategies, including creation, retrieval, updating, deployment, and deletion of automated trading strategies built with the Level2 visual strategy builder.
  name: level2 Strategies API
  slug: level2-strategies-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Endpoints for detecting candlestick patterns and analyzing ticker trends using technical indicators.
  name: level2 Technical Analysis API
  slug: level2-technical-analysis-api
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Endpoints for managing broker user accounts and their association with the Level2 platform.
  name: level2 Users API
  slug: level2-users-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Level2 Strategy Builder Backtesting API
  slug: open-level2-backtesting-api
- collection_type: open
  name: Level2 Strategy Builder Backtesting Discovery API
  slug: open-level2-discovery-api
- collection_type: open
  name: Level2 Strategy Builder Backtesting Market Data API
  slug: open-level2-market-data-api
- collection_type: open
  name: Level2 Strategy Builder Backtesting Strategies API
  slug: open-level2-strategies-api
- collection_type: open
  name: Level2 Strategy Builder API
  slug: open-level2-strategy-builder
- collection_type: open
  name: Level2 Strategy Builder Backtesting Technical Analysis API
  slug: open-level2-technical-analysis-api
- collection_type: open
  name: Level2 TradeStation Integration API
  slug: open-level2-tradestation-integration
- collection_type: open
  name: Level2 Strategy Builder Backtesting Users API
  slug: open-level2-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/level2-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/level2-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/level2-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/level2-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mylevel2
- group: company
  title: ''
  type: Website
  url: https://www.trylevel2.com
- group: design
  title: ''
  type: JSONLD
  url: json-ld/level2-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/level2-strategy-schema.json
description: Level2 provides an accessible, intuitive platform for anyone to create, backtest, and deploy fully automated trading strategies—no coding or knowledge of proprietary programming languages required.
finops:
- name: Level2 Finops
  service_category: API
  slug: level2-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/level2.png
json_schemas:
- name: Level2 Trading Strategy
  property_count: 12
  slug: level2-strategy
jsonld:
- class_count: 0
  name: Level2 Context
  property_count: 7
  slug: level2-context
layout: provider
modified: '2026-05-19'
name: Level2
nav: Providers
network: true
overview: 'Level2 publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Backtesting API, Discovery API, Market Data API, and 3 more.


  The Level2 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Level2''s developer surface includes authentication and 7 more developer resources.'
plans:
- name: Level2 Plans Pricing
  plan_count: 3
  slug: level2-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Level2 Rate Limits
  slug: level2-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Level2 API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: level2-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 41.3
    catalog_earned_first_party: 0.0
    catalog_gap: 73.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 59.9
    developer_ergonomics: 21.4
    discoverability: 44.4
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 29.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/screenshots/level2-2026-06-20T184439.png
security:
- kind: authentication
  name: Level2 Authentication
  slug: level2-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Level2 Domain Security
  slug: level2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Level2 Vulnerability Disclosure
  slug: level2-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: level2
website: https://www.trylevel2.com
---
