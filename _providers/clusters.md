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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Clusters Agentic Access
  operation_count: 14
  slug: clusters-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 6
apis:
- description: Wallet-signature authentication for write operations
  name: Clusters Authentication API
  slug: clusters-authentication-api
- description: Read and create clusters (profiles bundling wallets)
  name: Clusters Clusters API
  slug: clusters-clusters-api
- description: Community cluster name availability and registration
  name: Clusters Communities API
  slug: clusters-communities-api
- description: Replayable historical event feed
  name: Clusters Events API
  slug: clusters-events-api
- description: Resolve addresses to cluster/wallet names and back
  name: Clusters Names API
  slug: clusters-names-api
- description: Check availability and build registration transaction data
  name: Clusters Registration API
  slug: clusters-registration-api
arazzos:
- description: Check whether a name is available, then build the EVM registration transaction data to sign.
  name: Check availability and build Clusters registration data
  slug: clusters-register-name
- description: Bulk-resolve a cluster name to its address, then read the full cluster profile.
  name: Resolve a Clusters name to a wallet and profile
  slug: clusters-resolve-name
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clusters Authentication API
  slug: open-clusters-authentication-api
- collection_type: open
  name: Authentication Clusters API
  slug: open-clusters-clusters-api
- collection_type: open
  name: Clusters Authentication Communities API
  slug: open-clusters-communities-api
- collection_type: open
  name: Clusters Authentication Events API
  slug: open-clusters-events-api
- collection_type: open
  name: Clusters Authentication Names API
  slug: open-clusters-names-api
- collection_type: open
  name: Clusters Authentication Registration API
  slug: open-clusters-registration-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clusters-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://clusters.xyz/vulnerability-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clusters-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clusters-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clusters-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://clusters.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://clusters.xyz/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clusters.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clusters.xyz/getting-started/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clusters.xyz/getting-started/javascript
- group: start
  title: ''
  type: SignUp
  url: https://clusters.xyz/developer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clustersxyz
- group: company
  title: ''
  type: Blog
  url: https://clusters.xyz/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clusters.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clusters.xyz/privacy
- group: build
  title: ''
  type: SDKs
  url: packages/clusters-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/clusters-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clusters-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clusters-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clusters-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/clusters-v1-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/clusters-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clusters-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clusters-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/clusters-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clusters-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clusters-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clusters-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/clusters-resolve-name.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/clusters-register-name.yml
created: '2026-07-17'
description: Clusters is a multichain namespace and identity service that gives users a single universal name across blockchain ecosystems instead of a separate domain per chain. A Clusters name uses the format username/wallet (for example username/eth or username/sol) to bundle many wallets — EVM chains, Solana, and more — under one hierarchical, human-readable profile. The Clusters v1 REST API resolves an address to its cluster and wallet name and back, reads full cluster profiles, checks name availability, produces on-chain registration transaction data for EVM and Solana, registers community cluster names, and exposes a replayable historical event feed for permissionless indexing. Reads are public; wallet management and registration require a wallet-signature bearer token, and an optional API key raises rate limits. The protocol uses a hub-and-spoke model bridged with LayerZero v2 and replicates metadata to Arweave for data availability. Backed by Electric Capital.
image: https://clusters.xyz/assets/images/apple/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Clusters MCP Server
  slug: clusters-mcp-server
modified: '2026-07-18'
name: Clusters
nav: Providers
network: true
overview: 'Clusters publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Clusters API, Communities API, and 3 more. Tagged areas include Company, Infrastructure, Identity, Naming, and Blockchain.


  Clusters'' developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, engineering blog, sandbox, and 24 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 55.9
    developer_ergonomics: 56.5
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clusters/refs/heads/main/screenshots/clusters-2026-07-25T205748.png
security:
- kind: authentication
  name: Clusters Authentication
  slug: clusters-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Clusters Domain Security
  slug: clusters-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Clusters Vulnerability Disclosure
  slug: clusters-vulnerability-disclosure
  summary_line: disclosure policy published
slug: clusters
tags:
- Company
- Infrastructure
- Identity
- Naming
- Blockchain
- Web3
- Wallets
- Multi-Chain
- Resolver
website: https://clusters.xyz/
---
