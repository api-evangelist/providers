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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Latest API from Maverick Protocol — 1 operation(s) for latest.
  name: Maverick Protocol Latest API
  slug: maverick-protocol-latest-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Maverick V2 Data Latest API
  slug: open-maverick-protocol-latest-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/maverick-protocol-market-tickers.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/maverick-protocol-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maverick-protocol-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/maverick-protocol-well-known.yml
- group: auth
  title: ''
  type: Security
  url: security/maverick-protocol-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/maverick-protocol-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maverick-protocol-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mav.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mav.xyz/technical-reference/maverick-v2/v2-api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mav.xyz/getting-started/the-maverick-v2-ui
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maverickprotocol
- group: start
  title: ''
  type: SignUp
  url: https://app.mav.xyz/
- group: company
  title: ''
  type: Website
  url: https://www.mav.xyz/
created: '2026-07-17'
description: Maverick Protocol is a decentralized exchange (DEX) and automated market maker (AMM) for EVM chains, live on Ethereum, Base, zkSync Era and other networks through its dApp at app.mav.xyz. Its Dynamic Distribution AMM lets liquidity providers concentrate and automatically shift liquidity as prices move, and its veFlywheel and Boosted Positions direct MAV token incentives to pools. The core protocol is a set of on-chain V1 and V2 Solidity contracts (Factory, Pool, Router, Quoter, PoolLens, position and reward contracts) documented at docs.mav.xyz, complemented by a public hosted Data API (v2-api.mav.xyz) that returns 24-hour market pricing and volume tickers per chain. Surfaced in the API Evangelist network from the Pantera Capital portfolio.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maverick-protocol.png
layout: provider
mcp_servers:
- description: Candidate MCP tool surface mapped 1:1 from the documented Maverick V2 Data API. Not an official Maverick MCP server; a derivation for evaluation.
  name: Maverick V2 Data (candidate)
  slug: maverick-v2-data-candidate
modified: '2026-07-20'
name: Maverick Protocol
nav: Providers
network: true
overview: 'Maverick Protocol publishes 1 API on the [APIs.io](https://apis.io/) network: Latest API. Tagged areas include Company, Crypto, DeFi, DEX, and AMM.


  Maverick Protocol''s developer surface includes documentation, API reference, getting-started guide, signup flow, and 9 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 49.7
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 25.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maverick-protocol/refs/heads/main/screenshots/maverick-protocol-2026-08-07T172331.png
security:
- kind: domain-security
  name: Maverick Protocol Domain Security
  slug: maverick-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Maverick Protocol Vulnerability Disclosure
  slug: maverick-protocol-vulnerability-disclosure
  summary_line: Hackerone
slug: maverick-protocol
tags:
- Company
- Crypto
- DeFi
- DEX
- AMM
- Blockchain
- Market Data
- Liquidity
website: https://www.mav.xyz/
---
