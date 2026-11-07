---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bykaranteli Agentic Access
  operation_count: 14
  slug: bykaranteli-agentic-access
  summary_line: 14 operations
api_count: 2
apis:
- baseURL: https://bykaranteli.com
  baseurl_source: spec
  description: Per-call priced history and depth endpoints, settled in USDC over the x402 protocol on Solana and Base mainnet through the Coinbase CDP facilitator. 13 priced endpoints plus the free catalog at /api/x
  name: ByKaranteli X402 API
  slug: bykaranteli-x402-api
- baseURL: https://bykaranteli.com
  baseurl_source: spec
  description: 'The free, no-key public REST surface — 10 endpoints under /api/v1/public/ described by the provider''s own self-describing manifest, plus the /api/public/ index endpoints. Verified 2026-08-11: unauthen'
  name: ByKaranteli Public API
  slug: bykaranteli-public-api
- baseURL: https://bykaranteli.com
  baseurl_source: declared
  description: The Public API from ByKaranteli — 68 operation(s) for public.
  name: ByKaranteli Public API
  slug: bykaranteli-public-api
- baseURL: https://bykaranteli.com
  baseurl_source: declared
  description: The Series API from ByKaranteli — 2 operation(s) for series.
  name: ByKaranteli Series API
  slug: bykaranteli-series-api
- baseURL: https://bykaranteli.com
  baseurl_source: declared
  description: The Usage API from ByKaranteli — 1 operation(s) for usage.
  name: ByKaranteli Usage API
  slug: bykaranteli-usage-api
artifact_total: 26
collections:
- collection_type: open
  name: ByKaranteli crypto derivatives data X402 API
  slug: open-bykaranteli-x402-api
common:
- group: other
  href: https://artifacts.apis.io/bykaranteli/capabilities/bykaranteli-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/bykaranteli-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/bykaranteli/plans/bykaranteli-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bykaranteli-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/bykaranteli/plans/bykaranteli-plans.yml
  title: ''
  type: Plans
  url: plans/bykaranteli-plans.yml
- group: operate
  href: https://artifacts.apis.io/bykaranteli/rate-limits/bykaranteli-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bykaranteli-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bykaranteli/finops/bykaranteli-finops.yml
  title: ''
  type: FinOps
  url: finops/bykaranteli-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://bykaranteli.com/pricing
- group: company
  title: ''
  type: BlogRSS
  url: https://bykaranteli.com/feed.xml
- group: other
  title: ''
  type: APIsJSON
  url: https://bykaranteli.com/apis.json
- group: other
  title: ''
  type: APIsJSON
  url: https://bykaranteli.com/.well-known/apis.json
- group: design
  href: https://artifacts.apis.io/bykaranteli/rules/bykaranteli-rules.yml
  title: ''
  type: Spectral
  url: rules/bykaranteli-rules.yml
- group: other
  href: https://artifacts.apis.io/bykaranteli/a2a/bykaranteli-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bykaranteli-a2a.yml
- group: other
  href: https://artifacts.apis.io/bykaranteli/hosts/bykaranteli-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bykaranteli-hosts.yml
- group: other
  href: https://artifacts.apis.io/bykaranteli/vendors/bykaranteli-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bykaranteli-vendors.yml
- group: build
  href: https://artifacts.apis.io/bykaranteli/packages/bykaranteli-packages.yml
  title: ''
  type: SDKs
  url: packages/bykaranteli-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bykaranteli.com/terms
- group: auth
  title: ''
  type: Security
  url: https://bykaranteli.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bykaranteli.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://bykaranteli.com/newsroom
- group: auth
  href: https://artifacts.apis.io/bykaranteli/security/bykaranteli-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bykaranteli-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.bykaranteli.com/
- group: agent
  href: https://artifacts.apis.io/bykaranteli/mcp/bykaranteli-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bykaranteli-mcp.yml
- group: docs
  title: ''
  type: Documentation
  url: https://bykaranteli.com/developers
- group: agent
  href: https://artifacts.apis.io/bykaranteli/agentic-access/bykaranteli-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bykaranteli-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/bykaranteli/security/bykaranteli-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bykaranteli-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bykaranteli.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://bykaranteli.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://bykaranteli.com/guide
- group: operate
  title: ''
  type: Support
  url: https://t.me/bykaranteli_com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bykarantelicom
- group: commercial
  title: ''
  type: Pricing
  url: https://bykaranteli.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://bykaranteli.com/register
- group: start
  title: ''
  type: Login
  url: https://bykaranteli.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://bykaranteli.com/status
- group: operate
  href: https://artifacts.apis.io/bykaranteli/changelog/bykaranteli-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bykaranteli-changelog.yml
- group: design
  href: https://artifacts.apis.io/bykaranteli/lifecycle/bykaranteli-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bykaranteli-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/bykaranteli/authentication/bykaranteli-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bykaranteli-authentication.yml
