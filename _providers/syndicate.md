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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Syndicate Agentic Access
  operation_count: 24
  slug: syndicate-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.syndicate.io
  baseurl_source: declared
  description: The api-key-manager > admin API from Syndicate — 11 operation(s) for api-key-manager > admin.
  name: Syndicate api-key-manager > admin API
  slug: syndicate-api-key-manager-admin-api
- baseURL: https://api.syndicate.io
  baseurl_source: declared
  description: The call API from Syndicate — 1 operation(s) for call.
  name: Syndicate Call API
  slug: syndicate-call-api
- baseURL: https://api.syndicate.io
  baseurl_source: declared
  description: The transact API from Syndicate — 1 operation(s) for transact.
  name: Syndicate Transact API
  slug: syndicate-transact-api
- baseURL: https://api.syndicate.io
  baseurl_source: declared
  description: The wallet API from Syndicate — 11 operation(s) for wallet.
  name: Syndicate Wallet API
  slug: syndicate-wallet-api
artifact_total: 17
asyncapis:
- description: ''
  name: Syndicate Webhooks
  slug: syndicate-webhooks
collections:
- collection_type: open
  name: api-key-manager > admin API
  slug: open-syndicate-api-key-manager-admin-api
- collection_type: open
  name: api-key-manager > admin call API
  slug: open-syndicate-call-api
- collection_type: open
  name: api-key-manager > admin transact API
  slug: open-syndicate-transact-api
- collection_type: open
  name: api-key-manager > admin wallet API
  slug: open-syndicate-wallet-api
common:
- group: other
  href: https://artifacts.apis.io/syndicate/overlays/syndicate-transaction-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/syndicate-transaction-cloud-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/syndicate/security/syndicate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/syndicate-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.syndicate.io
- group: docs
  title: ''
  type: Documentation
  url: https://tc.docs.syndicate.io
- group: docs
  title: ''
  type: APIReference
  url: https://tc.docs.syndicate.io/api/transactions/send-transaction
- group: start
  title: ''
  type: GettingStarted
  url: https://tc.docs.syndicate.io/get-started/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://tc.docs.syndicate.io/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://syndicate.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SyndicateProtocol
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.syndicate.io/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.syndicate.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://syndicate.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syndicate.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://syndicate.io
- group: agent
  href: https://artifacts.apis.io/syndicate/agentic-access/syndicate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/syndicate-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/syndicate/authentication/syndicate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/syndicate-authentication.yml
- group: build
  href: https://artifacts.apis.io/syndicate/packages/syndicate-packages.yml
  title: ''
  type: Packages
  url: packages/syndicate-packages.yml
- group: build
  href: https://artifacts.apis.io/syndicate/packages/syndicate-packages.yml
  title: ''
  type: SDKs
  url: packages/syndicate-packages.yml
- group: agent
  href: https://artifacts.apis.io/syndicate/mcp/syndicate-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/syndicate-mcp.yml
- group: agent
  href: https://artifacts.apis.io/syndicate/llms/syndicate-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/syndicate-llms.txt
- group: agent
  href: https://artifacts.apis.io/syndicate/well-known/syndicate-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/syndicate-well-known.yml
- group: design
  href: https://artifacts.apis.io/syndicate/conformance/syndicate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/syndicate-conformance.yml
- group: design
  href: https://artifacts.apis.io/syndicate/errors/syndicate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/syndicate-problem-types.yml
- group: design
  href: https://artifacts.apis.io/syndicate/lifecycle/syndicate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/syndicate-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/syndicate/conventions/syndicate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/syndicate-conventions.yml
- group: design
  href: https://artifacts.apis.io/syndicate/conventions/syndicate-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/syndicate-conventions.yml
- group: start
  href: https://artifacts.apis.io/syndicate/sandbox/syndicate-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/syndicate-sandbox.yml
- group: design
  href: https://artifacts.apis.io/syndicate/data-model/syndicate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/syndicate-data-model.yml
- group: design
  href: https://artifacts.apis.io/syndicate/asyncapi/syndicate-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/syndicate-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/syndicate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Syndicate is a web3 Transaction Cloud that abstracts blockchain transaction infrastructure for developers. Its REST APIs let teams broadcast transactions across EVM-compatible chains without managing private keys, nonces, or gas — with wallets and private keys secured inside HSM enclaves, guaranteed idempotency, managed gas, EIP-191 personal signing and EIP-712 typed-data signing and attestations, contract and function-signature authorization, IP allowlisting, and reliability-focused signed webhooks for real-time transaction status updates. Syndicate is backed by a16z crypto and ships an official Node.js SDK and a hosted MCP server for AI agents.
image: https://avatars.githubusercontent.com/u/76978866?s=200&v=4
layout: provider
mcp_servers:
- description: Official hosted MCP server published by Syndicate for AI client integration (Claude Code, Cursor, etc.). Serves the Syndicate documentation surface — including the Transaction Cloud API reference — to
  name: Syndicate MCP Server
  slug: syndicate-docs
modified: '2026-07-21'
name: Syndicate
nav: Providers
network: true
overview: 'Syndicate publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including api-key-manager > admin API, Call API, Transact API, and 1 more. Tagged areas include Blockchain, Web3, Ethereum, Transaction, and Wallets.


  The Syndicate catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Syndicate''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Syndicate API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 2
    warn: 4
  slug: syndicate-rules
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 56.7
    developer_ergonomics: 68.5
    discoverability: 71.7
    operational_transparency: 10.5
  previous_composite: 42.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: first-party
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
screenshot: https://apis.io/screenshots/syndicate/syndicate-2026-08-17T082233.png
security:
- kind: authentication
  name: Syndicate Authentication
  slug: syndicate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Syndicate Domain Security
  slug: syndicate-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 3
skills:
- name: Authorize a contract then broadcast a transaction
  slug: syndicate-authorize-and-transact
- name: Send and monitor an on-chain transaction
  slug: syndicate-send-and-monitor-transaction
- name: Sign EIP-712 typed data with a project wallet
  slug: syndicate-sign-typed-data
slug: syndicate
tags:
- Blockchain
- Web3
- Ethereum
- Transaction
- Wallets
- EVM
- Infrastructure
- Signing
- Webhook
- Cryptography
website: https://syndicate.io
---
