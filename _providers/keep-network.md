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
  url: security/keep-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://keep.network
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/keep-network
- group: company
  title: ''
  type: Blog
  url: https://blog.keep.network
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/Threshold
- group: build
  title: ''
  type: Packages
  url: packages/keep-network-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/keep-network-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/keep-network-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/keep-network-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/keep-network-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/threshold-network/solidity-contracts/blob/main/SECURITY.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/keep-network-llms.txt
created: '2026-07-17'
description: Keep Network is a privacy-focused blockchain infrastructure project that merged with NuCypher in 2021 to form the Threshold Network. Its flagship product is tBTC, a decentralized, trust-minimized bridge that tokenizes Bitcoin as the TBTC ERC-20 token so it can be used across Ethereum DeFi without centralized custodians. Keep originally provided off-chain "keeps" — private data containers secured by a threshold ECDSA signing network and a random beacon — enabling confidential data to be used on public protocols. The developer surface is on-chain Solidity smart contracts plus first-party JavaScript/TypeScript client libraries published under the @keep-network npm scope; there is no hosted REST API. This profile was surfaced as a VC portfolio company and enriched from the project's public GitHub org, npm packages, blog, and security.txt.
image: https://github.com/keep-network.png
layout: provider
modified: '2026-07-19'
name: Keep Network
nav: Providers
network: true
overview: 'Keep Network is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Cryptocurrency, Bitcoin, and Ethereum.


  Keep Network''s developer surface includes engineering blog, support, and 10 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 6
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
  previous_composite: 10.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keep-network/refs/heads/main/screenshots/keep-network-2026-07-25T223548.png
security:
- kind: domain-security
  name: Keep Network Domain Security
  slug: keep-network-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Keep Network Vulnerability Disclosure
  slug: keep-network-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: keep-network
tags:
- Company
- Blockchain
- Cryptocurrency
- Bitcoin
- Ethereum
- DeFi
- Smart Contracts
- Web3
- Cryptography
- Decentralized Finance
website: https://keep.network
---
