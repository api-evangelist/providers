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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-02'
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
  name: Syndicate call API
  slug: syndicate-call-api
- baseURL: https://api.syndicate.io
  baseurl_source: declared
  description: The transact API from Syndicate — 1 operation(s) for transact.
  name: Syndicate transact API
  slug: syndicate-transact-api
- baseURL: https://api.syndicate.io
  baseurl_source: declared
  description: The wallet API from Syndicate — 11 operation(s) for wallet.
  name: Syndicate wallet API
  slug: syndicate-wallet-api
artifact_total: 14
asyncapis:
- description: ''
  name: Syndicate Webhooks
  slug: syndicate-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: Overlay
  url: overlays/syndicate-transaction-cloud-overlay.yaml
- group: auth
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
  title: ''
  type: AgenticAccess
  url: agentic-access/syndicate-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/syndicate-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/syndicate-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/syndicate-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syndicate-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syndicate-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/syndicate-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/syndicate-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/syndicate-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syndicate-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/syndicate-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/syndicate-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/syndicate-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/syndicate-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/syndicate-webhooks.yml
- group: agent
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
  slug: syndicate-mcp-server
modified: '2026-07-21'
name: Syndicate
nav: Providers
network: true
overview: 'Syndicate publishes 4 APIs on the [APIs.io](https://apis.io/) network, including api-key-manager > admin API, call API, transact API, and 1 more. Tagged areas include Blockchain, Web3, Ethereum, Transaction, and Wallets.


  The Syndicate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syndicate''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 19
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 56.2
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/syndicate/refs/heads/main/screenshots/syndicate-2026-08-17T082233.png
security:
- kind: authentication
  name: Syndicate Authentication
  slug: syndicate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Syndicate Domain Security
  slug: syndicate-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
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
