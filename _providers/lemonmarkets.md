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
    well_known_catalog: true
  schema_version: 0.1
  score: 83.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Lemonmarkets Agentic Access
  operation_count: 96
  slug: lemonmarkets-agentic-access
  summary_line: 96 operations · 33 acting
api_count: 17
apis:
- description: 'The Accounts: General API from lemon.markets — 6 operation(s) for accounts: general.'
  name: 'lemon.markets Accounts: General API'
  slug: lemonmarkets-accounts-general-api
- description: 'The Accounts: ID+V API from lemon.markets — 3 operation(s) for accounts: id+v.'
  name: 'lemon.markets Accounts: ID+V API'
  slug: lemonmarkets-accounts-id-v-api
- description: The Batch Orders API from lemon.markets — 4 operation(s) for batch orders.
  name: lemon.markets Batch Orders API
  slug: lemonmarkets-batch-orders-api
- description: The Businesses API from lemon.markets — 5 operation(s) for businesses.
  name: lemon.markets Businesses API
  slug: lemonmarkets-businesses-api
- description: The Cash Settlement API from lemon.markets — 5 operation(s) for cash settlement.
  name: lemon.markets Cash Settlement API
  slug: lemonmarkets-cash-settlement-api
- description: The Corporate Actions API from lemon.markets — 6 operation(s) for corporate actions.
  name: lemon.markets Corporate Actions API
  slug: lemonmarkets-corporate-actions-api
- description: The Documents API from lemon.markets — 4 operation(s) for documents.
  name: lemon.markets Documents API
  slug: lemonmarkets-documents-api
- description: The Events + Webhooks API from lemon.markets — 3 operation(s) for events + webhooks.
  name: lemon.markets Events + Webhooks API
  slug: lemonmarkets-events-webhooks-api
- description: The Instruments API from lemon.markets — 4 operation(s) for instruments.
  name: lemon.markets Instruments API
  slug: lemonmarkets-instruments-api
- description: The Money + Positions API from lemon.markets — 9 operation(s) for money + positions.
  name: lemon.markets Money + Positions API
  slug: lemonmarkets-money-positions-api
- description: The Orders API from lemon.markets — 4 operation(s) for orders.
  name: lemon.markets Orders API
  slug: lemonmarkets-orders-api
- description: The Persons API from lemon.markets — 4 operation(s) for persons.
  name: lemon.markets Persons API
  slug: lemonmarkets-persons-api
- description: The Securities Accounts API from lemon.markets — 2 operation(s) for securities accounts.
  name: lemon.markets Securities Accounts API
  slug: lemonmarkets-securities-accounts-api
- description: The Taxes API from lemon.markets — 4 operation(s) for taxes.
  name: lemon.markets Taxes API
  slug: lemonmarkets-taxes-api
- description: The Trades API from lemon.markets — 2 operation(s) for trades.
  name: lemon.markets Trades API
  slug: lemonmarkets-trades-api
- description: The Treasury Mandates API from lemon.markets — 9 operation(s) for treasury mandates.
  name: lemon.markets Treasury Mandates API
  slug: lemonmarkets-treasury-mandates-api
- description: Use workflows to perform repetitive tasks automatically.
  name: lemon.markets Workflows API
  slug: lemonmarkets-workflows-api
artifact_total: 22
asyncapis:
- description: ''
  name: Lemonmarkets Brokerage Webhooks
  slug: lemonmarkets-brokerage-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lemonmarkets-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lemonmarkets-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lemonmarkets-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lemonmarkets-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lemonmarkets-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lemonmarkets-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lemonmarkets-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.lemon.markets/changelog
- group: design
  title: ''
  type: Conformance
  url: conformance/lemonmarkets-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lemonmarkets-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/lemonmarkets-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lemonmarkets-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lemonmarkets-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lemonmarkets-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lemonmarkets-brokerage-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lemonmarkets-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lemonmarkets-brokerage-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.lemon.markets/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lemon.markets/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lemon.markets/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.lemon.markets/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.lemon.markets/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.lemon.markets/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lemonmarkets-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lemon.markets/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lemon-markets
- group: operate
  title: ''
  type: Support
  url: https://www.lemon.markets/en-de/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lemon.markets/en-de/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lemon.markets/en-de/privacy-policy
- group: other
  title: ''
  type: Imprint
  url: https://www.lemon.markets/en-de/imprint
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lemon-markets/
created: '2026-07-17'
description: lemon.markets is a Berlin-based, BaFin-licensed investment firm that sells brokerage infrastructure as an API. Its Brokerage API lets fintechs, banks and platforms embed investing — account opening and KYC/identification, securities accounts, order placement and execution, trades, positions, transactions, withdrawals, settlements, corporate actions, income distributions, tax exemption orders (Freistellungsauftrag) and treasury products — without building or licensing a broker-dealer stack themselves. Coverage spans 10,000+ ETFs, ETPs, stocks, bonds and funds, and the platform supports omnibus, fully disclosed and BPO (business process outsourcing) operating models. The REST API is complemented by a webhook/event surface, an Idempotency-Key contract on order placement, and a sandbox environment with published test ISINs. API access is invite-only.
image: https://www.lemon.markets/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: lemonmarkets-mcp.yml
  slug: lemonmarkets-mcpyml
modified: '2026-07-19'
name: lemon.markets
nav: Providers
network: true
overview: 'lemon.markets publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accounts: General API, Accounts: ID+V API, Batch Orders API, and 14 more. Tagged areas include Company, Fintech, Brokerage, Investing, and Trading.


  The lemon.markets catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  lemon.markets'' developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, changelog, support, and 25 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 51.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 60.9
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 51.2
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lemonmarkets/refs/heads/main/screenshots/lemonmarkets-2026-07-25T224849.png
security:
- kind: authentication
  name: Lemonmarkets Authentication
  slug: lemonmarkets-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Lemonmarkets Domain Security
  slug: lemonmarkets-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lemonmarkets
tags:
- Company
- Fintech
- Brokerage
- Investing
- Trading
- Embedded Finance
- Banking as a Service
- Securities
- Wealth Management
- Germany
- Europe
website: https://www.lemon.markets/
---
