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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-23'
api_count: 10
apis:
- description: The Accounts API from Lorum — 5 operation(s) for accounts.
  name: Lorum Accounts API
  slug: lorum-accounts-api
- description: The Customers API from Lorum — 10 operation(s) for customers.
  name: Lorum Customers API
  slug: lorum-customers-api
- description: The Customers V2 API from Lorum — 1 operation(s) for customers v2.
  name: Lorum Customers V2 API
  slug: lorum-customers-v2-api
- description: The Documents API from Lorum — 2 operation(s) for documents.
  name: Lorum Documents API
  slug: lorum-documents-api
- description: The Exchange API from Lorum — 2 operation(s) for exchange.
  name: Lorum Exchange API
  slug: lorum-exchange-api
- description: The Internal Transfers API from Lorum — 1 operation(s) for internal transfers.
  name: Lorum Internal Transfers API
  slug: lorum-internal-transfers-api
- description: The Oauth API from Lorum — 1 operation(s) for oauth.
  name: Lorum Oauth API
  slug: lorum-oauth-api
- description: The Payments API from Lorum — 2 operation(s) for payments.
  name: Lorum Payments API
  slug: lorum-payments-api
- description: The Simulation API from Lorum — 4 operation(s) for simulation.
  name: Lorum Simulation API
  slug: lorum-simulation-api
- description: The Transactions API from Lorum — 8 operation(s) for transactions.
  name: Lorum Transactions API
  slug: lorum-transactions-api
artifact_total: 14
asyncapis:
- description: Real-time webhook events emitted by Lorum for payments, transfers, currency exchanges, account changes, and customer onboarding. Generated from the provider's published webhook catalogue (docs.lorum.c
  name: Lorum (Fuse) Webhooks
  slug: lorum-webhooks-asyncapi
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lorum.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lorum.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lorum.com/reference/getting-a-bearer-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lorum.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/lorum-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lorum-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lorum-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lorum-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lorum-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lorum.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/lorum-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lorum-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lorum-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lorum-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lorum-well-known.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/lorum-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lorum-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lorum-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lorum-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.lorum.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lorum.com/legal/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.lorum.com/
- group: operate
  title: ''
  type: Support
  url: https://www.lorum.com/contact-us
- group: company
  title: ''
  type: Website
  url: https://www.lorum.com
created: '2026-07-17'
description: Lorum (developer brand "Fuse") is a fintech providing banking-grade clearing, settlement, and treasury infrastructure - "built for clearing, not lending." Through one API it offers multi-currency clearing across 30+ markets, programmable segregated account infrastructure (including virtual IBANs), and cash management with FX and liquidity sweeps. It targets payroll/EOR platforms, fintechs and PSPs, trading and investment platforms, and marketplaces that need to move and settle funds across global payment rails without standing up local banking entities. The API (OAuth2 client-credentials auth, idempotency-keyed money movement, and webhook event notifications) covers customers/KYC, accounts, payments, internal transfers, currency exchange, documents, batch payments, and full sandbox scheme simulation. Lorum is backed by Northzone.
image: https://cdn.prod.website-files.com/691dc048eb27bd1d29e459b1/692b0683e9466303595474d6_1ddad7f49147abb7075cab3048b9487b_Opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: lorum-mcp.yml
  slug: lorum-mcpyml
modified: '2026-07-20'
name: Lorum
nav: Providers
network: true
overview: 'Lorum publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Customers API, Customers V2 API, and 7 more. Tagged areas include Company, Fintech, Payments, Banking, and Clearing.


  The Lorum catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lorum''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, engineering blog, support, and 18 more developer resources.'
random_paper: 49
score:
  band: developing
  composite: 49.4
  delta: -0.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 69.7
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 50.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 45.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Lorum Authentication
  slug: lorum-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Lorum Domain Security
  slug: lorum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: lorum
tags:
- Company
- Fintech
- Payments
- Banking
- Clearing
- Settlement
- Treasury
- Multi-Currency
- Accounts
- Foreign Exchange
- Webhooks
website: https://www.lorum.com
---
