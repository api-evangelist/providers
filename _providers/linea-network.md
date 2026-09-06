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
  scored_at: '2026-09-05'
api_count: 10
apis:
- description: Public Ethereum-compatible JSON-RPC endpoint for Linea mainnet (chain ID 59144). Supports the standard eth_* method set plus Linea-specific extensions such as linea_estimateGas and linea_getProof.
  name: Linea Mainnet JSON-RPC
  slug: mainnet-rpc
- description: Public JSON-RPC endpoint for the Linea Sepolia testnet (chain ID 59141), used for application development, prover-changes testing, and bridge integration before deploying to mainnet.
  name: Linea Sepolia Testnet JSON-RPC
  slug: sepolia-rpc
- description: Linea custom JSON-RPC methods including linea_estimateGas (returns recommended gas limit, base fee, and priority fee accounting for L1 verification costs) and linea_getProof. Documented in the Linea A
  name: Linea-Specific JSON-RPC Methods
  slug: linea-rpc-methods
- description: Official TypeScript SDK for interacting with Linea — message-service helpers, bridge claim flows, and L1/L2 utility methods used by app developers and bridge integrators.
  name: Linea SDK
  slug: linea-sdk
- description: Canonical Ethereum-Linea bridge for ETH and supported ERC-20 tokens, built on Linea's message service. UI lives at bridge.linea.build.
  name: Linea Bridge
  slug: bridge
- description: Etherscan-style block explorer for Linea mainnet — transactions, blocks, contracts, tokens, batches, and Solidity source verification.
  name: Lineascan Block Explorer
  slug: lineascan-explorer
- description: Lineascan instance for the Linea Sepolia testnet, supporting transaction lookup and contract verification for testnet deployments.
  name: Lineascan Sepolia Testnet Explorer
  slug: lineascan-sepolia-explorer
- description: Linea Stack lets infra teams deploy and operate their own Ethereum-equivalent network using the Linea protocol — sequencer, prover, and message-service components.
  name: Linea Stack
  slug: linea-stack
- description: Linea POH (Proof of Humanity) attestation system used by ecosystem dApps for sybil-resistant identity, queried by contract or via attestation services.
  name: Linea Proof of Humanity
  slug: linea-poh
- description: Public directory of dApps, infrastructure providers, wallets, indexers, and services building on Linea — surfaces partner integrations developers can plug into.
  name: Linea Ecosystem Directory
  slug: ecosystem
artifact_total: 15
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/linea-network-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linea-network-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linea.build
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linea.build
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linea.build/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.linea.build/api
- group: other
  title: ''
  type: Bridge
  url: https://bridge.linea.build
- group: other
  title: ''
  type: Explorer
  url: https://lineascan.build
- group: other
  title: ''
  type: TestnetExplorer
  url: https://sepolia.lineascan.build
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Consensys/linea-monorepo
- group: docs
  title: ''
  type: DocsRepository
  url: https://github.com/Consensys/doc.linea
- group: operate
  title: ''
  type: Support
  url: https://support.linea.build
- group: operate
  title: ''
  type: Forums
  url: https://community.linea.build
- group: other
  title: ''
  type: Apps
  url: https://linea.build/apps
- group: company
  title: ''
  type: Blog
  url: https://linea.build/blog
- group: company
  title: ''
  type: Twitter
  url: https://x.com/LineaBuild
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/linea
- group: operate
  title: ''
  type: Status
  url: https://linea.statuspage.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linea.build/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linea.build/terms-of-service
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.linea.build/llms.txt
created: '2026-05-23'
description: Linea is an Ethereum zkEVM Layer 2 developed by Consensys, offering full Ethereum equivalence under a zero-knowledge proving system that finalizes state to Ethereum L1. Linea mainnet runs at chain ID 59144 with public JSON-RPC at rpc.linea.build, and a Sepolia testnet at chain ID 59141 at rpc.sepolia.linea.build. Developer surfaces include Linea-specific JSON-RPC extensions (linea_estimateGas, linea_getProof), the Linea SDK, the canonical Linea Bridge, Lineascan block explorer, the Linea POH/attestation system, and a published Linea Stack for deploying Linea-equivalent chains.
finops:
- name: Linea Network Finops
  service_category: API
  slug: linea-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linea-network.png
layout: provider
modified: '2026-05-23'
name: Linea
nav: Providers
network: true
overview: 'Linea publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Layer 2, Ethereum, zkEVM, and EVM Equivalence.


  Linea''s developer surface includes documentation, getting-started guide, API reference, GitHub presence, support, engineering blog, status page, and 14 more developer resources.'
plans:
- name: Linea Network Plans Pricing
  plan_count: 1
  slug: linea-network-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Linea Network Rate Limits
  slug: linea-network-rate-limits
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.0
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 24.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linea-network/refs/heads/main/screenshots/linea-network-2026-06-20T184538.png
security:
- kind: domain-security
  name: Linea Network Domain Security
  slug: linea-network-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Linea Network Vulnerability Disclosure
  slug: linea-network-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: linea-network
tags:
- Blockchain
- Layer 2
- Ethereum
- zkEVM
- EVM Equivalence
- JSON-RPC
- ConsenSys
website: https://linea.build
---
