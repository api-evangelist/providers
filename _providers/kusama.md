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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-19'
api_count: 21
apis:
- description: 'The public Substrate JSON-RPC 2.0 interface to the Kusama relay chain. Probed live on 2026-07-19: 130 methods are advertised by rpc_methods, spanning chain (blocks/headers), state (storage, metadata, '
  name: Kusama JSON-RPC API
  slug: json-rpc
- description: The accounts API from Kusama — 11 operation(s) for accounts.
  name: Kusama accounts API
  slug: kusama-accounts-api
- description: Asset Hub Migration information
  name: Kusama ahm API
  slug: kusama-ahm-api
- description: The blocks API from Kusama — 8 operation(s) for blocks.
  name: Kusama blocks API
  slug: kusama-blocks-api
- description: The contracts API from Kusama — 1 operation(s) for contracts.
  name: Kusama contracts API
  slug: kusama-contracts-api
- description: The coretime API from Kusama — 6 operation(s) for coretime.
  name: Kusama coretime API
  slug: kusama-coretime-api
- description: node connected to sidecar
  name: Kusama node API
  slug: kusama-node-api
- description: pallets employed in the runtime
  name: Kusama pallets API
  slug: kusama-pallets-api
- description: The paras API from Kusama — 9 operation(s) for paras.
  name: Kusama paras API
  slug: kusama-paras-api
- description: The rc accounts API from Kusama — 5 operation(s) for rc accounts.
  name: Kusama rc accounts API
  slug: kusama-rc-accounts-api
- description: relay chain specific endpoints for asset hub
  name: Kusama rc API
  slug: kusama-rc-api
- description: The rc blocks API from Kusama — 8 operation(s) for rc blocks.
  name: Kusama rc blocks API
  slug: kusama-rc-blocks-api
- description: The rc node API from Kusama — 3 operation(s) for rc node.
  name: Kusama rc node API
  slug: kusama-rc-node-api
- description: The rc pallets API from Kusama — 13 operation(s) for rc pallets.
  name: Kusama rc pallets API
  slug: kusama-rc-pallets-api
- description: The rc runtime API from Kusama — 5 operation(s) for rc runtime.
  name: Kusama rc runtime API
  slug: kusama-rc-runtime-api
- description: The rc staking API from Kusama — 4 operation(s) for rc staking.
  name: Kusama rc staking API
  slug: kusama-rc-staking-api
- description: The rc transaction API from Kusama — 5 operation(s) for rc transaction.
  name: Kusama rc transaction API
  slug: kusama-rc-transaction-api
- description: The runtime API from Kusama — 5 operation(s) for runtime.
  name: Kusama runtime API
  slug: kusama-runtime-api
- description: The staking API from Kusama — 4 operation(s) for staking.
  name: Kusama staking API
  slug: kusama-staking-api
- description: The trace API from Kusama — 4 operation(s) for trace.
  name: Kusama trace API
  slug: kusama-trace-api
- description: The transaction API from Kusama — 6 operation(s) for transaction.
  name: Kusama transaction API
  slug: kusama-transaction-api
artifact_total: 49
asyncapis:
- description: The event/streaming surface of the Kusama relay chain, served over WebSocket at wss://kusama-rpc.polkadot.io. Kusama publishes no webhooks — there is no vendor to register a callback URL with. Push de
  name: Kusama JSON-RPC Subscription API
  slug: kusama-jsonrpc-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Substrate API Sidecar accounts API
  slug: open-kusama-accounts-api
- collection_type: open
  name: Substrate API Sidecar accounts ahm API
  slug: open-kusama-ahm-api
- collection_type: open
  name: Substrate API Sidecar accounts blocks API
  slug: open-kusama-blocks-api
- collection_type: open
  name: Substrate API Sidecar accounts contracts API
  slug: open-kusama-contracts-api
- collection_type: open
  name: Substrate API Sidecar accounts coretime API
  slug: open-kusama-coretime-api
- collection_type: open
  name: Substrate API Sidecar accounts node API
  slug: open-kusama-node-api
- collection_type: open
  name: Substrate API Sidecar accounts pallets API
  slug: open-kusama-pallets-api
- collection_type: open
  name: Substrate API Sidecar accounts paras API
  slug: open-kusama-paras-api
- collection_type: open
  name: Substrate API Sidecar accounts rc accounts API
  slug: open-kusama-rc-accounts-api
- collection_type: open
  name: Substrate API Sidecar accounts rc API
  slug: open-kusama-rc-api
