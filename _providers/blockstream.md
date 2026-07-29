---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The Addresses API from Blockstream — 11 operation(s) for addresses.
  name: Blockstream Addresses API
  slug: blockstream-addresses-api
- description: The Assets API from Blockstream — 7 operation(s) for assets.
  name: Blockstream Assets API
  slug: blockstream-assets-api
- description: The Blocks API from Blockstream — 11 operation(s) for blocks.
  name: Blockstream Blocks API
  slug: blockstream-blocks-api
- description: The Fee Estimates API from Blockstream — 1 operation(s) for fee estimates.
  name: Blockstream Fee Estimates API
  slug: blockstream-fee-estimates-api
- description: The Mempool API from Blockstream — 3 operation(s) for mempool.
  name: Blockstream Mempool API
  slug: blockstream-mempool-api
- description: The Mining API from Blockstream — 1 operation(s) for mining.
  name: Blockstream Mining API
  slug: blockstream-mining-api
- description: The Transactions API from Blockstream — 10 operation(s) for transactions.
  name: Blockstream Transactions API
  slug: blockstream-transactions-api
artifact_total: 10
common:
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Blockstream/esplora/blob/master/API.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blockstream
- group: company
  title: ''
  type: Blog
  url: https://blockstream.com/blog/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/blockstream-esplora-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/blockstream-esplora-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blockstream-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blockstream-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blockstream-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blockstream-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blockstream-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blockstream-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/blockstream-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blockstream-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blockstream-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blockstream-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blockstream-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/blockstream-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blockstream-domain-security.yml
created: '2026-07-17'
description: 'Blockstream is a Bitcoin infrastructure company whose products include the Liquid Network sidechain, the Green self-custody wallet, Blockstream Satellite, and Bitcoin mining and data services. For developers its flagship public API is Esplora, the open-source Bitcoin block explorer behind blockstream.info: a no-authentication HTTP REST API for reading blocks, transactions, addresses, scripthashes, the mempool, and fee estimates across Bitcoin mainnet, testnet, and signet, plus Liquid/Elements issued assets. Amounts are returned in satoshis and hashes are hex-encoded, with cursor pagination over confirmed transaction history. Blockstream also ships GDK, its open-source cross-platform wallet SDK.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blockstream.png
layout: provider
mcp_servers:
- description: ''
  name: blockstream-mcp.yml
  slug: blockstream-mcpyml
modified: '2026-07-18'
name: Blockstream
nav: Providers
network: true
overview: 'Blockstream publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Assets API, Blocks API, and 4 more. Tagged areas include Company, Bitcoin, Blockchain, Cryptocurrency, and Block Explorer.


  Blockstream''s developer surface includes documentation, engineering blog, authentication, sandbox, and 15 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 31.1
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 48.2
    developer_ergonomics: 38.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 32.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/screenshots/blockstream-2026-07-25T203345.png
security:
- kind: authentication
  name: Blockstream Authentication
  slug: blockstream-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Blockstream Domain Security
  slug: blockstream-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: blockstream
tags:
- Company
- Bitcoin
- Blockchain
- Cryptocurrency
- Block Explorer
- Financial Services
- Infrastructure
---
