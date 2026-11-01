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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: GraphQL subgraphs providing endpoints for querying Toucan infrastructure and ecosystem data (projects, TCO2s, pools, retirements) on Base, Base Sepolia, Polygon, Amoy, Celo, and Celo Alfajores, served
  name: Toucan Subgraph API
  slug: toucan-subgraph-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/toucan/security/toucan-domain-security.yml
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
  href: https://artifacts.apis.io/toucan/packages/toucan-packages.yml
  title: ''
  type: Packages
  url: packages/toucan-packages.yml
- group: build
  href: https://artifacts.apis.io/toucan/packages/toucan-packages.yml
  title: ''
  type: SDKs
  url: packages/toucan-packages.yml
- group: agent
  href: https://artifacts.apis.io/toucan/llms/toucan-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toucan-llms.txt
- group: design
  href: https://artifacts.apis.io/toucan/errors/toucan-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/toucan-error-codes.yml
- group: start
  href: https://artifacts.apis.io/toucan/sandbox/toucan-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/toucan-sandbox.yml
- group: design
  href: https://artifacts.apis.io/toucan/lifecycle/toucan-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/toucan-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.toucan.earth/resources/archives/verra-bridge-deprecated
- group: auth
  href: https://artifacts.apis.io/toucan/authentication/toucan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toucan-authentication.yml
- group: design
  href: https://artifacts.apis.io/toucan/conformance/toucan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toucan-conformance.yml
- group: operate
  href: https://artifacts.apis.io/toucan/changelog/toucan-changelog.yml
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
overview: 'Toucan is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Planetary Health, Carbon Credits, Climate, and Web3.


  Toucan''s developer surface includes engineering blog, documentation, API reference, getting-started guide, support, sandbox, authentication, and 15 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 66.1
    operational_transparency: 28.9
  previous_composite: 33.1
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 19.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/toucan/toucan-2026-09-02T163945.png
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
