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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for the Request Finance platform — accounts payable / receivable, invoices, payroll, organizations and clients — that Consola Finance's crypto accounting product is now part of. JSON over HTT
  name: Request Finance API
  slug: request-finance-api
artifact_total: 6
asyncapis:
- description: ''
  name: Consola Finance Webhooks
  slug: consola-finance-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consola-finance-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.request.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.request.finance/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.request.finance/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.request.finance/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.request.finance/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.request.finance
- group: company
  title: ''
  type: Blog
  url: https://www.request.finance/category/product-updates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.request.finance
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RequestFinance
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/request-finance/workspace/request-finance-api-public
- group: auth
  title: ''
  type: Authentication
  url: authentication/consola-finance-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/consola-finance-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/consola-finance-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/consola-finance-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/consola-finance-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/consola-finance-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/consola-finance-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/consola-finance-scopes.yml
created: '2026-07-17'
description: Consola Finance is an enterprise-grade automated crypto accounting and finance platform for digital assets, acquired by and now operating as part of Request Finance. It lets finance and accounting teams monitor wallets across 25+ blockchains and 20+ exchanges (Binance, Coinbase, Kraken, KuCoin and others), automate bookkeeping, categorize and label on-chain transactions, filter spam, and generate audit-ready reports — transaction history, historical wallet balances, team breakdowns, contact lists, and realized / unrealized gains and losses — exported to CSV, XLSX and JSON, with integrations into existing ERP and accounting systems. As part of Request Finance it shares the Request Finance REST API for accounts payable / receivable, invoicing and payroll, authenticated with API keys or OAuth over JSON/HTTPS.
image: https://avatars.githubusercontent.com/RequestFinance
layout: provider
modified: '2026-07-18'
name: Consola Finance
nav: Providers
network: true
overview: 'Consola Finance publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Accounting, Digital Assets, Web3 Finance, and Accounts Payable.


  The Consola Finance catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Consola Finance''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, authentication, and 12 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 3
  name: Consola Finance Rate Limits
  slug: consola-finance-rate-limits
scopes:
- name: Consola Finance Scopes
  scope_count: 5
  slug: consola-finance-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.6
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 37.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/consola-finance/refs/heads/main/screenshots/consola-finance-2026-07-25T210307.png
security:
- kind: authentication
  name: Consola Finance Authentication
  slug: consola-finance-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Consola Finance Domain Security
  slug: consola-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: consola-finance
tags:
- Company
- Crypto Accounting
- Digital Assets
- Web3 Finance
- Accounts Payable
- Accounts Receivable
- Invoicing
- Payroll
- Bookkeeping
- Blockchain
website: https://docs.request.finance/
---
