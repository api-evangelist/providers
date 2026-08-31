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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: 'RESTful API (v1) to automate outbound payments from your own Telleroo account: manage recipients, query accounts and transactions, and create bank transfers (to a saved recipient or adhoc). Token auth'
  name: Telleroo Business API
  slug: telleroo-business-api
- description: 'RESTful Embedded Payments API (v3) to build Telleroo into your own platform: authorize against client companies over OAuth 2.0 (authorization code, scope "create"), enumerate companies and accounts, a'
  name: Telleroo Partner API
  slug: telleroo-partner-api
artifact_total: 7
asyncapis:
- description: Outbound webhook events emitted by the Telleroo Business API (v1) and Partner API (v3). Each delivery is an HTTP POST to the subscriber URL configured in the Telleroo dashboard and carries a subscribe
  name: Telleroo Webhooks
  slug: telleroo-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.telleroo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.telleroo.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telleroo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.telleroo.com/#introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.telleroo.com/api
- group: operate
  title: ''
  type: Support
  url: http://help.telleroo.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: http://help.telleroo.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.telleroo.com/blog-feed
- group: operate
  title: ''
  type: StatusPage
  url: https://status.telleroo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telleroo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.telleroo.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.telleroo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telleroo.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telleroo.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/telleroo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/telleroo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/telleroo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/telleroo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/telleroo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/telleroo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/telleroo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/telleroo-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/telleroo-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/telleroo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/telleroo-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telleroo-domain-security.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/telleroo-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/telleroo-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/telleroo-mcp.yml
created: '2026-07-17'
description: 'Telleroo is a UK bulk payments platform that automates supplier and payroll payments for businesses, accountants and bookkeepers. It provisions a ring-fenced e-money wallet in the customer''s name and sends bulk Faster Payments 24/7 (including bank holidays), plus international payments in 25+ currencies over SEPA, ACH and SWIFT. Built-in fraud controls include Confirmation of Payee, new/updated payee alerts and multi-level approval workflows, and it integrates with accounting and payroll software such as Xero, QuickBooks, Employment Hero and Staffology. Telleroo exposes two RESTful APIs: a Business API (v1, token auth) for automating outbound payments from your own account, and a Partner/Embedded Payments API (v3, OAuth 2.0) for building pay runs into your own platform on behalf of client companies. Both support idempotent requests, real-time webhooks and a dedicated sandbox environment.'
image: https://www.telleroo.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Telleroo MCP Server
  slug: telleroo-mcp-server
modified: '2026-07-21'
name: Telleroo
nav: Providers
network: true
overview: 'Telleroo publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Bulk Payments, Payroll, and Faster Payments.


  The Telleroo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Telleroo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 9
scopes:
- name: Telleroo Scopes
  scope_count: 1
  slug: telleroo-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 60.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 47.6
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telleroo/refs/heads/main/screenshots/telleroo-2026-08-17T082305.png
security:
- kind: authentication
  name: Telleroo Authentication
  slug: telleroo-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Telleroo Domain Security
  slug: telleroo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telleroo
tags:
- Company
- Payments
- Bulk Payments
- Payroll
- Faster Payments
- E-Money
- Fintech
- Banking
- International Payments
- Embedded Finance
website: https://www.telleroo.com
---
