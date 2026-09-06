---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Standard Ethereum JSON-RPC 2.0 interface to the Zircuit L2 network (HTTP and WebSocket) for reading chain state and submitting transactions. Mainnet is chain ID 48900; the Garfield testnet is chain ID
  name: Zircuit JSON-RPC API
  slug: zircuit-json-rpc-api
- baseURL: https://mainnet.zircuit.com
  baseurl_source: declared
  description: Trade estimates and cross-chain order execution data.
  name: Zircuit Orders API
  slug: zircuit-orders-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zircuit GUD Trading Engine API (Beta) Orders API
  slug: open-zircuit-orders-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zircuit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zircuit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.zircuit.com/build/start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zircuit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zircuit.com/infra/rpcs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.zircuit.com/build/start
- group: company
  title: ''
  type: Blog
  url: https://www.zircuit.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zircuit-labs
- group: start
  title: ''
  type: SignUp
  url: https://finance.zircuit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://static.zircuit.com/docs/tos.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://static.zircuit.com/docs/pp.pdf
- group: operate
  title: ''
  type: Support
  url: https://jobs.ashbyhq.com/Zircuit
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zircuit.com/
- group: other
  title: ''
  type: x-explorer
  url: https://explorer.zircuit.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zircuit-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/zircuit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zircuit-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zircuit-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zircuit-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zircuit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/zircuit-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zircuit-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zircuit-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/zircuit-mcp.yml
created: '2026-07-17'
description: Zircuit is a zero-knowledge (zk) rollup Layer 2 blockchain and secure onchain finance platform. The network is fully EVM-compatible and OP-Stack based, letting developers deploy standard Solidity smart contracts (via Foundry and the usual Ethereum tooling) while settling to Ethereum with zk validity proofs. Zircuit exposes standard Ethereum JSON-RPC endpoints for mainnet (chain ID 48900) and the Garfield testnet (chain ID 48898), a canonical L1<>L2 bridge, a relayer service (EIP-7702 gasless relaying), a transaction simulation surface, and the GUD Trading Engine — a REST API that aggregates cross-chain liquidity to return best-execution quotes and signable transaction data. On top of the chain, Zircuit Finance and the Liquidity Hub offer institutional-grade yield and LST/LRT staking. Backed by Pantera Capital; the network and contracts have been audited by six independent security firms and run a bug-bounty program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zircuit.png
layout: provider
modified: '2026-07-21'
name: Zircuit
nav: Providers
network: true
overview: 'Zircuit publishes 1 API on the [APIs.io](https://apis.io/) network: Orders API. Tagged areas include Company, Crypto, Blockchain, Layer 2, and Rollup.


  Zircuit''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 17 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 52.4
    developer_ergonomics: 60.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 44.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zircuit/refs/heads/main/screenshots/zircuit-2026-08-17T083112.png
security:
- kind: authentication
  name: Zircuit Authentication
  slug: zircuit-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Zircuit Domain Security
  slug: zircuit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zircuit Vulnerability Disclosure
  slug: zircuit-vulnerability-disclosure
  summary_line: contact published
slug: zircuit
tags:
- Company
- Crypto
- Blockchain
- Layer 2
- Rollup
- Zero Knowledge
- EVM
- DeFi
- JSON-RPC
- Web3
website: https://www.zircuit.com/
---
