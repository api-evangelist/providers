---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Cow Protocol Agentic Access
  operation_count: 34
  slug: cow-protocol-agentic-access
  summary_line: 34 operations · 15 acting
api_count: 6
apis:
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Account API from CoW Swap — 1 operation(s) for account.
  name: CoW Swap Account API
  slug: cow-protocol-account-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The App Data API from CoW Swap — 2 operation(s) for app data.
  name: CoW Swap App Data API
  slug: cow-protocol-app-data-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Auction API from CoW Swap — 1 operation(s) for auction.
  name: CoW Swap Auction API
  slug: cow-protocol-auction-api
- baseURL: https://api.cow.fi
  baseurl_source: declared
  description: The Notify API from CoW Swap — 1 operation(s) for notify.
  name: CoW Swap Notify API
  slug: cow-protocol-notify-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Orders API from CoW Swap — 4 operation(s) for orders.
  name: CoW Swap Orders API
  slug: cow-protocol-orders-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Quote API from CoW Swap — 3 operation(s) for quote.
  name: CoW Swap Quote API
  slug: cow-protocol-quote-api
- baseURL: https://api.cow.fi
  baseurl_source: declared
  description: Pay for a quote, then sign and submit an order separately through the orderbook API.
  name: CoW Swap Quotes API
  slug: cow-protocol-quotes-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Restricted API from CoW Swap — 3 operation(s) for restricted.
  name: CoW Swap Restricted API
  slug: cow-protocol-restricted-api
- baseURL: https://api.cow.fi
  baseurl_source: declared
  description: The Reveal API from CoW Swap — 1 operation(s) for reveal.
  name: CoW Swap Reveal API
  slug: cow-protocol-reveal-api
- baseURL: https://api.cow.fi
  baseurl_source: declared
  description: The Settle API from CoW Swap — 1 operation(s) for settle.
  name: CoW Swap Settle API
  slug: cow-protocol-settle-api
- baseURL: https://api.cow.fi
  baseurl_source: declared
  description: The Settle Fast Path API from CoW Swap — 1 operation(s) for settle fast path.
  name: CoW Swap Settle Fast Path API
  slug: cow-protocol-settle-fast-path-api
- baseURL: https://api.cow.fi
  baseurl_source: declared
  description: The Solve API from CoW Swap — 1 operation(s) for solve.
  name: CoW Swap Solve API
  slug: cow-protocol-solve-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Solver Competition API from CoW Swap — 3 operation(s) for solver competition.
  name: CoW Swap Solver Competition API
  slug: cow-protocol-solver-competition-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Token API from CoW Swap — 1 operation(s) for token.
  name: CoW Swap Token API
  slug: cow-protocol-token-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Trades API from CoW Swap — 1 operation(s) for trades.
  name: CoW Swap Trades API
  slug: cow-protocol-trades-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Transactions API from CoW Swap — 1 operation(s) for transactions.
  name: CoW Swap Transactions API
  slug: cow-protocol-transactions-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Users API from CoW Swap — 1 operation(s) for users.
  name: CoW Swap Users API
  slug: cow-protocol-users-api
- baseURL: https://api.cow.fi/mainnet
  baseurl_source: declared
  description: The Version API from CoW Swap — 1 operation(s) for version.
  name: CoW Swap Version API
  slug: cow-protocol-version-api
artifact_total: 42
common:
- group: other
  href: https://artifacts.apis.io/cow-protocol/capabilities/cow-protocol-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cow-protocol-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/cow-protocol/agentic-access/cow-protocol-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cow-protocol-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/cow-protocol/rate-limits/cow-protocol-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cow-protocol-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/cow-protocol/rules/cow-protocol-rules.yml
  title: ''
  type: Spectral
  url: rules/cow-protocol-rules.yml
- group: design
  href: https://artifacts.apis.io/cow-protocol/json-ld/cow-protocol-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cow-protocol-context.jsonld
- group: design
  href: https://artifacts.apis.io/cow-protocol/vocabulary/cow-protocol-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cow-protocol-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cow-protocol/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cow-protocol/data-model/cow-protocol-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cow-protocol-data-model.yml
- group: design
  href: https://artifacts.apis.io/cow-protocol/components/cow-protocol-components.yml
  title: ''
  type: Components
  url: components/cow-protocol-components.yml
