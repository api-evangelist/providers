---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 97
  human_in_the_loop: 0
  name: Nano Agentic Access
  operation_count: 97
  slug: nano-agentic-access
  summary_line: 97 operations · 97 acting
api_count: 1
apis:
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Account balance, history, representative, and frontier queries
  name: Nano Accounts API
  slug: nano-accounts-api
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Block creation, processing, signing, and querying operations
  name: Nano Blocks API
  slug: nano-blocks-api
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Cryptographic key generation and derivation
  name: Nano Keys API
  slug: nano-keys-api
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Ledger-level queries for supply, frontiers, and account data
  name: Nano Ledger API
  slug: nano-ledger-api
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Node diagnostics, bootstrapping, peers, and confirmation management
  name: Nano Node API
  slug: nano-node-api
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Conversion between Nano and raw unit denominations
  name: Nano Unit Conversion API
  slug: nano-unit-conversion-api
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Local wallet management for development and testing
  name: Nano Wallets API
  slug: nano-wallets-api
- baseURL: http://localhost:7076
  baseurl_source: declared
  description: Proof-of-work generation, validation, and caching
  name: Nano Work API
  slug: nano-work-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nano RPC Accounts API
  slug: open-nano-accounts-api
- collection_type: open
  name: Nano RPC Accounts Blocks API
  slug: open-nano-blocks-api
- collection_type: open
  name: Nano RPC Accounts Keys API
  slug: open-nano-keys-api
- collection_type: open
  name: Nano RPC Accounts Ledger API
  slug: open-nano-ledger-api
- collection_type: open
  name: Nano RPC Accounts Node API
  slug: open-nano-node-api
- collection_type: open
  name: Nano RPC Accounts Unit Conversion API
  slug: open-nano-unit-conversion-api
- collection_type: open
  name: Nano RPC Accounts Wallets API
  slug: open-nano-wallets-api
- collection_type: open
  name: Nano RPC Accounts Work API
  slug: open-nano-work-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nano-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nano-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nano.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nano.org
- group: docs
  title: ''
  type: IntegrationGuides
  url: https://docs.nano.org/integration-guides/
- group: other
  title: ''
  type: WhitePaper
  url: https://docs.nano.org/living-whitepaper/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.nano.org/releases/current-release-notes/
- group: build
  title: ''
  type: DeveloperTools
  url: https://hub.nano.org/developer-tools
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nanocurrency
- group: operate
  title: ''
  type: Contact
  url: mailto:integrations@nano.org
- group: company
  title: ''
  type: Blog
  url: https://nano.org/en/blog/rss/
created: '2026-06-14'
description: Nano is a feeless, instant digital currency using a block-lattice architecture. It provides a JSON-RPC HTTP API for querying accounts, retrieving block information, managing wallets, processing transactions, and interacting with the Nano network. Each account maintains its own blockchain, enabling fast and lightweight consensus without mining.
examples:
- key_count: 2
  name: Account Balance
  slug: account-balance
- key_count: 2
  name: Block Info
  slug: block-info
- key_count: 2
  name: Send Transaction
  slug: send-transaction
- key_count: 2
  name: Unit Conversion
  slug: unit-conversion
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://nano.org/favicon.ico
json_schemas:
- name: Nano State Block
  property_count: 10
  slug: nano-block
- name: Nano RPC Request
  property_count: 18
  slug: nano-rpc-request
jsonld:
- class_count: 0
  name: Nano Context
  property_count: 25
  slug: nano-context
layout: provider
modified: '2026-06-14'
name: Nano
nav: Providers
network: true
overview: 'Nano publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Blocks API, Keys API, and 5 more. Tagged areas include Cryptocurrency, Payments, Blockchain, Feeless, and Instant Payments.


  The Nano catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nano''s developer surface includes documentation, release notes, GitHub presence, engineering blog, and 7 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 8
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Nano API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nano-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 54.3
    catalog_earned_first_party: 0.0
    catalog_gap: 60.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 48.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 21.1
  previous_composite: 27.4
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
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nano/refs/heads/main/screenshots/nano-2026-06-20T185939.png
security:
- kind: domain-security
  name: Nano Domain Security
  slug: nano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nano
tags:
- Cryptocurrency
- Payments
- Blockchain
- Feeless
- Instant Payments
- Digital Currency
website: https://nano.org
---
