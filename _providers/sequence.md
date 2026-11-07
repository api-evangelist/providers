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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.9
  scored_at: '2026-11-06'
api_count: 7
apis:
- baseURL: https://mainnet-indexer.sequence.app
  baseurl_source: declared
  description: The Analytics API from Sequence — 177 operation(s) for analytics.
  name: Sequence Analytics API
  slug: sequence-analytics-api
- baseURL: https://mainnet-indexer.sequence.app
  baseurl_source: declared
  description: The Marketplace API from Sequence — 34 operation(s) for marketplace.
  name: Sequence Marketplace API
  slug: sequence-marketplace-api
- baseURL: https://mainnet-indexer.sequence.app
  baseurl_source: declared
  description: Endpoints accessible by passing your project-access-key in the header. This is injected whenever you login automatically.
  name: Sequence Public API
  slug: sequence-public-api
- baseURL: https://mainnet-indexer.sequence.app
  baseurl_source: declared
  description: The Rpc API from Sequence — 32 operation(s) for rpc.
  name: Sequence Rpc API
  slug: sequence-rpc-api
- baseURL: https://mainnet-indexer.sequence.app
  baseurl_source: declared
  description: Endpoints that require a Sequence service token intended to be secret. You can manually generate one on Sequence Builder and pass it as a Bearer Token.
  name: Sequence Secret API
  slug: sequence-secret-api
artifact_total: 16
asyncapis:
- description: ''
  name: Sequence Indexer Webhooks
  slug: sequence-indexer-webhooks
collections:
- collection_type: open
  name: Api Analytics API
  slug: open-sequence-analytics-api
- collection_type: open
  name: Api Analytics Marketplace API
  slug: open-sequence-marketplace-api
- collection_type: open
  name: Api Analytics public API
  slug: open-sequence-public-api
- collection_type: open
  name: Api Analytics Rpc API
  slug: open-sequence-rpc-api
- collection_type: open
  name: Api Analytics secret API
  slug: open-sequence-secret-api
common:
- group: other
  href: https://artifacts.apis.io/sequence/overlays/sequence-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sequence-analytics-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://sequence.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sequence.build
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sequence.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sequence.xyz/api-references/overview
- group: start
  title: ''
  type: SignUp
  url: https://sequence.build
- group: operate
  title: ''
  type: Support
  url: https://support.sequence.xyz/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.sequence.xyz/en/
- group: company
  title: ''
  type: Blog
  url: https://sequence.xyz/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/0xsequence
- group: commercial
  title: ''
  type: Pricing
  url: https://sequence.xyz/pricing
- group: operate
  href: https://artifacts.apis.io/sequence/lifecycle/sequence-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/sequence-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/sequence/changelog/sequence-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sequence-changelog.yml
- group: build
  href: https://artifacts.apis.io/sequence/packages/sequence-packages.yml
  title: ''
  type: Packages
  url: packages/sequence-packages.yml
- group: build
  href: https://artifacts.apis.io/sequence/packages/sequence-packages.yml
  title: ''
  type: SDKs
  url: packages/sequence-packages.yml
- group: build
  href: https://artifacts.apis.io/sequence/cli/sequence-cli.yml
  title: ''
  type: CLI
  url: cli/sequence-cli.yml
- group: design
  href: https://artifacts.apis.io/sequence/components/sequence-components.yml
  title: ''
  type: Components
  url: components/sequence-components.yml
- group: agent
  href: https://artifacts.apis.io/sequence/llms/sequence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sequence-llms.txt
- group: agent
  href: https://artifacts.apis.io/sequence/mcp/sequence-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sequence-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sequence/well-known/sequence-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sequence-well-known.yml
- group: auth
  href: https://artifacts.apis.io/sequence/authentication/sequence-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sequence-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sequence/security/sequence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sequence-domain-security.yml
- group: design
  href: https://artifacts.apis.io/sequence/conventions/sequence-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sequence-conventions.yml
- group: design
  href: https://artifacts.apis.io/sequence/errors/sequence-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sequence-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sequence/conformance/sequence-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sequence-conformance.yml
- group: design
  href: https://artifacts.apis.io/sequence/lifecycle/sequence-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sequence-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sequence/data-model/sequence-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sequence-data-model.yml
- group: start
  href: https://artifacts.apis.io/sequence/sandbox/sequence-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sequence-sandbox.yml
- group: design
  href: https://artifacts.apis.io/sequence/asyncapi/sequence-indexer-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sequence-indexer-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/sequence/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Sequence is a web3 developer platform (0xsequence, now part of Polygon Labs) for building blockchain applications: smart-contract wallets, a universal crypto payments and swap layer, a real-time multi-chain Indexer with balances, token prices, contract events and webhooks, plus Metadata, Marketplace, Transactions (Relayer) and Analytics APIs. Its backend APIs are webrpc-generated (POST /rpc/{Service}/{Method}) authenticated with a project access key and secret JWT, and it ships first-party SDKs for TypeScript, Go, Unity, Unreal, Kotlin and Swift plus a CLI. Backed by a16z and Polychain.'
image: https://sequence.xyz/favicon.ico
layout: provider
modified: '2026-07-21'
name: Sequence
nav: Providers
network: true
overview: 'Sequence publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Marketplace API, Public API, and 2 more. Tagged areas include Company, Web3, Blockchain, Wallets, and Payments.


  The Sequence catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sequence''s developer surface includes documentation, API reference, signup flow, support, engineering blog, pricing, changelog, and 23 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: Sequence API Rules
  rule_count: 43
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 3
  slug: sequence-rules
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 53.7
    developer_ergonomics: 58.9
    discoverability: 78.6
    operational_transparency: 42.1
  previous_composite: 41.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sequence/sequence-2026-08-17T081813.png
security:
- kind: authentication
  name: Sequence Authentication
  slug: sequence-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Sequence Domain Security
  slug: sequence-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: sequence-read-token-balances
  slug: sequence-read-token-balances
- name: sequence-watch-onchain-events
  slug: sequence-watch-onchain-events
slug: sequence
tags:
- Company
- Web3
- Blockchain
- Wallets
- Payments
- Cryptocurrency
- Indexer
- NFT
- Developer Platform
- Gaming
website: https://sequence.xyz
---
