---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Bnb Chain API from InfStones — 1 operation(s) for bnb chain.
  name: InfStones Bnb Chain API
  slug: infstones-bnb-chain-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: bnb-chain Bnb Chain API
  slug: open-infstones-bnb-chain-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/infstones-bnb-chain-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://infstones.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.infstones.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infstones.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.infstones.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.infstones.com/reference/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://app.infstones.com
- group: operate
  title: ''
  type: Support
  url: https://infstones.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://infstones.com/blog/all
- group: commercial
  title: ''
  type: TermsOfService
  url: https://infstones.com/terms/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infstones.com/terms/privacy-notice
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infstones-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/infstones-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infstones-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infstones-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/infstones-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infstones-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infstones-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://infstones.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infstones-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://infstones.com/bug-bounty-program
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infstones-domain-security.yml
created: '2026-07-17'
description: InfStones is an enterprise-grade blockchain infrastructure platform providing node deployment and management, non-custodial staking, and reliable RPC/JSON-RPC API access across 50+ blockchains including Ethereum, BNB Chain, Cosmos, Solana, Cardano, Tezos, TRON, and ZetaChain. Developers connect to hosted full and archive nodes over standard EVM JSON-RPC, Tendermint, and Cosmos gRPC-REST endpoints authenticated by a per-project API key, deploy dedicated validator and staking nodes, and query on-chain data through a single unified developer console. The platform holds SOC 2 Type I and Type II attestation and serves major exchanges, protocols, and institutional clients globally. Backed by Qiming Venture Partners and SoftBank Vision Fund.
image: https://infstones.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: infstones-mcp.yml
  slug: infstones-mcpyml
modified: '2026-07-19'
name: InfStones
nav: Providers
network: true
overview: 'InfStones publishes 1 API on the [APIs.io](https://apis.io/) network: Bnb Chain API. Tagged areas include Company, Blockchain, Node Infrastructure, Staking, and Web3.


  InfStones'' developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 91
score:
  band: developing
  composite: 40.8
  delta: -6.5
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 30.3
    contract_quality: 55.9
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 47.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/infstones/refs/heads/main/screenshots/infstones-2026-07-25T222427.png
security:
- kind: authentication
  name: Infstones Authentication
  slug: infstones-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Infstones Domain Security
  slug: infstones-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Infstones Vulnerability Disclosure
  slug: infstones-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: infstones
tags:
- Company
- Blockchain
- Node Infrastructure
- Staking
- Web3
- JSON-RPC
- RPC
- Ethereum
- BNB Chain
- Cosmos
- Cryptocurrency
- API
website: https://infstones.com
---