- collection_type: open
  name: Substrate API Sidecar accounts rc blocks API
  slug: open-kusama-rc-blocks-api
- collection_type: open
  name: Substrate API Sidecar accounts rc node API
  slug: open-kusama-rc-node-api
- collection_type: open
  name: Substrate API Sidecar accounts rc pallets API
  slug: open-kusama-rc-pallets-api
- collection_type: open
  name: Substrate API Sidecar accounts rc runtime API
  slug: open-kusama-rc-runtime-api
- collection_type: open
  name: Substrate API Sidecar accounts rc staking API
  slug: open-kusama-rc-staking-api
- collection_type: open
  name: Substrate API Sidecar accounts rc transaction API
  slug: open-kusama-rc-transaction-api
- collection_type: open
  name: Substrate API Sidecar accounts runtime API
  slug: open-kusama-runtime-api
- collection_type: open
  name: Substrate API Sidecar accounts staking API
  slug: open-kusama-staking-api
- collection_type: open
  name: Substrate API Sidecar accounts trace API
  slug: open-kusama-trace-api
- collection_type: open
  name: Substrate API Sidecar accounts transaction API
  slug: open-kusama-transaction-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/kusama-sidecar-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://kusama.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.polkadot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.polkadot.com/chain-interactions/
- group: docs
  title: ''
  type: APIReference
  url: https://paritytech.github.io/json-rpc-interface-spec/
- group: start
  title: ''
  type: GettingStarted
  url: https://wiki.polkadot.com/kusama/kusama-getting-started/
- group: operate
  title: ''
  type: Support
  url: https://docs.polkadot.com/get-support/
- group: operate
  title: ''
  type: Community
  url: https://forum.polkadot.network/tag/kusama
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/paritytech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kusama.network/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kusama.network/privacy
- group: build
  title: ''
  type: Packages
  url: packages/kusama-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kusama-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/kusama-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kusama-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kusama-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kusama-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kusama-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kusama-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kusama-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kusama-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kusama-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/kusama-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/kusama-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kusama-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kusama-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kusama-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/kusama-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kusama-jsonrpc-asyncapi.yml
created: '2026-07-17'
description: 'Kusama is the permissionless, unaudited canary network of the Polkadot ecosystem, running the same Polkadot SDK (Substrate/FRAME) runtime as Polkadot but with faster governance, lower barriers to entry, and real economic conditions — it is where runtime upgrades, parachain/coretime mechanics, and governance changes ship first before reaching Polkadot. Its developer surface is a chain interface rather than a hosted SaaS API: a public Substrate JSON-RPC 2.0 endpoint at kusama-rpc.polkadot.io exposing 130 live methods (chain, state, author, system, payment, plus the newer chainHead/archive/transaction v1 families) over HTTP and WebSocket, and a REST projection of the same chain state via Substrate API Sidecar at kusama-public-sidecar.parity-chains.parity.io, documented by a 119-operation OpenAPI 3.0 specification. Access is unauthenticated and public-read; write access happens by submitting SCALE-encoded, key-signed extrinsics. The native token is KSM (12 decimals, SS58 prefix
  2).'
examples:
- key_count: 6
  name: Kusama Jsonrpc Examples
  slug: kusama-jsonrpc-examples
- key_count: 3
  name: Kusama Rpc Methods
  slug: kusama-rpc-methods
image: https://kusama.network/images/kusama-logo-canary-white.png
layout: provider
mcp_servers:
- description: ''
  name: kusama-mcp.yml
  slug: kusama-mcpyml
modified: '2026-07-19'
name: Kusama
nav: Providers
network: true
overview: 'Kusama publishes 21 APIs on the [APIs.io](https://apis.io/) network, including JSON-RPC API, accounts API, ahm API, and 18 more. Tagged areas include Company, Crypto, Blockchain, Web3, and Polkadot.


  The Kusama catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kusama''s developer surface includes documentation, API reference, getting-started guide, support, CLI, authentication, changelog, and 23 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 50.0
  delta: 0.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 56.8
    developer_ergonomics: 78.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 49.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kusama/refs/heads/main/screenshots/kusama-2026-07-25T224336.png
security:
- kind: authentication
  name: Kusama Authentication
  slug: kusama-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kusama Domain Security
  slug: kusama-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kusama Vulnerability Disclosure
  slug: kusama-vulnerability-disclosure
  summary_line: disclosure policy published
slug: kusama
tags:
- Company
- Crypto
- Blockchain
- Web3
- Polkadot
- Substrate
- JSON-RPC
- Blockchain Data
- Staking
- Governance
website: https://kusama.network/
---
