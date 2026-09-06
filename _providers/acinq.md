---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
  score: 25.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The HTTP API of phoenixd, ACINQ's self-custodial Lightning server daemon. 27 documented endpoints covering Bolt11 invoices, Bolt12 offers, Lightning addresses, on-chain sends and swap-in, payment hist
  name: phoenixd HTTP API
  slug: phoenixd-http-api
- description: The JSON/HTTP API of eclair, ACINQ's Scala implementation of the Lightning Network. 56 documented methods grouped into node info, connections, channel open/close/splice/RBF, peers, network graph queri
  name: Eclair JSON API
  slug: eclair-json-api
artifact_total: 8
asyncapis:
- description: ''
  name: Acinq Phoenixd Webhooks
  slug: acinq-phoenixd-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/ACINQ/phoenixd/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acinq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acinq.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://phoenix.acinq.co/server
- group: docs
  title: ''
  type: Documentation
  url: https://acinq.github.io/eclair/
- group: docs
  title: ''
  type: APIReference
  url: https://phoenix.acinq.co/server/api
- group: start
  title: ''
  type: GettingStarted
  url: https://phoenix.acinq.co/server/get-started
- group: operate
  title: ''
  type: Support
  url: https://phoenix.acinq.co/support
- group: company
  title: ''
  type: Blog
  url: https://acinq.co/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ACINQ
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phoenix.acinq.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phoenix.acinq.co/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://phoenix.acinq.co/server/auto-liquidity
- group: auth
  title: ''
  type: Security
  url: https://github.com/ACINQ/eclair/blob/master/SECURITY.md
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/acinq-vulnerability-disclosure.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/acinq-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/acinq-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/acinq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/acinq-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/acinq-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/acinq-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/acinq-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/acinq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/acinq-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/acinq-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/acinq-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/acinq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/acinq-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/acinq-phoenixd-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acinq-llms.txt
created: '2026-08-17'
description: ACINQ is a Paris-based Bitcoin technology company and one of the principal implementers of the Lightning Network. It builds and maintains eclair, a Scala Lightning node with a 56-method JSON/HTTP API used for routing and channel management at scale; phoenixd, a self-custodial Lightning server daemon that exposes a 27-endpoint HTTP API plus websocket and HMAC-signed webhooks for merchants and applications; the Phoenix self-custodial mobile wallet; and the Kotlin Multiplatform libraries lightning-kmp, bitcoin-kmp and secp256k1-kmp published to Maven Central. ACINQ also operates its own mainnet and testnet Lightning nodes and acts as a liquidity service provider. Every API is self-hosted software rather than a vendor-hosted SaaS endpoint.
image: https://acinq.co/images/acinq-logo.svg
layout: provider
modified: '2026-08-17'
name: Acinq
nav: Providers
network: true
overview: 'Acinq publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Bitcoin, Lightning Network, and Payments.


  The Acinq catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Acinq''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 23 more developer resources.'
plans:
- name: Acinq Plans Pricing
  plan_count: 0
  slug: acinq-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Acinq Rate Limits
  slug: acinq-rate-limits
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 76.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 48.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/acinq/refs/heads/main/screenshots/acinq-2026-09-02T144115.png
security:
- kind: authentication
  name: Acinq Authentication
  slug: acinq-authentication
  summary_line: http · 5 schemes
- kind: domain-security
  name: Acinq Domain Security
  slug: acinq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Acinq Vulnerability Disclosure
  slug: acinq-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: acinq
tags:
- Company
- Blockchain
- Bitcoin
- Lightning Network
- Payments
- Open-Source
- Self-Custody
- Node Software
- Cryptocurrency
- Developer Tools
website: https://acinq.co/
---
