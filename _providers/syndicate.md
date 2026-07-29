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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Syndicate Agentic Access
  operation_count: 24
  slug: syndicate-agentic-access
  summary_line: 24 operations · 14 acting
api_count: 4
apis:
- description: The api-key-manager > admin API from Syndicate — 11 operation(s) for api-key-manager > admin.
  name: Syndicate api-key-manager > admin API
  slug: syndicate-api-key-manager-admin-api
- description: The call API from Syndicate — 1 operation(s) for call.
  name: Syndicate call API
  slug: syndicate-call-api
- description: The transact API from Syndicate — 1 operation(s) for transact.
  name: Syndicate transact API
  slug: syndicate-transact-api
- description: The wallet API from Syndicate — 11 operation(s) for wallet.
  name: Syndicate wallet API
  slug: syndicate-wallet-api
artifact_total: 9
asyncapis:
- description: ''
  name: Syndicate Webhooks
  slug: syndicate-webhooks
common:
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
- description: ''
  name: syndicate-mcp.yml
  slug: syndicate-mcpyml
modified: '2026-07-21'
name: Syndicate
nav: Providers
network: true
overview: 'Syndicate publishes 4 APIs on the [APIs.io](https://apis.io/) network, including api-key-manager > admin API, call API, transact API, and 1 more. Tagged areas include Blockchain, Web3, Ethereum, Transactions, and Wallets.


  The Syndicate catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syndicate''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 49.8
  delta: 0.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.3
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Transactions
- Wallets
- EVM
- Infrastructure
- Signing
- Webhooks
- Cryptography
website: https://syndicate.io
---
