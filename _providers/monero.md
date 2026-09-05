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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Monero Agentic Access
  operation_count: 17
  slug: monero-agentic-access
  summary_line: 17 operations · 17 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: Blockchain data and block operations
  name: Monero Blockchain API
  slug: monero-blockchain-api
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: JSON-RPC 2.0 dispatch endpoint
  name: Monero JSON-RPC API
  slug: monero-json-rpc-api
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: Mining control and block template operations
  name: Monero Mining API
  slug: monero-mining-api
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: Peer and network management
  name: Monero Network API
  slug: monero-network-api
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: Node status and info
  name: Monero Node Info API
  slug: monero-node-info-api
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: Output and key image operations
  name: Monero Outputs API
  slug: monero-outputs-api
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: Mempool / transaction pool operations
  name: Monero Transaction Pool API
  slug: monero-transaction-pool-api
- baseURL: http://localhost:18081
  baseurl_source: declared
  description: Transaction submission and lookup
  name: Monero Transactions API
  slug: monero-transactions-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Monero Daemon RPC Blockchain API
  slug: open-monero-blockchain-api
- collection_type: open
  name: Monero Daemon RPC Blockchain JSON-RPC API
  slug: open-monero-json-rpc-api
- collection_type: open
  name: Monero Daemon RPC Blockchain Mining API
  slug: open-monero-mining-api
- collection_type: open
  name: Monero Daemon RPC Blockchain Network API
  slug: open-monero-network-api
- collection_type: open
  name: Monero Daemon RPC Blockchain Node Info API
  slug: open-monero-node-info-api
- collection_type: open
  name: Monero Daemon RPC Blockchain Outputs API
  slug: open-monero-outputs-api
- collection_type: open
  name: Monero Daemon RPC Blockchain Transaction Pool API
  slug: open-monero-transaction-pool-api
- collection_type: open
  name: Monero Daemon RPC Blockchain Transactions API
  slug: open-monero-transactions-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/monero-project/monero/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/monero-project/monero/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/monero-project/monero/blob/master/docs/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/monero-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getmonero.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getmonero.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.getmonero.org/resources/developer-guides/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/monero-project
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/monero-project/monero
- group: build
  title: ''
  type: GitHubEcosystem
  url: https://github.com/monero-ecosystem
- group: operate
  title: ''
  type: StackOverflow
  url: https://monero.stackexchange.com
- group: operate
  title: ''
  type: Forums
  url: https://forum.getmonero.org/
- group: other
  title: ''
  type: IRC
  url: https://matrix.to/#/#monero:libera.chat
- group: company
  title: ''
  type: Blog
  url: https://www.getmonero.org/blog/
- group: other
  title: ''
  type: ResearchLab
  url: https://www.getmonero.org/resources/research-lab/
- group: other
  title: ''
  type: Downloads
  url: https://www.getmonero.org/downloads/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/json-schema/monero-types.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/json-ld/monero-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/finops/finops.yml
created: '2026-06-14'
description: Monero is a privacy-focused, decentralized cryptocurrency providing JSON-RPC APIs for wallet management, transaction creation, mining coordination, and blockchain data access on the Monero (XMR) network. The daemon RPC exposes node and chain operations while the wallet RPC provides comprehensive wallet and transfer management.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monero.png
json_schemas:
- name: Monero API Types
  property_count: 0
  slug: monero-types
jsonld:
- class_count: 10
  name: Monero Context
  property_count: 49
  slug: monero-context
layout: provider
modified: '2026-06-14'
name: Monero
nav: Providers
network: true
overview: 'Monero publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Blockchain API, JSON-RPC API, Mining API, and 5 more. Tagged areas include Cryptocurrency, Privacy, Blockchain, JSON-RPC, and Wallets.


  The Monero catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Monero''s developer surface includes documentation, Stack Overflow tag, engineering blog, and 19 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Monero API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: monero-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 61.3
    catalog_earned_first_party: 0.0
    catalog_gap: 53.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 50.3
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monero/refs/heads/main/screenshots/monero-2026-06-20T185722.png
security:
- kind: domain-security
  name: Monero Domain Security
  slug: monero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: monero
tags:
- Cryptocurrency
- Privacy
- Blockchain
- JSON-RPC
- Wallets
- Mining
- Transaction
website: https://www.getmonero.org/
---
