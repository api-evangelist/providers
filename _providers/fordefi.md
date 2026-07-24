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
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 79.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Fordefi Agentic Access
  operation_count: 75
  slug: fordefi-agentic-access
  summary_line: 75 operations · 45 acting
api_count: 17
apis:
- description: These endpoints allow you to list the contacts in your address book.<br><br>To add/remove contacts, visit the Fordefi web console. See the <a href='https://docs.fordefi.com/user-guide/address-book'>us
  name: Fordefi Address Book API
  slug: fordefi-address-book-api
- description: These endpoints allow you to get information about the assets in your organization, including metadata, balances, and prices. <br><br> Fordefi supports native assets and fungible tokens on each of the
  name: Fordefi Assets API
  slug: fordefi-assets-api
- description: These endpoints allow you to manage audit logs. <br><br> Audit logs are used to track the actions of users in your organization.
  name: Fordefi Audit Log API
  slug: fordefi-audit-log-api
- description: These endpoints allow you to manage end-user authorization tokens used for Fordefi's WaaS solution.<br><br>Authorization tokens allow end users to authenticate with Fordefi. Each end user can have a m
  name: Fordefi Authorization Tokens API
  slug: fordefi-authorization-tokens-api
- description: These endpoints allow you to manage batch transactions on the Fordefi platform. <br><br> Batch transactions are currently supported only on Solana, for the purpose of supporting the `signAllTransactio
  name: Fordefi Batch Transactions API
  slug: fordefi-batch-transactions-api
- description: These endpoints allow you to get information about blockchains supported by Fordefi.
  name: Fordefi Blockchains API
  slug: fordefi-blockchains-api
- description: The Enclave Keys API from Fordefi — 1 operation(s) for enclave keys.
  name: Fordefi Enclave Keys API
  slug: fordefi-enclave-keys-api
- description: 'These endpoints allow you to manage WaaS end-users. <br><br> End users correspond to users of the platform who has integrated the Fordefi WaaS solution. For example, in the case of a retail platform, '
  name: Fordefi End Users API
  slug: fordefi-end-users-api
- description: These endpoints allow you to manage asynchronous actions such as data exports.
  name: Fordefi Exports API
  slug: fordefi-exports-api
- description: The Organizations API from Fordefi — 4 operation(s) for organizations.
  name: Fordefi Organizations API
  slug: fordefi-organizations-api
- description: These endpoints allow you to manage swaps.
  name: Fordefi Swaps API
  slug: fordefi-swaps-api
- description: 'These endpoints allow you to manage transactions on the Fordefi platform. <br><br> A transaction represents an operation that can be one of the following: <ul> <li>An on-chain action that modifies blo'
  name: Fordefi Transactions API
  slug: fordefi-transactions-api
- description: These endpoints allow you to view your user groups. <br><br> User Groups are used to collectively manage policies and view permissions for a group of users. <br><br> The API is read-only. To manage us
  name: Fordefi User Groups API
  slug: fordefi-user-groups-api
- description: 'These endpoints allow you to get information about users in your Fordefi organization. There are several types of users in the Fordefi platform: - **Person**: A human user of the platform. - **API Use'
  name: Fordefi Users API
  slug: fordefi-users-api
- description: These endpoints allow you to view your vault groups. <br><br> Vault Groups are used to collectively manage policies and view permissions for a group of vaults. <br><br> The API is read-only. To manage
  name: Fordefi Vault Groups API
  slug: fordefi-vault-groups-api
- description: These endpoints allow you to manage vaults. <br><br> A vault is the basic unit to manage funds. Each vault supports a single "chain family", such as EVM, Bitcoin, Solana, Cosmos, etc., determined by t
  name: Fordefi Vaults API
  slug: fordefi-vaults-api
- description: 'These endpoints allow you to manually trigger your pre-configured webhooks.<br><br><a href=''https://docs.fordefi.com/reference/webhooks''>Use Webhooks</a> describes how to configure webhooks, validate '
  name: Fordefi Webhooks API
  slug: fordefi-webhooks-api
artifact_total: 23
asyncapis:
- description: ''
  name: Fordefi Webhooks
  slug: fordefi-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://fordefi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fordefi.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fordefi.com/developers/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fordefi.com/api/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fordefi.com/developers/getting-started/create-an-api-user
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FordefiHQ
- group: company
  title: ''
  type: Blog
  url: https://blog.fordefi.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fordefi.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.fordefi.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fordefi.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fordefi.com/privacy-policy
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.fordefi.com/changelog/upcoming
- group: auth
  title: ''
  type: Compliance
  url: https://fordefi.com/solutions/mpc-security
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fordefi-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fordefi-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fordefi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fordefi-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fordefi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fordefi-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fordefi-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fordefi-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/fordefi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fordefi-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fordefi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fordefi-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/fordefi-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/fordefi-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fordefi-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fordefi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fordefi-agentic-access.yml
created: '2026-07-17'
description: Fordefi is an institutional MPC (multi-party computation) wallet and digital-asset security platform for DeFi, trading, and on-chain payments. Its developer API lets teams programmatically create vaults across 10+ blockchain families (EVM, Bitcoin, Solana, Cosmos and more), manage addresses and assets, and build, approve, sign, and broadcast transactions under a policy engine with built-in AML screening and audit logging. Authentication combines a Bearer JWT access token with ECDSA (NIST P-256) request signing by a registered API Signer; state-changing calls support idempotency and a signed webhook event surface for real-time monitoring. Fordefi is SOC 2 Type II certified. This profile was enriched by the API Evangelist pipeline from Fordefi's public OpenAPI and developer documentation.
image: https://cdn.prod.website-files.com/634ff29071ccb50e6fb7f68e/6368e19b2728473fafde3adb_fordefi.jpeg
layout: provider
mcp_servers:
- description: ''
  name: fordefi-mcp.yml
  slug: fordefi-mcpyml
modified: '2026-07-19'
name: Fordefi
nav: Providers
network: true
overview: 'Fordefi publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Address Book API, Assets API, Audit Log API, and 14 more. Tagged areas include Company, Security, Cryptocurrency, Digital Assets, and Wallet.


  The Fordefi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fordefi''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, authentication, and 24 more developer resources.'
random_paper: 21
score:
  band: developing
  composite: 58.8
  delta: 1.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.6
    developer_ergonomics: 69.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 57.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Fordefi Authentication
  slug: fordefi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fordefi Domain Security
  slug: fordefi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fordefi Trust Center
  slug: fordefi-trust-center
  summary_line: SOC 2 Type II
slug: fordefi
tags:
- Company
- Security
- Cryptocurrency
- Digital Assets
- Wallet
- Custody
- Blockchain
- DeFi
- MPC
- Payments
website: https://fordefi.com/
---
