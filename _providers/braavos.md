---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/braavos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://braavos.app/
- group: company
  title: ''
  type: Blog
  url: https://braavos.app/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://braavos.app/faq/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/9Ks7V5DN9z
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/myBraavos
- group: build
  title: ''
  type: Packages
  url: packages/braavos-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/braavos-packages.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/braavos-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://braavos.app/braavos-wallet-bug-bounty-program/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/braavos-llms.txt
created: '2026-07-17'
description: 'Braavos is a self-custody smart-contract wallet for Bitcoin and Starknet, available as a browser extension and mobile app. Built on Starknet account abstraction, it adds hardware-backed two-factor signing (mobile secure element and passkeys), session keys for dApps, gas abstraction, in-wallet swaps, staking, and fiat on-ramp. Its developer surface is the injected Starknet wallet API (get-starknet), the Braavos Cairo account contracts, and first-party JavaScript libraries (session keys, deeplinks, StarkNet URLs, dApp metadata) published under the myBraavos GitHub organization. Braavos does not publish a hosted REST API or OpenAPI. Sector: crypto. Backed by Pantera Capital.'
image: https://braavos.app/wp-content/uploads/2023/01/braavos-logo.png
layout: provider
modified: '2026-07-18'
name: Braavos
nav: Providers
network: true
overview: 'Braavos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Wallets, Blockchain, and Starknet.


  Braavos'' developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/braavos/refs/heads/main/screenshots/braavos-2026-07-25T203656.png
security:
- kind: domain-security
  name: Braavos Domain Security
  slug: braavos-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Braavos Vulnerability Disclosure
  slug: braavos-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: braavos
tags:
- Company
- Crypto
- Wallets
- Blockchain
- Starknet
- Bitcoin
- Self-Custody
- Account Abstraction
- Web3
website: https://braavos.app/
---
