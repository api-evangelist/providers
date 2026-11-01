---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 46
  human_in_the_loop: 1
  name: Madeonsol Agentic Access
  operation_count: 233
  slug: madeonsol-agentic-access
  summary_line: 233 operations · 46 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The primary keyed MadeOnSol REST API (Bearer msk_ API keys, free and paid tiers), version 1.20.0 with 198 operations across Solana and Robinhood Chain (78 Robinhood Chain operations under /rhc/*) - KO
  name: MadeOnSol API
  slug: madeonsol-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Self-service account inspection — quota, tier, feature usage. 1 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Account API
  slug: madeonsol-account-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Profitable non-KOL alpha wallets — leaderboard + per-wallet drilldown. 5 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Alpha API
  slug: madeonsol-alpha-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Rule-based copy-trade subscriptions (PRO+). 6 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Copy Trade API
  slug: madeonsol-copy-trade-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Pump.fun deployer reputation alerts, leaderboard, and per-deployer drilldowns. 13 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Deployer Hunter API
  slug: madeonsol-deployer-hunter-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Bulk Parquet exports of every fully archived closed month (token_trades, rhc_trades, token_ohlc_1m, rhc_ohlc_1m) via presigned S3 links. BUSINESS+. 1 operation(s) of the keyed MadeOnSol API (Bearer ms
  name: MadeOnSol Exports API
  slug: madeonsol-exports-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: KOL wallet trade feed, leaderboard, coordination, hot tokens, and per-KOL profile. 29 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol KOL API
  slug: madeonsol-kol-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Nightly dataset manifests — per-dataset fingerprint and schema hash to cite an exact data state. Any key. 1 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Meta API
  slug: madeonsol-meta-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Token MC dip/recovery alerts, evaluated every 250 ms. PRO+ (PRO 5 / ULTRA 25 / BUSINESS 125 rules). 6 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Price Alerts API
  slug: madeonsol-price-alerts-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Robinhood Chain (chain id 4663) coverage — same intel, EVM-native contracts (0x addresses, eth_amount, tx_hash). Bundled into existing tiers at no extra cost. 78 operation(s) of the keyed MadeOnSol AP
  name: MadeOnSol Robinhood Chain API
  slug: madeonsol-robinhood-chain-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Pre-confirmation pump.fun deploy detection — recent deploys, by-deployer feed, custom watchlist. PRO+ (curated to elite/good deployers); ULTRA gets every tier + watchlist + by-deployer. 5 operation(s)
  name: MadeOnSol Sniper API
  slug: madeonsol-sniper-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Public service health + data-quality status (no auth). 1 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Status API
  slug: madeonsol-status-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: WebSocket stream tokens and live session management — 30 channels (16 Solana + 14 Robinhood Chain) on one socket, with seq/id on event frames and resume (memory, then up to 60 minutes of backfill from
  name: MadeOnSol Streaming API
  slug: madeonsol-streaming-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Token-level buyer-quality, cap-table, and filtered token directory. 26 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Tokens API
  slug: madeonsol-tokens-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Public Solana & Robinhood Chain tools directory search. 1 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Tools API
  slug: madeonsol-tools-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: 'Universal per-wallet endpoints: aggregate stats with cross-product flags, FIFO cost-basis PnL with daily curve, open positions with live unrealized, and cursor-paginated raw trades. PRO+. 10 operation'
  name: MadeOnSol Wallet API
  slug: madeonsol-wallet-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: Track any Solana wallet — aggregate stats and recent trades. 6 operation(s) of the keyed MadeOnSol API (Bearer msk_ key).
  name: MadeOnSol Wallet Tracker API
  slug: madeonsol-wallet-tracker-api
- baseURL: https://madeonsol.com/api/v1
  baseurl_source: declared
  description: 'HMAC-signed webhook registrations for KOL, deployer, wallet-tracker, sniper, token momentum, RHC KOL and realtime developer activity (dev:activity, live since 2026-10-05) events. PRO+. 6 operation(s) '
  name: MadeOnSol Webhooks API
  slug: madeonsol-webhooks-api
- baseURL: https://madeonsol.com/api/x402/rhc
  baseurl_source: declared
  description: 'Keyless x402 pay-per-call subset of MadeOnSol for Robinhood Chain: 10 operations priced per call in USDG on Robinhood Chain (EIP-3009), no API key. A separate, smaller surface than the keyed MadeOnSol'
  name: MadeOnSol x402 Robinhood Chain API
  slug: madeonsol-x402-robinhood-chain-api
- baseURL: https://madeonsol.com/api/x402
  baseurl_source: declared
  description: 'Keyless x402 pay-per-call subset of MadeOnSol for Solana: 25 operations priced per call in USDC on Solana, no API key. A separate, smaller surface than the keyed MadeOnSol API.'
  name: MadeOnSol x402 Solana API
  slug: madeonsol-x402-solana-api
artifact_total: 30
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://madeonsol.com/feed.xml
- group: agent
  href: https://artifacts.apis.io/madeonsol/agentic-access/madeonsol-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/madeonsol-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/madeonsol/plans/madeonsol-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/madeonsol-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/madeonsol/rules/madeonsol-rules.yml
  title: ''
  type: Spectral
  url: rules/madeonsol-rules.yml
- group: build
  href: https://artifacts.apis.io/madeonsol/cli/madeonsol-cli.yml
  title: ''
  type: CLI
  url: cli/madeonsol-cli.yml
- group: operate
  href: https://artifacts.apis.io/madeonsol/changelog/madeonsol-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/madeonsol-changelog.yml
- group: design
  href: https://artifacts.apis.io/madeonsol/conventions/madeonsol-conventions.yml
  title: ''
  type: Conventions
  url: conventions/madeonsol-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://madeonsol.com/security
- group: auth
  href: https://artifacts.apis.io/madeonsol/authentication/madeonsol-authentication.yml
  title: ''
  type: Authentication
  url: authentication/madeonsol-authentication.yml
- group: design
  href: https://artifacts.apis.io/madeonsol/errors/madeonsol-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/madeonsol-problem-types.yml
- group: design
  href: https://artifacts.apis.io/madeonsol/conformance/madeonsol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/madeonsol-conformance.yml
- group: agent
  href: https://artifacts.apis.io/madeonsol/llms/madeonsol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/madeonsol-llms.txt
- group: auth
  href: https://artifacts.apis.io/madeonsol/well-known/madeonsol-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/madeonsol-security.txt
- group: agent
  href: https://artifacts.apis.io/madeonsol/well-known/madeonsol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/madeonsol-well-known.yml
- group: other
  href: https://artifacts.apis.io/madeonsol/hosts/madeonsol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/madeonsol-hosts.yml
- group: other
  href: https://artifacts.apis.io/madeonsol/vendors/madeonsol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/madeonsol-vendors.yml
- group: build
  href: https://artifacts.apis.io/madeonsol/packages/madeonsol-packages.yml
  title: ''
  type: Packages
  url: packages/madeonsol-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://madeonsol.com/status
- group: auth
  title: ''
  type: Security
  url: https://madeonsol.com/security
- group: build
  title: ''
  type: SDKs
  url: https://madeonsol.com/best/sdks
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/madeonsol
- group: start
  title: ''
  type: DeveloperPortal
  url: https://madeonsol.com/developer
- group: operate
  title: ''
  type: ChangeLog
  url: https://madeonsol.com/changelog
- group: auth
  href: https://artifacts.apis.io/madeonsol/security/madeonsol-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/madeonsol-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/madeonsol/security/madeonsol-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/madeonsol-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/madeonsol/security/madeonsol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/madeonsol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://madeonsol.com
- group: other
  title: ''
  type: APIsJSON
  url: https://madeonsol.com/.well-known/apis.json
- group: other
  title: ''
  type: APICatalog
  url: https://madeonsol.com/.well-known/api-catalog
- group: docs
  title: ''
  type: AsyncAPI
  url: https://madeonsol.com/api/v1/asyncapi.json
- group: agent
  title: ''
  type: AgentSkills
  url: https://madeonsol.com/skills/index.json
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://madeonsol.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://madeonsol.com/api/agent-gateway/mcp
- group: agent
  title: ''
  type: MCPPackages
  url: https://madeonsol.com/mcp-packages.json
- group: other
  title: ''
  type: AgentsJSON
  url: https://madeonsol.com/agents.json
- group: other
  title: ''
  type: X402
  url: https://madeonsol.com/.well-known/x402
- group: agent
  title: ''
  type: LLMsFullTxt
  url: https://madeonsol.com/llms-full.txt
- group: docs
  title: ''
  type: Documentation
  url: https://madeonsol.com/api-docs
- group: operate
  title: ''
  type: Support
  url: https://madeonsol.com/about
- group: company
  title: ''
  type: Blog
  url: https://madeonsol.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://madeonsol.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://madeonsol.com/auth/login?next=%2F
- group: commercial
  title: ''
  type: TermsOfService
  url: https://madeonsol.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://madeonsol.com/privacy
created: '2026-09-28'
description: MadeOnSol provides on-chain intelligence APIs for Solana and Robinhood Chain, offering real-time KOL wallet tracking, deployer reputation scoring, and all-DEX trade streams. It also hosts a directory of tools and a developer API with SDKs and a pay-per-call x402 model.
finops:
- has_sources: true
  method: derived
  name: Madeonsol Finops
  primary_unit: ''
  service_category: ''
  slug: madeonsol-finops
  template: true
image: https://madeonsol.com/opengraph-image?v=3
layout: provider
mcp_servers:
- description: ''
  name: MadeOnSol MCP Server
  slug: mcp
modified: '2026-10-06'
name: MadeOnSol
nav: Providers
network: true
overview: 'MadeOnSol publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Alpha API, and 18 more. Tagged areas include Blockchain, Analytics, Solana, and Robinhood Chain.


  The MadeOnSol catalog on APIs.io includes 1 Spectral governance ruleset.


  MadeOnSol''s developer surface includes CLI, changelog, authentication, documentation, support, engineering blog, pricing, and 37 more developer resources.'
plans:
- name: Madeonsol Plans Pricing
  plan_count: 5
  slug: madeonsol-plans-pricing
- name: Madeonsol Price Estimates
  plan_count: 0
  slug: madeonsol-price-estimates
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: MadeOnSol API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: madeonsol-rules
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 47.8
    catalog_earned_first_party: 12.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 92.1
    contract_governance: 15.9
    contract_quality: 48.2
    developer_ergonomics: 70.7
    discoverability: 66.7
    operational_transparency: 47.4
  previous_composite: 63.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 11.1
      total: 18
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/madeonsol/madeonsol-2026-10-11T110633.png
security:
- kind: authentication
  name: Madeonsol Authentication
  slug: madeonsol-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Madeonsol Domain Security
  slug: madeonsol-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Madeonsol Vulnerability Disclosure
  slug: madeonsol-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Madeonsol Trust Center
  slug: madeonsol-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: madeonsol
tags:
- Blockchain
- Analytics
- Solana
- Robinhood Chain
website: https://madeonsol.com
---
