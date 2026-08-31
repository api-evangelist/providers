---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
  score: 21.9
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The Binance.US REST API is the primary programmatic interface to the exchange. It exposes general system and exchange information, market and trade data (recent/aggregate/historical trades, order book
  name: Binance.US REST API
  slug: rest-api
- description: The Binance.US WebSocket API is a request/response API delivered over a persistent WebSocket connection at wss://ws-api.binance.us/ws-api/v3. It is functionally equivalent to the REST API — the same p
  name: Binance.US WebSocket API
  slug: websocket-api
- description: Binance.US WebSocket Streams deliver real-time market data and account events over persistent WebSocket connections at wss://stream.binance.us:9443. Market data streams include aggregate trade, raw tr
  name: Binance.US WebSocket Streams
  slug: websocket-streams
artifact_total: 10
asyncapis:
- description: The Binance.US WebSocket API is a request/response API delivered over a persistent WebSocket connection. It is functionally equivalent to the REST API — same features, same parameters, same status and
  name: Binance.US WebSocket API
  slug: binance.us-websocket-api-asyncapi
- description: Binance.US WebSocket Streams deliver real-time market data and account events over persistent WebSocket connections. Streams can be consumed as a single raw stream at /ws/<streamName> or as a combined
  name: Binance.US WebSocket Streams
  slug: binance.us-websocket-streams-asyncapi
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/binance.us-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/binance.us-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/binance.us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.binance.us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.binance.us/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.binance.us/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.binance.us/#rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.binance.us/#introduction
- group: operate
  title: ''
  type: Support
  url: https://support.binance.us/en
- group: company
  title: ''
  type: Blog
  url: https://blog.binance.us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/binance-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.binance.us/fees
- group: start
  title: ''
  type: SignUp
  url: https://www.binance.us/register
- group: start
  title: ''
  type: Login
  url: https://www.binance.us/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.binance.us/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.binance.us/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.binance.us/status
- group: auth
  title: ''
  type: Compliance
  url: https://www.binance.us/compliance
- group: auth
  title: ''
  type: Security
  url: https://www.binance.us/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/binance.us-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/binance.us-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/binance.us-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/binance.us-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/binance.us-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/binance.us-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/binance.us-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/binance.us-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/binance.us-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/binance.us-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/binance.us-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/binance.us-websocket-streams-asyncapi.yml
created: '2026-08-07'
description: Binance.US (operated by BAM Trading Services, Inc.) is a U.S.-regulated digital asset marketplace offering spot trading, staking, OTC and custodial services across 100+ cryptocurrencies. Its public developer program exposes a signed REST API at api.binance.us covering exchange and system information, market and trade data, user account data, spot order management (including OCO and cancel-replace), wallet deposits and withdrawals, dust conversion, referrals, staking, OTC quoting, Custodial Solution and Credit Line endpoints, plus a functionally equivalent WebSocket API and real-time WebSocket market-data and user-data streams. Authentication is HMAC SHA-256 request signing with an X-MBX-APIKEY header, and the platform publishes a full error-code registry, symbol/exchange filter rules, weighted IP and order rate limits, and a dated changelog in its official GitHub documentation repository.
image: https://public.cstatic.us/static/images/binance_previewImage.png
layout: provider
modified: '2026-08-07'
name: Binance.US
nav: Providers
network: true
overview: 'Binance.US publishes 2 APIs on the [APIs.io](https://apis.io/) network: WebSocket API and WebSocket Streams. Tagged areas include Company, Cryptocurrency, Digital Assets, Exchange, and Trading.


  The Binance.US catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Binance.US''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 0
  name: Binance.Us Rate Limits
  slug: binance.us-rate-limits
score:
  band: developing
  composite: 52.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 45.2
    developer_ergonomics: 47.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 54.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/binance.us/refs/heads/main/screenshots/binance.us-2026-08-07T162440.png
security:
- kind: authentication
  name: Binance.Us Authentication
  slug: binance.us-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Binance.Us Domain Security
  slug: binance.us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Binance.Us Vulnerability Disclosure
  slug: binance.us-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Binance.Us Trust Center
  slug: binance.us-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: binance.us
tags:
- Company
- Cryptocurrency
- Digital Assets
- Exchange
- Trading
- Market Data
- Financial-Services
- WebSocket
- Custody
- Staking
website: https://www.binance.us
---
