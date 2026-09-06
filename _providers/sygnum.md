---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-09-05'
api_count: 10
apis:
- description: Real-time account and balance retrieval across fiat, digital assets and traditional securities held at Sygnum, with role-based permissions, exposed to B2B partners as REST.
  name: Sygnum Banking API
  slug: sygnum-banking-api
- description: Order management and execution for Sygnum's digital asset trading service, offered over both REST and the FIX protocol, with a webhook channel for asynchronous trade events.
  name: Sygnum Trading API
  slug: sygnum-trading-api
- description: Endpoint set designed for bank clients to fetch account balances held in Sygnum's institutional-grade digital asset custody environment.
  name: Sygnum Custody API
  slug: sygnum-custody-api
- description: Regulated Ethereum staking for retail and institutional clients — real-time staking, automated rewards, flexible amounts and portfolio tracking — with a webhook channel for staking lifecycle events.
  name: Sygnum Staking API
  slug: sygnum-staking-api
- description: Wallet service API covering wallet resources attached to Sygnum staking and digital asset accounts.
  name: Sygnum Wallet API
  slug: sygnum-wallet-api
- description: Digital asset transfer service API for moving assets in and out of Sygnum, with a webhook channel for transfer status events.
  name: Sygnum Digital Transfer API
  slug: sygnum-digital-transfer-api
- description: API for Sygnum Protect, the bank's off-exchange custody solution that lets exchanges verify client collateral held at Sygnum without moving it onto the venue.
  name: Sygnum Protect API
  slug: sygnum-protect-api
- description: API for Sygnum Connect, the bank's 24/7 instant multi-asset settlement network for crypto assets, stablecoins and fiat between member institutions.
  name: Sygnum Connect API
  slug: sygnum-connect-api
- description: Market data service exposed as REST plus a streaming WebSocket channel, so partners can stream prices and monitor markets inside their own systems.
  name: Sygnum Market Data API
  slug: sygnum-market-data-api
- description: Client-management surface of the developer portal — create and manage Auth0 clients, attach credentials (public key or certificate with a key identifier and expiry) and scope their access to Sygnum AP
  name: Sygnum Access Management API
  slug: sygnum-access-management-api
artifact_total: 17
asyncapis:
- description: ''
  name: Sygnum Webhooks
  slug: sygnum-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.sygnum.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sygnum.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sygnum.com/catalog
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sygnum.com/catalog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.sygnum.com/how-to-connect
- group: start
  title: ''
  type: SignUp
  url: https://start.join.sygnum.com/
- group: start
  title: ''
  type: Login
  url: https://developer.sygnum.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.sygnum.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.sygnum.com/future-finance/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sygnumbank
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sygnum.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sygnum.com/terms-of-use/
- group: other
  title: ''
  type: Imprint
  url: https://www.sygnum.com/imprint/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sygnum.com/help/accounts/custody-fees-at-sygnum/
- group: commercial
  title: ''
  type: Plans
  url: plans/sygnum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sygnum-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sygnum-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sygnum-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sygnum-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/sygnum-auth-openid-configuration.json
- group: design
  title: ''
  type: Conformance
  url: conformance/sygnum-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/sygnum-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sygnum-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sygnum-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sygnum-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sygnum-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sygnum-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sygnum-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/sygnum-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sygnum-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sygnum-security.txt
- group: auth
  title: ''
  type: Security
  url: security/sygnum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sygnum-vulnerability-disclosure.yml
coverage:
  checked: '2026-08-29'
  detail: Sygnum's developer portal ships a "Download specification" control for each of its ten B2B APIs, but the specifications are served from https://api.sygnum.com/b2b/v1/assets/content/dev-portal-assets-map, which returns HTTP 401 to anyone who is not a logged-in Sygnum client — the portal's own copy says registration requires an existing client relationship.
  evidence:
  - status: 401
    url: https://api.sygnum.com/b2b/v1/assets/content/dev-portal-assets-map
  - status: 401
    url: https://api.sygnum.com/b2b/v1/available-scopes
  - status: 200
    url: https://developer.sygnum.com/
  reason: customer-only-docs
  state: gated
created: '2026-08-29'
description: Sygnum is a regulated digital asset banking group, headquartered in Zurich with a Singapore arm, that received a Swiss FINMA banking and securities dealer licence in August 2019. It provides institutional custody, spot and derivatives trading, staking, tokenisation, Lombard lending and 24/7 instant settlement for banks, asset managers, exchanges and corporates. Its B2B business is delivered through an API layer published at developer.sygnum.com — a catalogue covering Banking, Trading (REST and FIX), Custody, Staking, Wallet, Digital Transfer, Sygnum Protect (off-exchange custody), Sygnum Connect (instant settlement) and Market Data (REST and WebSocket) — served from the api.sygnum.com/b2b gateway and secured with OAuth 2.0 client credentials issued from the bank's Auth0 tenant at auth.sygnum.com. The specifications themselves are downloadable only to authenticated Sygnum clients from the developer portal.
image: https://avatars.githubusercontent.com/sygnumbank
layout: provider
modified: '2026-08-29'
name: Sygnum
nav: Providers
network: true
overview: 'Sygnum publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Digital Assets, Cryptocurrency, and Custody.


  The Sygnum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sygnum''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 26 more developer resources.'
plans:
- name: Sygnum Plans Pricing
  plan_count: 0
  slug: sygnum-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Sygnum Rate Limits
  slug: sygnum-rate-limits
scopes:
- name: Sygnum Scopes
  scope_count: 0
  slug: sygnum-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
    - southeast-asia
  previous_composite: 53.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 74.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sygnum/refs/heads/main/screenshots/sygnum-2026-09-02T161443.png
security:
- kind: authentication
  name: Sygnum Authentication
  slug: sygnum-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sygnum Domain Security
  slug: sygnum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sygnum Vulnerability Disclosure
  slug: sygnum-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: sygnum
tags:
- Company
- Banking
- Digital Assets
- Cryptocurrency
- Custody
- Trading
- Staking
- Tokenization
- Settlement
- Market Data
- Financial-Services
- Switzerland
- Singapore
- B2B
website: https://www.sygnum.com/
---
