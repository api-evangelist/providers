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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.0
  scored_at: '2026-07-28'
api_count: 12
apis:
- description: The addresses API from Oumla Ltd — 5 operation(s) for addresses.
  name: Oumla Ltd addresses API
  slug: oumla-ltd-addresses-api
- description: The assets API from Oumla Ltd — 2 operation(s) for assets.
  name: Oumla Ltd assets API
  slug: oumla-ltd-assets-api
- description: The contract-interactions API from Oumla Ltd — 4 operation(s) for contract-interactions.
  name: Oumla Ltd contract-interactions API
  slug: oumla-ltd-contract-interactions-api
- description: The contract-templates API from Oumla Ltd — 5 operation(s) for contract-templates.
  name: Oumla Ltd contract-templates API
  slug: oumla-ltd-contract-templates-api
- description: The deployed-contracts API from Oumla Ltd — 5 operation(s) for deployed-contracts.
  name: Oumla Ltd deployed-contracts API
  slug: oumla-ltd-deployed-contracts-api
- description: The networks API from Oumla Ltd — 2 operation(s) for networks.
  name: Oumla Ltd networks API
  slug: oumla-ltd-networks-api
- description: The profiles API from Oumla Ltd — 1 operation(s) for profiles.
  name: Oumla Ltd profiles API
  slug: oumla-ltd-profiles-api
- description: The tokenization API from Oumla Ltd — 9 operation(s) for tokenization.
  name: Oumla Ltd tokenization API
  slug: oumla-ltd-tokenization-api
- description: The transactions API from Oumla Ltd — 4 operation(s) for transactions.
  name: Oumla Ltd transactions API
  slug: oumla-ltd-transactions-api
- description: The wallets API from Oumla Ltd — 3 operation(s) for wallets.
  name: Oumla Ltd wallets API
  slug: oumla-ltd-wallets-api
- description: The withdraw API from Oumla Ltd — 1 operation(s) for withdraw.
  name: Oumla Ltd withdraw API
  slug: oumla-ltd-withdraw-api
- description: The workflows API from Oumla Ltd — 1 operation(s) for workflows.
  name: Oumla Ltd workflows API
  slug: oumla-ltd-workflows-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://oumla.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.oumla.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oumla.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oumla.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oumla.com/guides/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/oumla-ltd-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oumla-ltd-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/oumla-ltd-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/oumla-ltd-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oumla-ltd-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oumla.com/changelog
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oumla-ltd-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oumla-ltd-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oumla-ltd-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oumla-ltd-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oumla-ltd-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://oumla.com/blog/oumla-achieves-soc-2-type-ii-certification
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oumla-ltd-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oumla-ltd-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.oumla.com/guides/faqs
- group: company
  title: ''
  type: Blog
  url: https://oumla.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oumla
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.oumla.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oumla.com/privacy-policy
created: '2026-07-17'
description: Oumla is a Saudi-based provider of enterprise-grade digital asset infrastructure for regulated institutions. Its Core API delivers MPC-based wallet and address management, portfolio and native-balance queries, on-chain transaction tracking, smart-contract templates plus deployment and read/write interactions, and tokenization (collections, issue, mint, burn) for tokenized securities, fund units, sukuk, and NFTs. Products span Digital Assets Infrastructure (custody, policy engines, lifecycle), Capital Markets Tokenization, the Oumla Financial Chain for Shariah-compliant interbank settlement, and Bahith blockchain monitoring and compliance analytics built for Saudi data sovereignty. Authentication is via the x-api-key header; long-running mutations run as async workflows. Oumla is SOC 2 Type II and ISO 27001 certified.
image: https://oumla.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: oumla-ltd-mcp.yml
  slug: oumla-ltd-mcpyml
modified: '2026-07-20'
name: Oumla Ltd
nav: Providers
network: true
overview: 'Oumla Ltd publishes 12 APIs on the [APIs.io](https://apis.io/) network, including addresses API, assets API, contract-interactions API, and 9 more. Tagged areas include Company, Blockchain, Digital Assets, Wallet Infrastructure, and Custody.


  Oumla Ltd''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, changelog, support, and 18 more developer resources.'
random_paper: 64
score:
  band: developing
  composite: 47.8
  delta: -1.3
  facets:
    commercial_clarity: 31.6
    contract_quality: 57.3
    developer_ergonomics: 69.0
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 21.1
  previous_composite: 49.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Oumla Ltd Authentication
  slug: oumla-ltd-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Oumla Ltd Domain Security
  slug: oumla-ltd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oumla-ltd
tags:
- Company
- Blockchain
- Digital Assets
- Wallet Infrastructure
- Custody
- Tokenization
- Smart Contracts
- Web3
- Fintech
- Saudi Arabia
website: https://oumla.com
---
