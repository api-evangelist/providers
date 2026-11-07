---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Shapeshift Agentic Access
  operation_count: 25
  slug: shapeshift-agentic-access
  summary_line: 25 operations · 7 acting
api_count: 3
apis:
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Account API from Shapeshift — 3 operation(s) for account.
  name: Shapeshift Account API
  slug: shapeshift-account-api
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Fees API from Shapeshift — 3 operation(s) for fees.
  name: Shapeshift Fees API
  slug: shapeshift-fees-api
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Gas API from Shapeshift — 2 operation(s) for gas.
  name: Shapeshift Gas API
  slug: shapeshift-gas-api
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Info API from Shapeshift — 1 operation(s) for info.
  name: Shapeshift Info API
  slug: shapeshift-info-api
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Jsonrpc API from Shapeshift — 1 operation(s) for jsonrpc.
  name: Shapeshift Jsonrpc API
  slug: shapeshift-jsonrpc-api
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Send API from Shapeshift — 1 operation(s) for send.
  name: Shapeshift Send API
  slug: shapeshift-send-api
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Token API from Shapeshift — 1 operation(s) for token.
  name: Shapeshift Token API
  slug: shapeshift-token-api
- baseURL: https://api.ethereum.shapeshift.com/api/v1
  baseurl_source: declared
  description: The Tx API from Shapeshift — 2 operation(s) for tx.
  name: Shapeshift Tx API
  slug: shapeshift-tx-api
artifact_total: 17
asyncapis:
- description: ''
  name: Shapeshift Unchained Webhooks
  slug: shapeshift-unchained-webhooks
collections:
- collection_type: open
  name: '@shapeshiftoss/bitcoin-api v1 API'
  slug: open-shapeshift-v1-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/shapeshift/unchained/issues
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/shapeshift/unchained/blob/develop/CONTRIBUTING.MD
- group: commercial
  title: ''
  type: License
  url: https://github.com/shapeshift/unchained/blob/develop/LICENSE
- group: auth
  href: https://artifacts.apis.io/shapeshift/security/shapeshift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shapeshift-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/shapeshift/agentic-access/shapeshift-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shapeshift-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/shapeshift/authentication/shapeshift-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shapeshift-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://shapeshift.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://github.com/shapeshift/unchained
- group: docs
  title: ''
  type: Documentation
  url: https://api.ethereum.shapeshift.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.ethereum.shapeshift.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/shapeshift/unchained#readme
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shapeshift
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/shapeshift/unchained
- group: operate
  title: ''
  type: Support
  url: https://shapeshift.com/support
- group: company
  title: ''
  type: Blog
  url: https://shapeshift.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.shapeshift.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shapeshift.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shapeshift.com/privacy-policy
- group: build
  href: https://artifacts.apis.io/shapeshift/packages/shapeshift-packages.yml
  title: ''
  type: Packages
  url: packages/shapeshift-packages.yml
- group: build
  href: https://artifacts.apis.io/shapeshift/packages/shapeshift-packages.yml
  title: ''
  type: SDKs
  url: packages/shapeshift-packages.yml
- group: agent
  href: https://artifacts.apis.io/shapeshift/mcp/shapeshift-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/shapeshift-mcp.yml
- group: agent
  href: https://artifacts.apis.io/shapeshift/llms/shapeshift-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shapeshift-llms.txt
- group: design
  href: https://artifacts.apis.io/shapeshift/conformance/shapeshift-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shapeshift-conformance.yml
- group: design
  href: https://artifacts.apis.io/shapeshift/errors/shapeshift-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shapeshift-problem-types.yml
- group: design
  href: https://artifacts.apis.io/shapeshift/lifecycle/shapeshift-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shapeshift-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/shapeshift/conventions/shapeshift-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shapeshift-conventions.yml
- group: design
  href: https://artifacts.apis.io/shapeshift/data-model/shapeshift-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shapeshift-data-model.yml
- group: operate
  href: https://artifacts.apis.io/shapeshift/changelog/shapeshift-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shapeshift-changelog.yml
- group: design
  href: https://artifacts.apis.io/shapeshift/asyncapi/shapeshift-unchained-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shapeshift-unchained-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/shapeshift/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/shapeshift/overlays/shapeshift-ethereum-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shapeshift-ethereum-overlay.yaml
created: '2026-07-17'
description: ShapeShift is a community-owned, non-custodial multichain cryptocurrency platform where users buy, hold, trade, and earn with digital assets across 48+ blockchains and 10,000+ tokens while retaining full custody of their keys. Its open-source "unchained" backend exposes a public, key-free REST and WebSocket API that provides a common interface to many blockchains — account balances, transaction history, UTXOs, raw transaction broadcast, gas/fee estimation, and realtime pending/confirmed transaction updates — behind per-chain hosts such as api.ethereum.shapeshift.com and api.bitcoin.shapeshift.com. ShapeShift was founded in 2014, is backed by Earlybird Venture Capital, and today operates as a DAO with all code public under github.com/shapeshift.
image: https://shapeshift.com/apple-touch-icon.png
layout: provider
modified: '2026-07-21'
name: Shapeshift
nav: Providers
network: true
overview: 'Shapeshift publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Fees API, Gas API, and 5 more. Tagged areas include Company, Cryptocurrency, Blockchain, Bitcoin, and Ethereum.


  The Shapeshift catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Shapeshift''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 24 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Shapeshift API Rules
  rule_count: 57
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 2
  slug: shapeshift-rules
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 55.9
    developer_ergonomics: 66.1
    discoverability: 78.6
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 25.0
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 75.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/shapeshift/shapeshift-2026-08-17T081822.png
security:
- kind: authentication
  name: Shapeshift Authentication
  slug: shapeshift-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Shapeshift Domain Security
  slug: shapeshift-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 3
skills:
- name: Estimate fees and broadcast a signed EVM transaction
  slug: shapeshift-broadcast-evm-transaction
- name: Check a blockchain address balance and transaction history
  slug: shapeshift-check-address-activity
- name: List UTXOs and network fees for a Bitcoin/UTXO address
  slug: shapeshift-utxo-coin-control
slug: shapeshift
tags:
- Company
- Cryptocurrency
- Blockchain
- Bitcoin
- Ethereum
- Web3
- DeFi
- Wallets
- Trading
- Multi-Chain
website: https://shapeshift.com
---
