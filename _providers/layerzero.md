---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Layerzero Agentic Access
  operation_count: 26
  slug: layerzero-agentic-access
  summary_line: 26 operations · 3 acting
api_count: 4
apis:
- baseURL: https://scan.layerzero-api.com/v1
  baseurl_source: declared
  description: The Discovery API from LayerZero — 3 operation(s) for discovery.
  name: LayerZero Discovery API
  slug: layerzero-discovery-api
- baseURL: https://scan.layerzero-api.com/v1
  baseurl_source: declared
  description: The messages API from LayerZero — 7 operation(s) for messages.
  name: LayerZero messages API
  slug: layerzero-messages-api
- baseURL: https://scan.layerzero-api.com/v1
  baseurl_source: declared
  description: The ofts API from LayerZero — 2 operation(s) for ofts.
  name: LayerZero ofts API
  slug: layerzero-ofts-api
- baseURL: https://scan.layerzero-api.com/v1
  baseurl_source: declared
  description: The openapi API from LayerZero — 1 operation(s) for openapi.
  name: LayerZero openapi API
  slug: layerzero-openapi-api
- baseURL: https://scan.layerzero-api.com/v1
  baseurl_source: declared
  description: The Transfer API from LayerZero — 4 operation(s) for transfer.
  name: LayerZero Transfer API
  slug: layerzero-transfer-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LayerZero OFT Transfer Discovery API
  slug: open-layerzero-discovery-api
- collection_type: open
  name: LayerZero OFT Transfer Discovery messages API
  slug: open-layerzero-messages-api
- collection_type: open
  name: LayerZero OFT Transfer Discovery ofts API
  slug: open-layerzero-ofts-api
- collection_type: open
  name: LayerZero OFT Transfer Discovery openapi API
  slug: open-layerzero-openapi-api
- collection_type: open
  name: LayerZero OFT Discovery Transfer API
  slug: open-layerzero-transfer-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/LayerZero-Labs/devtools/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/LayerZero-Labs/devtools/releases
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/layerzero-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/layerzero-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/layerzero-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://layerzero.network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.layerzero.network/v2
- group: build
  title: ''
  type: GitHub
  url: https://github.com/LayerZero-Labs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/LayerZero-Labs/devtools
- group: other
  title: ''
  type: Explorer
  url: https://layerzeroscan.com/
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/layerzero
- group: company
  title: ''
  type: Twitter
  url: https://x.com/LayerZero_Core
- group: company
  title: ''
  type: Blog
  url: https://layerzero.network/blog
- group: other
  title: ''
  type: Whitepaper
  url: https://layerzero.network/whitepaper
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.layerzero.network/v2/developers/changelog
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/layerzero/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/layerzero/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/layerzero/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: LayerZero is an omnichain interoperability protocol that enables seamless cross-chain messaging, token transfers, and OApp/OFT deployments across 90+ blockchains. It provides REST APIs for querying cross-chain message status, estimating fees, tracking OFT deployments, and executing value transfers across 150+ supported chains.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/layerzero.png
jsonld:
- class_count: 9
  name: context Context
  property_count: 6
  slug: context
layout: provider
modified: '2026-06-13'
name: LayerZero
nav: Providers
network: true
overview: 'LayerZero publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, messages API, ofts API, and 2 more. Tagged areas include Blockchain, Cross-Chain, Omnichain, Interoperability, and Web3.


  The LayerZero catalog on APIs.io includes 1 JSON-LD context.


  LayerZero''s developer surface includes authentication, documentation, GitHub presence, engineering blog, changelog, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 2
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 31.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 48.4
    developer_ergonomics: 28.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/layerzero/refs/heads/main/screenshots/layerzero-2026-06-20T184335.png
security:
- kind: authentication
  name: Layerzero Authentication
  slug: layerzero-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Layerzero Domain Security
  slug: layerzero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: layerzero
tags:
- Blockchain
- Cross-Chain
- Omnichain
- Interoperability
- Web3
- DeFi
- Messaging
- Token Transfers
website: https://layerzero.network/
---
