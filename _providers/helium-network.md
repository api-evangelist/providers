---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: REST + WebSocket / MQTT integration surface exposed by Helium-compatible LoRaWAN Network Servers (e.g. Nova Labs Console) for provisioning IoT devices, managing organizations and labels, configuring i
  name: Helium Console / LoRaWAN Network Server API
  slug: console-lns
- description: Open-source Solana on-chain programs and TypeScript client SDKs powering the Helium DAO, sub-DAOs, HNT / IOT / MOBILE token emissions, hotspot onboarding (HEM), and rewards distribution. Used by integ
  name: Helium Program Library (Solana)
  slug: helium-program-library
- description: Reference Rust command-line wallet for managing Helium accounts, tokens, and hotspot operations on Solana. Used by hotspot operators and integrators.
  name: Helium Wallet CLI (Rust)
  slug: helium-wallet-rs
- description: Canonical protocol buffer definitions for Helium message formats used across packet routing, oracles, and rewards. Required when implementing Helium-compatible services or tooling.
  name: Helium Protobuf Definitions
  slug: proto
- description: Source repository for docs.helium.com, covering the Mobile and IoT networks, tokens, wallets, and network-data resources. Useful as the authoritative pointer to per-vendor Network Server APIs and inte
  name: Helium Documentation Repository
  slug: docs-repo
artifact_total: 9
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/helium/helium-program-library/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/helium/helium-program-library/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/helium/helium-program-library/blob/master/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/helium/helium-program-library/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/helium-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.helium.com/
- group: company
  title: ''
  type: Website
  url: https://www.hellohelium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.helium.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/helium
- group: other
  title: ''
  type: Foundation
  url: https://www.helium.foundation/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/helium-systems-inc-
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.helium.com/llms.txt
created: '2026-05-23'
description: Helium operates two decentralized wireless networks - a global LoRaWAN network for low-power IoT devices and a cellular + Wi-Fi offload network for mobile connectivity (Helium Mobile). The network is settled on the Solana blockchain with HNT, IOT, and MOBILE tokens. Developer surface includes the Helium Console / LoRaWAN Network Server APIs used to onboard devices and stream uplinks, on-chain Solana programs for the Helium DAO and rewards, the open-source Helium-Program-Library and helium-wallet SDKs, and partner-operated Network Servers (e.g. Nova Labs, MeteoScientific).
finops:
- name: Helium Network Finops
  service_category: API
  slug: helium-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/helium-network.png
layout: provider
modified: '2026-05-23'
name: Helium Network
nav: Providers
network: true
overview: 'Helium Network publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Wireless, IoT, LoRaWAN, 5G, and DePIN.


  Helium Network''s developer surface includes documentation, GitHub presence, and 10 more developer resources.'
plans:
- name: Helium Network Plans Pricing
  plan_count: 1
  slug: helium-network-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 2
  name: Helium Network Rate Limits
  slug: helium-network-rate-limits
score:
  band: thin
  composite: 26.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 52.6
  open_source:
    applies: true
    score: 60.0
  previous_composite: 26.4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/helium-network/refs/heads/main/screenshots/helium-network-2026-06-20T182625.png
security:
- kind: domain-security
  name: Helium Network Domain Security
  slug: helium-network-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: helium-network
tags:
- Wireless
- IoT
- LoRaWAN
- 5G
- DePIN
- Solana
- Crypto
website: https://www.helium.com/
---
