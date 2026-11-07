---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Arbitron App Agentic Access
  operation_count: 20
  slug: arbitron-app-agentic-access
  summary_line: 20 operations
api_count: 1
apis:
- baseURL: https://arbitron.app
  baseurl_source: declared
  description: 'Your own account: cards, trades, PnL, balances and positions, connected exchange accounts, leaderboard place and plan. Needs a key with the `account:read` scope, which is never granted by default. Car'
  name: Arbitron Account API
  slug: arbitron-app-account-api
- baseURL: https://arbitron.app
  baseurl_source: declared
  description: Funding rates on every perpetual contract, one coin across venues, and history by day or by settlement. Rates are percent per settlement; `apr_pct` is annualised.
  name: Arbitron Funding API
  slug: arbitron-app-funding-api
- baseURL: https://arbitron.app
  baseurl_source: declared
  description: Discovery and your key's usage. Authentication, rate limits, caching, errors and versioning are covered in the introduction above.
  name: Arbitron Platform API
  slug: arbitron-app-platform-api
- baseURL: https://arbitron.app
  baseurl_source: declared
  description: 'The venues, the coins and the listings calendar: what exists, what it is called, and what is about to be listed or delisted. Use the names these return to fill the `exchange` and `coin` parameters eve'
  name: Arbitron Reference data API
  slug: arbitron-app-reference-data-api
- baseURL: https://arbitron.app
  baseurl_source: declared
  description: 'Cross-venue spreads on the same coin: the live print from the spread engine, and the scanner''s backtest priced against order-book depth.'
  name: Arbitron Spreads API
  slug: arbitron-app-spreads-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/arbitron-app/agentic-access/arbitron-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arbitron-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/arbitron-app/rate-limits/arbitron-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/arbitron-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/arbitron-app/plans/arbitron-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arbitron-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/arbitron-app/rules/arbitron-app-rules.yml
  title: ''
  type: Spectral
  url: rules/arbitron-app-rules.yml
- group: design
  href: https://artifacts.apis.io/arbitron-app/json-ld/arbitron-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/arbitron-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/arbitron-app/vocabulary/arbitron-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/arbitron-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/arbitron-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/arbitron-app/data-model/arbitron-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arbitron-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/arbitron-app/authentication/arbitron-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arbitron-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/arbitron-app/errors/arbitron-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arbitron-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arbitron-app/conformance/arbitron-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arbitron-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arbitron-app/llms/arbitron-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arbitron-app-llms.txt
- group: build
  href: https://artifacts.apis.io/arbitron-app/mcp/arbitron-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/arbitron-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/arbitron-app/mcp/arbitron-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arbitron-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arbitron-app/well-known/arbitron-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arbitron-app-security.txt
- group: auth
  href: https://artifacts.apis.io/arbitron-app/well-known/arbitron-app-partner-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arbitron-app-partner-security.txt
- group: agent
  href: https://artifacts.apis.io/arbitron-app/well-known/arbitron-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arbitron-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/arbitron-app/hosts/arbitron-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arbitron-app-hosts.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://arbitron.app/funding-rates/coin/trust
- group: auth
  title: ''
  type: Security
  url: https://arbitron.app/security
- group: start
  title: ''
  type: Login
  url: https://arbitron.app/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://arbitron.app/developers
- group: docs
  title: ''
  type: APIReference
  url: https://arbitron.app/developers/reference/
- group: auth
  href: https://artifacts.apis.io/arbitron-app/security/arbitron-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arbitron-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arbitron-app/security/arbitron-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arbitron-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arbitron.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://arbitron.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arbitron.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arbitron.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://arbitron.app/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://arbitron.app/mcp
  - status: 200
    url: https://arbitron.app/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: Arbitron is a non‑custodial automated crypto perpetual‑futures arbitrage platform that scans real‑time order books across more than 19 exchanges and runs market‑neutral two‑leg hedged trades to capture cross‑exchange spreads and funding rates. Users connect their own exchange accounts via API keys; the platform never holds funds, providing trade‑only access. Plans include live scanners, a dedicated execution server, and clear per‑plan limits.
image: https://arbitron.app/og-image-v4.png
json_schemas:
- name: ApiEnvelopeOfFundingHistoryResponse
  property_count: 2
  slug: arbitron-app-api-envelope-of-funding-history-response
- name: ApiEnvelopeOfIReadOnlyListOfAccountExchange
  property_count: 2
  slug: arbitron-app-api-envelope-of-iread-only-list-of-account-exchange
- name: ApiEnvelopeOfIReadOnlyListOfCurrentSpreadItem
  property_count: 2
  slug: arbitron-app-api-envelope-of-iread-only-list-of-current-spread-item
- name: ApiEnvelopeOfIReadOnlyListOfFundingRateItem
  property_count: 2
  slug: arbitron-app-api-envelope-of-iread-only-list-of-funding-rate-item
- name: ApiEnvelopeOfSpreadBacktestResponse
  property_count: 2
  slug: arbitron-app-api-envelope-of-spread-backtest-response
- name: DiscoveryResponse
  property_count: 11
  slug: arbitron-app-discovery-response
jsonld:
- class_count: 67
  name: Arbitron App Context
  property_count: 247
  slug: arbitron-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at arbitron.app.
  name: Arbitron MCP Server
  slug: arbitron-app-mcp-yml
modified: '2026-11-01'
name: Arbitron
nav: Providers
network: true
overview: 'Arbitron publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Funding API, Platform API, and 2 more. Tagged areas include Cryptocurrency, Arbitrage, Finance, and Platform.


  The Arbitron catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Arbitron''s developer surface includes authentication, API reference, pricing, support, and 26 more developer resources.'
plans:
- name: Arbitron App Plans Pricing
  plan_count: 3
  slug: arbitron-app-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Arbitron App Rate Limits
  slug: arbitron-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: Arbitron API Rules
  rule_count: 63
  severity_counts:
    error: 57
    hint: 0
    info: 1
    warn: 5
  slug: arbitron-app-rules
scopes:
- name: Arbitron App Scopes
  scope_count: 0
  slug: arbitron-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 57.9
    contract_governance: 22.0
    contract_quality: 68.6
    developer_ergonomics: 29.0
    discoverability: 56.7
    operational_transparency: 26.3
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arbitron App Authentication
  slug: arbitron-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Arbitron App Domain Security
  slug: arbitron-app-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Arbitron App Vulnerability Disclosure
  slug: arbitron-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-funding-rates
  slug: arbitron-app-get-funding-rates
slug: arbitron-app
tags:
- Cryptocurrency
- Arbitrage
- Finance
- Platform
website: https://arbitron.app/
---
