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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The Address Book API from Utila — 5 operation(s) for address book.
  name: Utila Address Book API
  slug: utila-address-book-api
- description: The Assets API from Utila — 3 operation(s) for assets.
  name: Utila Assets API
  slug: utila-assets-api
- description: The Balances API from Utila — 5 operation(s) for balances.
  name: Utila Balances API
  slug: utila-balances-api
- description: The Blockchains API from Utila — 4 operation(s) for blockchains.
  name: Utila Blockchains API
  slug: utila-blockchains-api
- description: The Transactions API from Utila — 11 operation(s) for transactions.
  name: Utila Transactions API
  slug: utila-transactions-api
- description: The Vaults API from Utila — 2 operation(s) for vaults.
  name: Utila Vaults API
  slug: utila-vaults-api
- description: The Wallets API from Utila — 10 operation(s) for wallets.
  name: Utila Wallets API
  slug: utila-wallets-api
artifact_total: 19
asyncapis:
- description: ''
  name: Utila Webhooks
  slug: utila-webhooks
collections:
- collection_type: postman
  name: Utila Address Book API
  slug: postman-utila-address-book-api
- collection_type: postman
  name: Utila Address Book Assets API
  slug: postman-utila-assets-api
- collection_type: postman
  name: Utila Address Book Balances API
  slug: postman-utila-balances-api
- collection_type: postman
  name: Utila Address Book Blockchains API
  slug: postman-utila-blockchains-api
- collection_type: postman
  name: Utila Address Book Transactions API
  slug: postman-utila-transactions-api
- collection_type: postman
  name: Utila Address Book Vaults API
  slug: postman-utila-vaults-api
- collection_type: postman
  name: Utila Address Book Wallets API
  slug: postman-utila-wallets-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/utila/overview
- group: company
  title: ''
  type: Website
  url: https://utila.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.utila.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.utila.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.utila.io/reference/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.utila.io/reference/example-client
- group: company
  title: ''
  type: Blog
  url: https://utila.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/utila-io
- group: commercial
  title: ''
  type: Pricing
  url: https://utila.io/pricing
- group: start
  title: ''
  type: Login
  url: https://console.utila.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://utila.io/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://utila.io/legal/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://utila.io/contact
- group: operate
  title: ''
  type: Support
  url: https://support.utila.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.utila.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/utila-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.utila.io/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utila-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/utila-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/utila-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/utila-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/utila-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/utila-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/utila-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/utila-conformance.yml
- group: build
  title: ''
  type: CLI
  url: cli/utila-cli.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/utila-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/utila-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/utila-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/utila-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/utila-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/utila-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/utila-data-model.yml
created: '2026-07-17'
description: Utila is an institutional digital asset wallet and stablecoin infrastructure platform for fintechs and enterprises. Built on MPC (multi-party computation) key management, it provides secure custody with policy-driven governance, embedded compliance and AML screening, and a resource-oriented REST API for programmatically managing vaults, MPC wallets, addresses, balances, and transactions across many blockchains — including sponsored (gas-abstracted) transfers, transaction simulation, an automated Co-Signer for signing workflows, webhooks, and a first-party CLI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/utila.png
layout: provider
mcp_servers:
- description: ''
  name: utila-mcp.yml
  slug: utila-mcpyml
modified: '2026-07-21'
name: Utila
nav: Providers
network: true
overview: 'Utila publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Address Book API, Assets API, Balances API, and 4 more. Tagged areas include Company, Web3, Digital Assets, Stablecoins, and Custody.


  The Utila catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Utila''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, authentication, and 27 more developer resources.'
random_paper: 4
score:
  band: strong
  composite: 58.2
  delta: -3.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 63.6
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 62.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Utila Authentication
  slug: utila-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Utila Domain Security
  slug: utila-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Utila Trust Center
  slug: utila-trust-center
  summary_line: SOC 2 Type II
slug: utila
tags:
- Company
- Web3
- Digital Assets
- Stablecoins
- Custody
- MPC Wallets
- Blockchain
- Payments
- Treasury
website: https://utila.io/
---
