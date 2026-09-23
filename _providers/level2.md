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
    agent_skills: derived
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
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Level2 Agentic Access
  operation_count: 15
  slug: level2-agentic-access
  summary_line: 15 operations · 7 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://hub2.trylevel2.com
  baseurl_source: declared
  description: The live Level2 platform API — a single FastAPI service carrying 301 operations across the end-user surface (visual strategy canvas, backtesting, live and virtual deployment, market scanners, the stra
  name: Level2 Hub API
  slug: level2-hub-api
- baseURL: https://api.trylevel2.com/v1
  baseurl_source: declared
  description: Endpoints for running backtests on strategies against historical market data to validate performance before live deployment.
  name: level2 Backtesting API
  slug: level2-backtesting-api
- baseURL: https://app.bytemine.io/api
  baseurl_source: declared
  description: Endpoints for discovering similar stocks and retrieving company fundamental summaries.
  name: level2 Discovery API
  slug: level2-discovery-api
- baseURL: https://app.bytemine.io/api
  baseurl_source: declared
  description: Endpoints for retrieving historical OHLC price data for financial instruments across global exchanges.
  name: level2 Market Data API
  slug: level2-market-data-api
- baseURL: https://api.trylevel2.com/v1
  baseurl_source: declared
  description: Endpoints for managing user trading strategies, including creation, retrieval, updating, deployment, and deletion of automated trading strategies built with the Level2 visual strategy builder.
  name: level2 Strategies API
  slug: level2-strategies-api
- baseURL: https://app.bytemine.io/api
  baseurl_source: declared
  description: Endpoints for detecting candlestick patterns and analyzing ticker trends using technical indicators.
  name: level2 Technical Analysis API
  slug: level2-technical-analysis-api
- baseURL: https://api.trylevel2.com/v1
  baseurl_source: declared
  description: Endpoints for managing broker user accounts and their association with the Level2 platform.
  name: level2 Users API
  slug: level2-users-api
artifact_total: 26
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
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/agentic-access/level2-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/level2-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/security/level2-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/level2-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/security/level2-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/level2-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/authentication/level2-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/json-ld/level2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/level2-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/json-schema/level2-strategy-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/level2-strategy-schema.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/llms/level2-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/level2-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/well-known/level2-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/level2-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/well-known/level2-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/level2-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.trylevel2.com/security
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/mcp/level2-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/level2-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/overlays/level2-hub-controller-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/level2-hub-controller-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/conformance/level2-conformance.yml
  title: ''
  type: Conformance
  url: conformance/level2-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/errors/level2-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/level2-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/lifecycle/level2-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/level2-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/conventions/level2-conventions.yml
  title: ''
  type: Conventions
  url: conventions/level2-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/sandbox/level2-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/level2-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/components/level2-components.yml
  title: ''
  type: Components
  url: components/level2-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/data-model/level2-data-model.yml
  title: ''
  type: DataModel
  url: data-model/level2-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/packages/level2-packages.yml
  title: ''
  type: Packages
  url: packages/level2-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/plans/level2-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/level2-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/rate-limits/level2-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/level2-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/rules/level2-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/level2-jsonschema-spectral-rules.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/finops/level2-finops.yml
  title: ''
  type: FinOps
  url: finops/level2-finops.yml
- group: build
  title: ''
  type: Postman
  url: https://learn.trylevel2.com/broker_apis.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.trylevel2.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.trylevel2.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.trylevel2.com/docs/Broker/API/broker-api
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.trylevel2.com/docs/Broker/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.trylevel2.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.trylevel2.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.trylevel2.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trylevel2.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trylevel2.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bytemine-io
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@trylevel2
created: '2026-05-04'
description: 'Level2 is a no-code systematic-trading platform from Bytemine Technologies Ltd that lets active retail traders build, backtest and deploy fully automated strategies from a visual drag-and-drop canvas, with no code and no proprietary scripting language. Strategies can be rehearsed against historical data or paper-traded with virtual funds before being deployed live through a connected brokerage account. Level2 also sells the platform to brokers and prop firms as an embeddable surface: a customised iframe of the strategy builder, four standalone market widgets, and the Level2 Hub Broker API, which lets a broker register and manage its own customers'' Level2 accounts, read their strategies, deployments, trades and backtests, and measure their execution latency and slippage.'
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
modified: '2026-09-17'
name: Level2
nav: Providers
network: true
overview: 'Level2 publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Hub API, Backtesting API, Discovery API, and 4 more. Tagged areas include Trading, Fintech, Financial-Services, Automation, and No-Code.


  The Level2 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Level2''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, pricing, and 32 more developer resources.'
plans:
- name: Level2 Plans Pricing
  plan_count: 3
  slug: level2-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
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
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 63.3
    catalog_earned_first_party: 12.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 14.4
    contract_quality: 59.5
    developer_ergonomics: 68.5
    discoverability: 81.5
    operational_transparency: 13.2
  previous_composite: 63.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 61.7
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/level2/refs/heads/main/screenshots/level2-2026-06-20T184439.png
security:
- kind: authentication
  name: Level2 Authentication
  slug: level2-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Level2 Domain Security
  slug: level2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Level2 Vulnerability Disclosure
  slug: level2-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: level2
tags:
- Trading
- Fintech
- Financial-Services
- Automation
- No-Code
- Backtesting
- Strategies
- Brokerage
- Market Data
- Prediction Markets
website: https://www.trylevel2.com
---
