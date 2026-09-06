---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The EDX Markets institutional trading interface, delivered over the FIX protocol: FIX 5.0 SP2 order entry and drop copy plus FIX and binary (SBE) market data over a FIXT.1.1 session inside a mutually '
  name: EDX Markets FIX API (Order Entry & Market Data)
  slug: edx-markets-fix-api-order-entry-market-data
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.edxmarkets.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://edxmarkets.com/vr-edx-markets/
- group: docs
  title: ''
  type: Documentation
  url: https://edxmarkets.com/vr-edx-markets/
- group: docs
  title: ''
  type: APIReference
  url: https://edxmarkets.com/wp-content/uploads/EDXM-FIX-Order-Entry-Specifications.pdf
- group: operate
  title: ''
  type: Support
  url: https://edxmarkets.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://edxmarkets.com/news-insights/
- group: start
  title: ''
  type: SignUp
  url: https://edxmarkets.com/join-edx-markets/
- group: commercial
  title: ''
  type: Pricing
  url: https://edxmarkets.com/wp-content/uploads/EDX-Markets-Fee-Schedule.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://edxmarkets.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://edxmarkets.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/edx-markets-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/edx-markets-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/edx-markets-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/edx-markets-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/edx-markets-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/edx-markets-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/edx-markets-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/edx-markets-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/edx-markets-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/edx-markets-llms.txt
created: '2026-07-17'
description: EDX Markets is an institutional cryptocurrency exchange that operates the world's only centrally cleared crypto trading venue, combining deep liquidity, transparent markets, low trading costs and ultra-low-latency matching-engine technology. It runs a spot exchange (EDX Markets), a perpetual-futures exchange (EDXM International, based in Singapore), a central clearinghouse with daily net settlement and bankruptcy-remote member accounts (EDXM Global), and a white-label crypto-as-a-service platform (EDX FlowConnect). Connectivity for members is delivered over the FIX protocol — FIX 5.0 SP2 order entry and drop copy plus FIX and binary (SBE) market data, transported over mutually authenticated TLS — rather than a public REST/OpenAPI. EDX is backed by institutional partners and was surfaced through the pantera-capital portfolio.
image: https://edxmarkets.com/wp-content/uploads/EDX_URLPrevew_2024-09-10.jpg
layout: provider
modified: '2026-07-19'
name: EDX Markets
nav: Providers
network: true
overview: 'EDX Markets publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Cryptocurrency, Digital Assets, and Exchange.


  EDX Markets'' developer surface includes documentation, API reference, support, engineering blog, signup flow, pricing, authentication, and 13 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Edx Markets Rate Limits
  slug: edx-markets-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 35.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/edx-markets/refs/heads/main/screenshots/edx-markets-2026-07-25T212920.png
security:
- kind: authentication
  name: Edx Markets Authentication
  slug: edx-markets-authentication
  summary_line: mutualTLS/fix-session-logon · 2 schemes
- kind: domain-security
  name: Edx Markets Domain Security
  slug: edx-markets-domain-security
  summary_line: TLSv1.3 · DMARC
slug: edx-markets
tags:
- Company
- Crypto
- Cryptocurrency
- Digital Assets
- Exchange
- Trading
- FIX Protocol
- Market Data
- Clearing
- Institutional
website: https://www.edxmarkets.com/
---
