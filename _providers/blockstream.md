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
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-09-17'
api_count: 7
apis:
- baseURL: https://blockstream.info/api
  baseurl_source: declared
  description: The Addresses API from Blockstream — 11 operation(s) for addresses.
  name: Blockstream Addresses API
  slug: blockstream-addresses-api
- baseURL: https://blockstream.info/api
  baseurl_source: declared
  description: The Assets API from Blockstream — 7 operation(s) for assets.
  name: Blockstream Assets API
  slug: blockstream-assets-api
- baseURL: https://blockstream.info/api
  baseurl_source: declared
  description: The Blocks API from Blockstream — 11 operation(s) for blocks.
  name: Blockstream Blocks API
  slug: blockstream-blocks-api
- baseURL: https://blockstream.info/api
  baseurl_source: declared
  description: The Fee Estimates API from Blockstream — 1 operation(s) for fee estimates.
  name: Blockstream Fee Estimates API
  slug: blockstream-fee-estimates-api
- baseURL: https://blockstream.info/api
  baseurl_source: declared
  description: The Mempool API from Blockstream — 3 operation(s) for mempool.
  name: Blockstream Mempool API
  slug: blockstream-mempool-api
- baseURL: https://blockstream.info/api
  baseurl_source: declared
  description: The Mining API from Blockstream — 1 operation(s) for mining.
  name: Blockstream Mining API
  slug: blockstream-mining-api
- baseURL: https://blockstream.info/api
  baseurl_source: declared
  description: The Transactions API from Blockstream — 10 operation(s) for transactions.
  name: Blockstream Transactions API
  slug: blockstream-transactions-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blockstream Esplora HTTP Addresses API
  slug: open-blockstream-addresses-api
- collection_type: open
  name: Blockstream Esplora HTTP Addresses Assets API
  slug: open-blockstream-assets-api
- collection_type: open
  name: Blockstream Esplora HTTP Addresses Blocks API
  slug: open-blockstream-blocks-api
- collection_type: open
  name: Blockstream Esplora HTTP Addresses Fee Estimates API
  slug: open-blockstream-fee-estimates-api
- collection_type: open
  name: Blockstream Esplora HTTP Addresses Mempool API
  slug: open-blockstream-mempool-api
- collection_type: open
  name: Blockstream Esplora HTTP Addresses Mining API
  slug: open-blockstream-mining-api
- collection_type: open
  name: Blockstream Esplora HTTP Addresses Transactions API
  slug: open-blockstream-transactions-api
common:
- group: company
  title: ''
  type: Website
  url: https://blockstream.info
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
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/openapi/_original/blockstream-esplora-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/blockstream-esplora-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/overlays/blockstream-esplora-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/blockstream-esplora-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/authentication/blockstream-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blockstream-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/conventions/blockstream-conventions.yml
  title: ''
  type: Conventions
  url: conventions/blockstream-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/errors/blockstream-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/blockstream-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/data-model/blockstream-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blockstream-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/lifecycle/blockstream-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/blockstream-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/conformance/blockstream-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockstream-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/packages/blockstream-packages.yml
  title: ''
  type: Packages
  url: packages/blockstream-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/packages/blockstream-packages.yml
  title: ''
  type: SDKs
  url: packages/blockstream-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/mcp/blockstream-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/blockstream-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/llms/blockstream-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockstream-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/well-known/blockstream-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockstream-well-known.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/sandbox/blockstream-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/blockstream-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/blockstream/refs/heads/main/security/blockstream-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockstream-domain-security.yml
created: '2026-07-17'
description: 'Blockstream is a Bitcoin infrastructure company whose products include the Liquid Network sidechain, the Green self-custody wallet, Blockstream Satellite, and Bitcoin mining and data services. For developers its flagship public API is Esplora, the open-source Bitcoin block explorer behind blockstream.info: a no-authentication HTTP REST API for reading blocks, transactions, addresses, scripthashes, the mempool, and fee estimates across Bitcoin mainnet, testnet, and signet, plus Liquid/Elements issued assets. Amounts are returned in satoshis and hashes are hex-encoded, with cursor pagination over confirmed transaction history. Blockstream also ships GDK, its open-source cross-platform wallet SDK.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blockstream.png
layout: provider
modified: '2026-09-16'
name: Blockstream
nav: Providers
network: true
overview: 'Blockstream publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Assets API, Blocks API, and 4 more. Tagged areas include Company, Bitcoin, Blockchain, Cryptocurrency, and Block Explorer.


  Blockstream''s developer surface includes documentation, engineering blog, authentication, sandbox, and 16 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 11.5
    developer_ergonomics: 47.0
    discoverability: 81.5
    operational_transparency: 2.6
  previous_composite: 20.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Financial-Services
- Infrastructure
website: https://blockstream.info
---