- group: design
  href: https://artifacts.apis.io/bykaranteli/conventions/bykaranteli-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bykaranteli-conventions.yml
- group: design
  href: https://artifacts.apis.io/bykaranteli/errors/bykaranteli-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bykaranteli-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/bykaranteli/rate-limits/bykaranteli-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bykaranteli-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/bykaranteli/plans/bykaranteli-plans.yml
  title: ''
  type: Plans
  url: plans/bykaranteli-plans.yml
- group: commercial
  href: https://artifacts.apis.io/bykaranteli/finops/bykaranteli-finops.yml
  title: ''
  type: FinOps
  url: finops/bykaranteli-finops.yml
- group: build
  href: https://artifacts.apis.io/bykaranteli/packages/bykaranteli-packages.yml
  title: ''
  type: Packages
  url: packages/bykaranteli-packages.yml
- group: design
  href: https://artifacts.apis.io/bykaranteli/conformance/bykaranteli-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bykaranteli-conformance.yml
- group: design
  href: https://artifacts.apis.io/bykaranteli/vocabulary/bykaranteli-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bykaranteli-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bykaranteli/components/bykaranteli-components.yml
  title: ''
  type: Components
  url: components/bykaranteli-components.yml
- group: agent
  href: https://artifacts.apis.io/bykaranteli/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: A crypto-derivatives market-structure data platform. Its REST API, which takes a free bearer key from a verified account, surfaces funding rates/arbitrage, open interest, liquidation maps, options (Deribit), ETF flows, order-flow toxicity (VPIN), Coinbase premium, CFTC COT positioning, and Fear & Greed / BTC-dominance indices. It also offers a hosted MCP server, x402 agent-payment endpoints, and CC0 datasets.
examples:
- key_count: 6
  name: Bykaranteli Public Indices
  slug: bykaranteli-public-indices
- key_count: 3
  name: Bykaranteli Public Pressure
  slug: bykaranteli-public-pressure
- key_count: 8
  name: Bykaranteli Public Recent
  slug: bykaranteli-public-recent
- key_count: 4
  name: Bykaranteli V1 Health
  slug: bykaranteli-v1-health
- key_count: 10
  name: Bykaranteli V1 Leaderboard
  slug: bykaranteli-v1-leaderboard
- key_count: 5
  name: Bykaranteli X402 Payment Required
  slug: bykaranteli-x402-payment-required
finops:
- has_sources: true
  method: searched
  name: Bykaranteli Finops
  primary_unit: ''
  service_category: ''
  slug: bykaranteli-finops
  template: false
image: https://bykaranteli.com/brand/icon-192.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.bykaranteli.com over HTTP; 20 tools listed.
  name: ByKaranteli MCP Server
  slug: bykaranteli
modified: '2026-10-06'
name: ByKaranteli
nav: Providers
network: true
overview: 'ByKaranteli publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including X402 API, Public API, and 3 more. Tagged areas include Cryptocurrency, Crypto Derivatives, Market Data, Funding Rates, and Open Interest.


  The ByKaranteli catalog on APIs.io includes 1 Spectral governance ruleset.


  ByKaranteli''s developer surface includes pricing, documentation, API reference, getting-started guide, support, signup flow, changelog, and 39 more developer resources.'
plans:
- name: Bykaranteli Plans Pricing
  plan_count: 12
  slug: bykaranteli-plans-pricing
- name: Bykaranteli Plans
  plan_count: 5
  slug: bykaranteli-plans
- name: Bykaranteli Price Estimates
  plan_count: 0
  slug: bykaranteli-price-estimates
random_paper: 22
rate_limits:
- limit_count: 2
  name: Bykaranteli Rate Limits
  slug: bykaranteli-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: ByKaranteli API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: bykaranteli-rules
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 35
    catalog_earned: 61.5
    catalog_earned_first_party: 25.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 65.8
    contract_governance: 33.3
    contract_quality: 53.4
    developer_ergonomics: 63.7
    discoverability: 67.5
    operational_transparency: 60.5
  previous_composite: 62.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/bykaranteli/bykaranteli-2026-08-17T080800.png
security:
- kind: authentication
  name: Bykaranteli Authentication
  slug: bykaranteli-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Bykaranteli Domain Security
  slug: bykaranteli-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bykaranteli Vulnerability Disclosure
  slug: bykaranteli-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: bykaranteli-funding-carry-scan
  slug: bykaranteli-funding-carry-scan
- name: bykaranteli-liquidation-forensics
  slug: bykaranteli-liquidation-forensics
- name: bykaranteli-x402-pay-per-call
  slug: bykaranteli-x402-pay-per-call
slug: bykaranteli
tags:
- Cryptocurrency
- Crypto Derivatives
- Market Data
- Funding Rates
- Open Interest
- Liquidations
- Options
- ETF Flows
- Financial Data
- MCP
- x402
- Agents
website: https://www.bykaranteli.com/
---
