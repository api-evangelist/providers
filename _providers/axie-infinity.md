---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
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
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: 'Read-only REST API for Axie Infinity: Origins community game data — list and fetch cards, runes, charms and items; list a user''s fighters and fighter configurations; read burned items; list seasons an'
  name: Axie Infinity Origins API
  slug: axie-infinity-origins-api
- description: REST API for Axie Experience Points, the ecosystem-wide off-chain progression system for Axies. Partner games and dApps read AXP balances for up to 24 Axies at a time, read AXP by game, check AXP gain
  name: Axie Experience Points (AXP) API
  slug: axie-experience-points-axp-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/axie-infinity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://axieinfinity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.roninchain.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skymavis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skymavis.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skymavis.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://developers.roninchain.com/console/applications/
- group: operate
  title: ''
  type: Support
  url: https://support.axieinfinity.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.axieinfinity.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/axieinfinity
- group: other
  title: ''
  type: Whitepaper
  url: https://whitepaper.axieinfinity.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.skymavis.com/files/skymavis-terms-of-use-09012025.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.skymavis.com/files/skymavis-privacypolicy-10122024.pdf
- group: auth
  title: ''
  type: Authentication
  url: authentication/axie-infinity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/axie-infinity-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/axie-infinity-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/axie-infinity-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/axie-infinity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/axie-infinity-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/axie-infinity-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/axie-infinity-llms.txt
created: '2026-08-06'
description: 'Axie Infinity is a blockchain game franchise built by Sky Mavis on the Ronin network, where players collect, breed and battle creatures called Axies across titles including Axie Infinity: Origins, Homeland and Classic. Its developer-facing surface is published through the Sky Mavis developer platform: the Axie Infinity Origins API exposes read-only community game data — cards, runes, charms, items, user fighter configurations, burned items, seasons, season leaderboards and paginated battle logs — while the Axie Experience Points (AXP) API lets partner games and dApps read and issue AXP, the off-chain progression token that maps to on-chain Axie levels. Both are REST products behind the api-gateway.skymavis.com gateway, authenticated with an X-API-Key issued per application from the Ronin Developer Console, and both require a per-service access grant requested in the console. Sky Mavis publishes a rendered API reference for these products but no downloadable OpenAPI description.'
layout: provider
modified: '2026-08-06'
name: Axie Infinity
nav: Providers
network: true
overview: 'Axie Infinity publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Blockchain, Web3, and NFT.


  Axie Infinity''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 0
  name: Axie Infinity Rate Limits
  slug: axie-infinity-rate-limits
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 12
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 26.4
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/axie-infinity/refs/heads/main/screenshots/axie-infinity-2026-08-07T162037.png
security:
- kind: authentication
  name: Axie Infinity Authentication
  slug: axie-infinity-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Axie Infinity Domain Security
  slug: axie-infinity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: axie-infinity
tags:
- Company
- Gaming
- Blockchain
- Web3
- NFT
- Game Data
- Leaderboards
- Ronin
- Play-to-Earn
website: https://axieinfinity.com/
---
