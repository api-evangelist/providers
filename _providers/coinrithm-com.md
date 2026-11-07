---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 2
  name: Coinrithm Com Agentic Access
  operation_count: 86
  slug: coinrithm-com-agentic-access
  summary_line: 86 operations · 13 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: Paper isolated-futures positions — open, close, and set SL/TP.
  name: CoinRithm Futures API
  slug: coinrithm-com-futures-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: API-key identity, granted scopes, and paper-account status.
  name: CoinRithm Identity API
  slug: coinrithm-com-identity-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: Agent action ledger and the reproducible run-evidence export.
  name: CoinRithm Ledger API
  slug: coinrithm-com-ledger-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: Paper prediction-market discovery, quotes, and positions.
  name: CoinRithm Prediction Markets API
  slug: coinrithm-com-prediction-markets-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: 'Keyless crypto universe reads used for candidate discovery. Same Acceptable Use terms as the other keyless surfaces: https://www.coinrithm.com/en/terms-of-use'
  name: CoinRithm Public Crypto Data API
  slug: coinrithm-com-public-crypto-data-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: 'Keyless market data beyond the coin universe: TradFi reference prices, large perpetual trades, liquidations, CFTC positioning, SEC Form 4 insider filings and public-company crypto treasuries. Same Acc'
  name: CoinRithm Public Market Data API
  slug: coinrithm-com-public-market-data-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: 'Keyless cross-venue prediction-market research data across 12 venues. Subject to CoinRithm''s Acceptable Use terms — no model training, redistribution, or competing use: https://www.coinrithm.com/en/te'
  name: CoinRithm Public Pm Data API
  slug: coinrithm-com-public-pm-data-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: Market, coin, and prediction-market reads and quotes (no writes).
  name: CoinRithm Reads API
  slug: coinrithm-com-reads-api
- baseURL: https://api.coinrithm.com
  baseurl_source: declared
  description: Paper spot orders — place, cancel, and list open orders.
  name: CoinRithm Spot API
  slug: coinrithm-com-spot-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/coinrithm-com/agentic-access/coinrithm-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coinrithm-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/coinrithm-com/rules/coinrithm-com-rules.yml
  title: ''
  type: Spectral
  url: rules/coinrithm-com-rules.yml
- group: design
  href: https://artifacts.apis.io/coinrithm-com/json-ld/coinrithm-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coinrithm-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/coinrithm-com/vocabulary/coinrithm-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinrithm-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coinrithm-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coinrithm-com/data-model/coinrithm-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coinrithm-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/coinrithm-com/conventions/coinrithm-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/coinrithm-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/coinrithm-com/conventions/coinrithm-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/coinrithm-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/coinrithm-com/security/coinrithm-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/coinrithm-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/coinrithm-com/errors/coinrithm-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/coinrithm-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/coinrithm-com/conformance/coinrithm-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinrithm-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinrithm-com/llms/coinrithm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinrithm-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/coinrithm-com/mcp/coinrithm-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coinrithm-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/coinrithm-com/well-known/coinrithm-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinrithm-com-security.txt
- group: auth
  href: https://artifacts.apis.io/coinrithm-com/well-known/coinrithm-com-coinrithm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coinrithm-com-coinrithm-security.txt
- group: agent
  href: https://artifacts.apis.io/coinrithm-com/well-known/coinrithm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coinrithm-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coinrithm-com/hosts/coinrithm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinrithm-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinrithm-com/vendors/coinrithm-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinrithm-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/coinrithm-com/packages/coinrithm-com-packages.yml
  title: ''
  type: SDKs
  url: packages/coinrithm-com-packages.yml
- group: build
  href: https://artifacts.apis.io/coinrithm-com/packages/coinrithm-com-packages.yml
  title: ''
  type: Packages
  url: packages/coinrithm-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinrithm.com/en/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinrithm.com/en/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.coinrithm.com/en/news
- group: other
  title: ''
  type: Leadership
  url: https://www.coinrithm.com/en/tradfi/team
- group: company
  title: ''
  type: Blog
  url: https://www.coinrithm.com/en/blog
- group: auth
  href: https://artifacts.apis.io/coinrithm-com/authentication/coinrithm-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coinrithm-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/coinrithm-com/security/coinrithm-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coinrithm-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coinrithm-com/security/coinrithm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinrithm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coinrithm.com/
created: '2026-11-04'
description: CoinRithm, operated by Bees‑x Limited, provides an information and research service that offers prediction markets, live cryptocurrency prices, and paper‑trading tools. The platform is designed for people and AI agents to practice trading with virtual funds and to follow real‑world events without using real money.
image: https://www.coinrithm.com/banner.png
json_schemas:
- name: AgentDecisionArtifact
  property_count: 31
  slug: coinrithm-com-agent-decision-artifact
- name: ArenaContract
  property_count: 6
  slug: coinrithm-com-arena-contract
- name: ArenaDecision
  property_count: 30
  slug: coinrithm-com-arena-decision
- name: PmPosition
  property_count: 30
  slug: coinrithm-com-pm-position
- name: PublicCoinPrice
  property_count: 32
  slug: coinrithm-com-public-coin-price
- name: PublicPmCalibrationResponse
  property_count: 8
  slug: coinrithm-com-public-pm-calibration-response
jsonld:
- class_count: 120
  name: Coinrithm Com Context
  property_count: 599
  slug: coinrithm-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.coinrithm.com.
  name: CoinRithm MCP Server
  slug: coinrithm-com-mcp-yml
modified: '2026-11-04'
name: CoinRithm
nav: Providers
network: true
overview: 'CoinRithm publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Futures API, Identity API, Ledger API, and 6 more. Tagged areas include Prediction Markets, Crypto Prices, Paper Trading, Agentic Trading, and Research Service.


  The CoinRithm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CoinRithm''s developer surface includes engineering blog, authentication, and 27 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: CoinRithm API Rules
  rule_count: 65
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 10
  slug: coinrithm-com-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 27.9
    discoverability: 68.3
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coinrithm Com Authentication
  slug: coinrithm-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Coinrithm Com Domain Security
  slug: coinrithm-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coinrithm Com Vulnerability Disclosure
  slug: coinrithm-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: portfolio
  slug: coinrithm-com-portfolio
slug: coinrithm-com
tags:
- Prediction Markets
- Crypto Prices
- Paper Trading
- Agentic Trading
- Research Service
- Live Market Data
website: https://www.coinrithm.com/
---
