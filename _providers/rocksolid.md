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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 25.6
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://app-integration.rocksolid.network/api
  baseurl_source: declared
  description: Strategy allocation snapshots and periods
  name: RockSolid Allocations API
  slug: rocksolid-allocations-api
- baseURL: https://app-integration.rocksolid.network/api
  baseurl_source: declared
  description: APR and TVL calculations
  name: RockSolid Performance API
  slug: rocksolid-performance-api
- baseURL: https://app-integration.rocksolid.network/api
  baseurl_source: declared
  description: Vault catalogue, metadata and performance
  name: RockSolid Vaults API
  slug: rocksolid-vaults-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RockSolid Vaults Allocations API
  slug: open-rocksolid-allocations-api
- collection_type: open
  name: RockSolid Vaults Allocations Performance API
  slug: open-rocksolid-performance-api
- collection_type: open
  name: RockSolid Allocations Vaults API
  slug: open-rocksolid-vaults-api
common:
- group: company
  title: ''
  type: Website
  url: https://rocksolid.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rocksolid.network
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rocksolid.network
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rocksolid.network/integration/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rocksolid.network/integration/onboarding-guide
- group: company
  title: ''
  type: Blog
  url: https://blog.rocksolid.network
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rocksolid-network
- group: operate
  title: ''
  type: Support
  url: https://rocksolid.network/contact#contact-form
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rocksolid.network/terms#tos
- group: start
  title: ''
  type: SignUp
  url: https://app.rocksolid.network
- group: auth
  title: ''
  type: Authentication
  url: authentication/rocksolid-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rocksolid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rocksolid-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rocksolid-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rocksolid-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rocksolid-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rocksolid-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rocksolid-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rocksolid-vaults-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rocksolid-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: RockSolid (rocksolid.network) is a DeFi platform offering actively managed, institutional-grade liquid vaults. It lets institutions, protocols and projects launch tailored, white-label vault products that give their communities streamlined access to higher yields and DeFi strategies typically reserved for large investors, sourcing yield from protocols such as Uniswap, Aave, Morpho and Yearn. Vaults are built on the ERC-7540 Asynchronous Tokenized Vault standard (Lagoon Finance implementation) and are audited. RockSolid publishes a public, read-only REST Vaults API that exposes vault metadata, curators, rewards, latest performance (NAV, APR/APY, TVL), strategy allocation snapshots by period, and calculated APR/TVL — plus smart-contract integration docs for on-chain deposit/redeem. Added to the API Evangelist network as a portfolio company of Kindred Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rocksolid.png
layout: provider
modified: '2026-07-21'
name: RockSolid
nav: Providers
network: true
overview: 'RockSolid publishes 3 APIs on the [APIs.io](https://apis.io/) network: Allocations API, Performance API, and Vaults API. Tagged areas include Company, DeFi, Decentralized Finance, Liquid Vaults, and Yield.


  RockSolid''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 53.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 38.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rocksolid/refs/heads/main/screenshots/rocksolid-2026-09-02T154045.png
security:
- kind: authentication
  name: Rocksolid Authentication
  slug: rocksolid-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rocksolid Domain Security
  slug: rocksolid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rocksolid
tags:
- Company
- DeFi
- Decentralized Finance
- Liquid Vaults
- Yield
- Staking
- Web3
- Blockchain
website: https://rocksolid.network/
---
