---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.2
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Reown Agentic Access
  operation_count: 6
  slug: reown-agentic-access
  summary_line: 6 operations
api_count: 7
apis:
- description: REST API to retrieve listings of WalletGuide-approved wallets, dApps, hybrid entries, and chains, plus logo assets. Filter by chain, platform, SDK, standard, or search term.
  name: Reown Cloud Explorer API
  slug: explorer-api
- description: REST API for sending wallet push notifications via the Reown Notify protocol, plus subject/topic management.
  name: Reown Notify (Push) API
  slug: notify-api
- description: Multi-chain JSON-RPC over HTTPS used by AppKit and partners; provides on-chain reads, gas, swaps, and onramp helpers.
  name: Reown Blockchain API
  slug: blockchain-api
- description: WalletConnect v2 relay network for end-to-end encrypted JSON-RPC pairing between dApps and wallets. Accessed through SDK clients only; not a direct REST surface.
  name: WalletConnect Relay (SDK-mediated)
  slug: walletconnect-protocol
- description: Blockchain chains registered under CASA namespaces.
  name: Reown Chains API
  slug: reown-chains-api
- description: Wallet, dApp, and hybrid directory listings.
  name: Reown Listings API
  slug: reown-listings-api
- description: Logo image assets for listings.
  name: Reown Logos API
  slug: reown-logos-api
artifact_total: 21
asyncapis:
- description: 'AsyncAPI description of the Reown (formerly WalletConnect) v2 Relay WebSocket protocol. The relay is a JSON-RPC over WebSocket transport that routes end-to-end encrypted messages between paired peers '
  name: Reown / WalletConnect v2 Relay
  slug: reown-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reown Cloud Explorer Chains API
  slug: open-reown-chains-api
- collection_type: open
  name: Reown Cloud Explorer Chains Listings API
  slug: open-reown-listings-api
- collection_type: open
  name: Reown Cloud Explorer Chains Logos API
  slug: open-reown-logos-api
- collection_type: open
  name: Reown Cloud Explorer API
  slug: open-reown
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reown-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/reown-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reown-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reown-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reown-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/re-own
- group: company
  title: ''
  type: Website
  url: https://reown.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/reown-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reown-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reown-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.reown.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://reown.com/blog
created: '2026-05-08'
description: Reown (formerly WalletConnect) provides Web3 connection infrastructure including AppKit (login + wallet integration UX), WalletConnect SDK (wallet-side), the Reown Cloud Explorer API (dApp/wallet directory), Push Notifications, and Multi-chain RPC. The WalletConnect protocol itself is SDK-mediated; Reown also exposes REST APIs for the Cloud Explorer.
finops:
- name: Reown Finops
  service_category: Web3
  slug: reown-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reown.png
layout: provider
modified: '2026-05-08'
name: Reown
nav: Providers
network: true
overview: 'Reown publishes 4 APIs on the [APIs.io](https://apis.io/) network, including WalletConnect Relay (SDK-mediated), Chains API, Listings API, and 1 more. Tagged areas include Web3, Wallets, WalletConnect, AppKit, and RPC.


  The Reown catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Reown''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Reown Plans Pricing
  plan_count: 3
  slug: reown-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Reown Rate Limits
  slug: reown-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Reown API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: reown-asyncapi-spectral-rules
score:
  band: thin
  composite: 33.0
  delta: 1.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 60.8
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 11.4
    operational_transparency: 7.9
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reown/refs/heads/main/screenshots/reown-2026-06-20T192900.png
security:
- kind: authentication
  name: Reown Authentication
  slug: reown-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Reown Domain Security
  slug: reown-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Reown Vulnerability Disclosure
  slug: reown-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: reown
tags:
- Web3
- Wallets
- WalletConnect
- AppKit
- RPC
website: https://reown.com/
---
