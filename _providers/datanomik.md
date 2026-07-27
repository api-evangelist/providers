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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 69.2
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Datanomik Agentic Access
  operation_count: 21
  slug: datanomik-agentic-access
  summary_line: 21 operations · 2 acting
api_count: 10
apis:
- description: The Accounts API from Datanomik — 5 operation(s) for accounts.
  name: Datanomik Accounts API
  slug: datanomik-accounts-api
- description: The Applications API from Datanomik — 1 operation(s) for applications.
  name: Datanomik Applications API
  slug: datanomik-applications-api
- description: The Balances API from Datanomik — 1 operation(s) for balances.
  name: Datanomik Balances API
  slug: datanomik-balances-api
- description: The General Owners API from Datanomik — 2 operation(s) for general owners.
  name: Datanomik General Owners API
  slug: datanomik-general-owners-api
- description: The Investments API from Datanomik — 4 operation(s) for investments.
  name: Datanomik Investments API
  slug: datanomik-investments-api
- description: The Links API from Datanomik — 1 operation(s) for links.
  name: Datanomik Links API
  slug: datanomik-links-api
- description: The Payment Slips API from Datanomik — 1 operation(s) for payment slips.
  name: Datanomik Payment Slips API
  slug: datanomik-payment-slips-api
- description: The Payments API from Datanomik — 2 operation(s) for payments.
  name: Datanomik Payments API
  slug: datanomik-payments-api
- description: The Pix Transactions API from Datanomik — 2 operation(s) for pix transactions.
  name: Datanomik Pix Transactions API
  slug: datanomik-pix-transactions-api
- description: The Transactions API from Datanomik — 2 operation(s) for transactions.
  name: Datanomik Transactions API
  slug: datanomik-transactions-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datanomik-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datanomik-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.datanomik.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datanomik.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.datanomik.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datanomik.com/docs/quick-start
- group: start
  title: ''
  type: Quickstart
  url: https://docs.datanomik.com/docs/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.datanomik.com/#/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.datanomik.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@datanomik.com
- group: company
  title: ''
  type: Blog
  url: https://datanomik.com/entre-tesoureiros
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datanomik.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datanomik
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datanomik.com/termos-e-condicoes
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datanomik.com/politica-de-privacidade
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/datanomik-team/workspace/datanomik-api/overview/
- group: company
  title: ''
  type: Website
  url: https://datanomik.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datanomik/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datanomik-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/datanomik-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datanomik-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/datanomik-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datanomik-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/datanomik-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/datanomik-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/datanomik-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/datanomik-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://datanomik.com/seguranca
- group: agent
  title: ''
  type: MCPServer
  url: mcp/datanomik-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/datanomik-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Datanomik is a Brazilian open finance and treasury-management platform that gives mid-to-large enterprises real-time, consolidated visibility across their bank accounts, balances, investments and payments through a single API. Authorized by Banco Central do Brasil as a Payment Transaction Initiator (ITP) and a participant in Brazil's Open Finance ecosystem, Datanomik connects to 30+ Brazilian financial institutions (Banco do Brasil, Itau, Bradesco, Caixa, BTG, Nubank, Safra, Mercado Pago and others) to deliver bank connectivity, cash and liquidity management, investment-portfolio tracking, cash-flow forecasting, cash pooling and transfers, automated bank statements and financial reporting. The company exposes two REST APIs - an OpenBanking data API and a Treasury/Remuneration API - secured with HTTP Basic API keys, documented on a ReadMe developer portal with a public Postman workspace and a dedicated sandbox. Backed by a16z, its clients include iFood, Magalu, Flamengo and Unimed.
image: https://datanomik.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: datanomik-mcp.yml
  slug: datanomik-mcpyml
modified: '2026-07-18'
name: Datanomik
nav: Providers
network: true
overview: 'Datanomik publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Applications API, Balances API, and 7 more. Tagged areas include Company, Open Finance, Open Banking, Treasury Management, and Cash Management.


  Datanomik''s developer surface includes documentation, API reference, getting-started guide, quickstart, signup flow, support, engineering blog, and 24 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 52.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 55.2
    developer_ergonomics: 78.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 52.8
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datanomik/refs/heads/main/screenshots/datanomik-2026-07-25T211349.png
security:
- kind: authentication
  name: Datanomik Authentication
  slug: datanomik-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Datanomik Domain Security
  slug: datanomik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datanomik
tags:
- Company
- Open Finance
- Open Banking
- Treasury Management
- Cash Management
- Payments
- PIX
- Financial Data
- Bank Connectivity
- Brazil
- LatAm
- Fintech
website: https://datanomik.com
---
