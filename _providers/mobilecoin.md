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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: JSON-RPC 2.0 wallet backend for the MobileCoin network - manage accounts and addresses, build and submit transactions, read balances, and query the ledger and network status. Self-hosted; runs locally
  name: MobileCoin Full-Service Wallet API
  slug: mobilecoin-full-service-wallet-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://mobilecoin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sentz.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://mobilecoin.gitbook.io/full-service-api/
- group: docs
  title: ''
  type: APIReference
  url: https://mobilecoin.gitbook.io/full-service-api/api-endpoints/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://mobilecoin.gitbook.io/full-service-api/usage/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mobilecoinofficial
- group: company
  title: ''
  type: Blog
  url: https://www.sentz.com/blog
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/sentzapp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sentz.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sentz.com/legal/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobilecoin-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mobilecoin-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mobilecoin-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/mobilecoin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mobilecoin-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mobilecoin-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mobilecoin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mobilecoin-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mobilecoin-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mobilecoin-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mobilecoin-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://mobilecoin.gitbook.io/full-service-api/api-endpoints/v1
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mobilecoin-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mobilecoin-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mobilecoin-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mobilecoin-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobilecoin-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mobilecoin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sentz.com/developers/bug-bounties
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mobilecoin-create-account-and-receive.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/mobilecoin-send-payment.md
created: '2026-07-17'
description: MobileCoin is a privacy-focused, mobile-first cryptocurrency and payments network whose consumer wallet has since been rebranded as Sentz (send, save, receive and earn in stablecoins, including the eUSD stablecoin). For developers and exchanges, MobileCoin publishes the open-source Full-Service Wallet API - a JSON-RPC 2.0 service (default 127.0.0.1:9090) that creates and manages accounts, assigns addresses, builds/submits transactions against the UTXO ledger, reads balances, and queries blocks and network status. It ships first-party Python, Swift (iOS), Android, and Flutter SDKs plus a Python CLI, with documentation on GitBook and open code across the mobilecoinofficial and mobilecoinfoundation GitHub organizations.
image: https://cdn.prod.website-files.com/652eb795295cf0f25eb7ab84/654e61ed4358885cde9b69ac_Opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: mobilecoin-mcp.yml
  slug: mobilecoin-mcpyml
modified: '2026-07-20'
name: Mobilecoin
nav: Providers
network: true
overview: 'Mobilecoin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Payments, Blockchain, and Digital Wallet.


  Mobilecoin''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, CLI, authentication, and 24 more developer resources.'
random_paper: 73
score:
  band: thin
  composite: 35.8
  delta: -4.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 75.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 39.5
  previous_composite: 40.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mobilecoin Authentication
  slug: mobilecoin-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mobilecoin Domain Security
  slug: mobilecoin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mobilecoin Vulnerability Disclosure
  slug: mobilecoin-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mobilecoin
tags:
- Company
- Cryptocurrency
- Payments
- Blockchain
- Digital Wallet
- Stablecoins
- Privacy
- JSON-RPC
website: https://mobilecoin.com/
---