- group: design
  href: https://artifacts.apis.io/cow-protocol/errors/cow-protocol-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cow-protocol-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cow-protocol/conformance/cow-protocol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cow-protocol-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cow-protocol/llms/cow-protocol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cow-protocol-llms.txt
- group: other
  href: https://artifacts.apis.io/cow-protocol/hosts/cow-protocol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cow-protocol-hosts.yml
- group: other
  href: https://artifacts.apis.io/cow-protocol/vendors/cow-protocol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cow-protocol-vendors.yml
- group: build
  href: https://artifacts.apis.io/cow-protocol/packages/cow-protocol-packages.yml
  title: ''
  type: SDKs
  url: packages/cow-protocol-packages.yml
- group: build
  href: https://artifacts.apis.io/cow-protocol/packages/cow-protocol-packages.yml
  title: ''
  type: Packages
  url: packages/cow-protocol-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cow.fi/
- group: company
  title: ''
  type: Newsroom
  url: https://cow.fi/learn/topic/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.cow.fi/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cow.fi/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/cow-protocol/security/cow-protocol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cow-protocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cow.fi/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cow.fi/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cowprotocol
created: '2026-10-28'
description: CoW DAO (CoW Swap) is a decentralized finance protocol on Ethereum that enables batch auctions to find the most efficient trades while protecting users from front‑running and MEV. It offers a suite of products including a swap interface, a solver marketplace, and tools for liquidity providers, all governed by the community. The protocol aggregates orders into Coincidence‑of‑Wants (CoW) batches, matching complementary trades to execute at the best price without exposing trade details to the market.
image: https://cow.fi/images/og-meta-cowdao.png
json_schemas:
- name: Auction
  property_count: 9
  slug: cow-protocol-auction
- name: OrderCreation
  property_count: 18
  slug: cow-protocol-order-creation
- name: OrderQuoteRequest
  property_count: 12
  slug: cow-protocol-order-quote-request
- name: OrderQuoteResponse
  property_count: 6
  slug: cow-protocol-order-quote-response
- name: QuoteResponseKind
  property_count: 0
  slug: cow-protocol-quote-response-kind
- name: RevealRequest
  property_count: 2
  slug: cow-protocol-reveal-request
- name: SettleFastPathRequest
  property_count: 5
  slug: cow-protocol-settle-fast-path-request
- name: SettleRequest
  property_count: 3
  slug: cow-protocol-settle-request
- name: SimulationRequest
  property_count: 16
  slug: cow-protocol-simulation-request
- name: Solution
  property_count: 10
  slug: cow-protocol-solution
- name: SolveRequest
  property_count: 5
  slug: cow-protocol-solve-request
- name: SolveResponse
  property_count: 1
  slug: cow-protocol-solve-response
- name: SolverCompetitionResponse
  property_count: 8
  slug: cow-protocol-solver-competition-response
- name: Trade
  property_count: 13
  slug: cow-protocol-trade
jsonld:
- class_count: 96
  name: Cow Protocol Context
  property_count: 218
  slug: cow-protocol-context
layout: provider
modified: '2026-10-28'
name: CoW Swap
nav: Providers
network: true
overview: 'CoW Swap publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, App Data API, Auction API, and 15 more. Tagged areas include DeFi, Ethereum, Swap, Liquidity, and Governance.


  The CoW Swap catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CoW Swap''s developer surface includes API reference, documentation, and 22 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 3
  name: Cow Protocol Rate Limits
  slug: cow-protocol-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: CoW Swap API Rules
  rule_count: 13
  severity_counts:
    error: 7
    hint: 0
    info: 4
    warn: 2
  slug: cow-protocol-rules
scopes:
- name: Cow Protocol Scopes
  scope_count: 0
  slug: cow-protocol-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 54.5
    developer_ergonomics: 26.7
    discoverability: 79.5
    operational_transparency: 42.1
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cow-protocol/cow-protocol-2026-11-03T125453.png
security:
- kind: authentication
  name: Cow Protocol Authentication
  slug: cow-protocol-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cow Protocol Domain Security
  slug: cow-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: driver
  slug: cow-protocol-driver
- name: orderbook
  slug: cow-protocol-orderbook
- name: solver-operations
  slug: solver-operations
slug: cow-protocol
tags:
- DeFi
- Ethereum
- Swap
- Liquidity
- Governance
- AMM
website: https://cow.fi/
---
