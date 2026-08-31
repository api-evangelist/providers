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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The ccip API from Enso — 2 operation(s) for ccip.
  name: Enso ccip API
  slug: enso-ccip-api
- description: The cctp API from Enso — 3 operation(s) for cctp.
  name: Enso cctp API
  slug: enso-cctp-api
- description: The layerzero API from Enso — 4 operation(s) for layerzero.
  name: Enso layerzero API
  slug: enso-layerzero-api
- description: The metadata API from Enso — 8 operation(s) for metadata.
  name: Enso metadata API
  slug: enso-metadata-api
- description: The projects API from Enso — 2 operation(s) for projects.
  name: Enso projects API
  slug: enso-projects-api
- description: The relay API from Enso — 1 operation(s) for relay.
  name: Enso relay API
  slug: enso-relay-api
- description: The shortcuts API from Enso — 5 operation(s) for shortcuts.
  name: Enso shortcuts API
  slug: enso-shortcuts-api
- description: The standards API from Enso — 4 operation(s) for standards.
  name: Enso standards API
  slug: enso-standards-api
- description: The wallet API from Enso — 2 operation(s) for wallet.
  name: Enso wallet API
  slug: enso-wallet-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Enso ccip API
  slug: open-enso-ccip-api
- collection_type: open
  name: Enso ccip cctp API
  slug: open-enso-cctp-api
- collection_type: open
  name: Enso ccip layerzero API
  slug: open-enso-layerzero-api
- collection_type: open
  name: Enso ccip metadata API
  slug: open-enso-metadata-api
- collection_type: open
  name: Enso ccip projects API
  slug: open-enso-projects-api
- collection_type: open
  name: Enso ccip relay API
  slug: open-enso-relay-api
- collection_type: open
  name: Enso ccip shortcuts API
  slug: open-enso-shortcuts-api
- collection_type: open
  name: Enso ccip standards API
  slug: open-enso-standards-api
- collection_type: open
  name: Enso ccip wallet API
  slug: open-enso-wallet-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/enso-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://enso.build
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.enso.build/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.enso.build/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.enso.build/pages/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.enso.build/pages/build/get-started/overview
- group: company
  title: ''
  type: Blog
  url: https://blog.enso.build/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EnsoBuild
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/enso-build
- group: start
  title: ''
  type: SignUp
  url: https://developers.enso.build/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.enso.build/pages/build/reference/legal
- group: operate
  title: ''
  type: StatusPage
  url: https://status.enso.finance
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/enso-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/enso-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/enso-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/enso-packages.yml
- group: design
  title: ''
  type: Components
  url: components/enso-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/enso-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enso-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/enso-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enso-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/enso-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/enso-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/enso-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enso-domain-security.yml
created: '2026-07-17'
description: Enso is onchain infrastructure that turns DeFi product intent into signer-ready transaction data. Its Route API finds the optimal path between any two tokens or positions across 250+ protocols and multiple chains, while the Bundle API composes ordered onchain Actions (deposit, swap, borrow, bridge, flashloan, transfer and more) into a single executable transaction. Enso also exposes protocol, token, price and balance data, a Quoter for a simulate-then-validate transaction-safety model, cross-chain routing over Stargate/LayerZero, Chainlink CCIP, Relay and Circle CCTP, and prebuilt React widgets (Checkout, cross-chain route). Developers authenticate with a Bearer API key and integrate via the @ensofinance/sdk TypeScript SDK. Backed by Multicoin Capital and Techstars; 100+ apps and 1,900+ developers build on Enso.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enso.png
layout: provider
mcp_servers:
- description: ''
  name: Enso MCP Server
  slug: enso-mcp-server
modified: '2026-07-19'
name: Enso
nav: Providers
network: true
overview: 'Enso publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ccip API, cctp API, layerzero API, and 6 more. Tagged areas include Company, Crypto Web3, DeFi, Blockchain, and Cross-chain.


  Enso''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, changelog, and 19 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Enso Rate Limits
  slug: enso-rate-limits
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 50.9
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 43.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enso/refs/heads/main/screenshots/enso-2026-07-25T213420.png
security:
- kind: authentication
  name: Enso Authentication
  slug: enso-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Enso Domain Security
  slug: enso-domain-security
  summary_line: TLSv1.2 · DMARC
slug: enso
tags:
- Company
- Crypto Web3
- DeFi
- Blockchain
- Cross-chain
- Smart Contracts
- Transaction Routing
- Web3 Infrastructure
- Onchain
website: https://enso.build
---
