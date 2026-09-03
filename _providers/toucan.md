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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: GraphQL subgraphs providing endpoints for querying Toucan infrastructure and ecosystem data (projects, TCO2s, pools, retirements) on Base, Base Sepolia, Polygon, Amoy, Celo, and Celo Alfajores, served
  name: Toucan Subgraph API
  slug: toucan-subgraph-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toucan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://toucan.earth
- group: company
  title: ''
  type: Blog
  url: https://blog.toucan.earth
- group: docs
  title: ''
  type: Documentation
  url: https://docs.toucan.earth/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.toucan.earth/developers/toucan-developer-resources
- group: docs
  title: ''
  type: APIReference
  url: https://docs.toucan.earth/developers/subgraph
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.toucan.earth/developers/sdk/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.toucan.earth/developers/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ToucanProtocol
- group: commercial
  title: ''
  type: TermsOfService
  url: https://toucan.earth/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://toucan.earth/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.toucan.earth/
- group: build
  title: ''
  type: Packages
  url: packages/toucan-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/toucan-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/toucan-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/toucan-error-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/toucan-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/toucan-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.toucan.earth/resources/archives/verra-bridge-deprecated
- group: auth
  title: ''
  type: Authentication
  url: authentication/toucan-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/toucan-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/toucan-changelog.yml
created: '2026-07-17'
description: Toucan builds digital infrastructure for carbon credit markets, providing the rails for buying, selling, and retiring carbon credits on-chain. Its Carbon Bridge tokenizes credits from registries like Puro Earth into TCO2 tokens, carbon pools such as CHAR (biochar) bundle credits into liquid reference tokens, and retirement certificates prove offsets on-chain. Developers build on Toucan through audited smart contracts on Base, Celo, and Polygon, the toucan-sdk JavaScript/TypeScript SDK, and GraphQL subgraphs served through The Graph on six networks.
image: https://toucan.earth/wp-content/uploads/2024/05/transparent.png
layout: provider
modified: '2026-07-21'
name: Toucan
nav: Providers
network: true
overview: 'Toucan publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Planetary Health, Carbon Credits, Climate, and Web3.


  Toucan''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, sandbox, authentication, and 15 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 67.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 32.5
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toucan/refs/heads/main/screenshots/toucan-2026-09-02T163945.png
security:
- kind: authentication
  name: Toucan Authentication
  slug: toucan-authentication
  summary_line: apiKey/web3-wallet · 2 schemes
- kind: domain-security
  name: Toucan Domain Security
  slug: toucan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: toucan
tags:
- Company
- Planetary Health
- Carbon Credits
- Climate
- Web3
- Carbon Markets
- Tokenization
- GraphQL
- Biochar
website: https://toucan.earth
---
