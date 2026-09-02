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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'REST API for online checkout and credit-application flows: retrieve supported devices, begin a sale, and receive completion webhooks. Bearer-token authenticated plus a symmetric E-commerce key for enc'
  name: PayJoy E-commerce API
  slug: payjoy-e-commerce-api
- description: Retrieve cart information.
  name: PayJoy Carts API
  slug: payjoy-carts-api
- description: The Down Payments API from PayJoy — 1 operation(s) for down payments.
  name: PayJoy Down Payments API
  slug: payjoy-down-payments-api
- description: Retrieve merchants information.
  name: PayJoy Merchants API
  slug: payjoy-merchants-api
- description: The Reconciliation API from PayJoy — 1 operation(s) for reconciliation.
  name: PayJoy Reconciliation API
  slug: payjoy-reconciliation-api
- description: The Repayments API from PayJoy — 3 operation(s) for repayments.
  name: PayJoy Repayments API
  slug: payjoy-repayments-api
- description: Retrieve sales clerks information.
  name: PayJoy SalesClerks API
  slug: payjoy-salesclerks-api
- description: Displays the status of the application.
  name: PayJoy Status API
  slug: payjoy-status-api
- description: Endpoints related to vouchers management
  name: PayJoy Vouchers API
  slug: payjoy-vouchers-api
artifact_total: 22
asyncapis:
- description: ''
  name: Payjoy Webhooks
  slug: payjoy-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PayJoy Partner API V2 Carts API
  slug: open-payjoy-carts-api
- collection_type: open
  name: PayJoy Partner API V2 Carts Down Payments API
  slug: open-payjoy-down-payments-api
- collection_type: open
  name: PayJoy Partner API V2 Carts Merchants API
  slug: open-payjoy-merchants-api
- collection_type: open
  name: PayJoy Partner API V2 Carts Reconciliation API
  slug: open-payjoy-reconciliation-api
- collection_type: open
  name: PayJoy Partner API V2 Carts Repayments API
  slug: open-payjoy-repayments-api
- collection_type: open
  name: PayJoy Partner API V2 Carts SalesClerks API
  slug: open-payjoy-salesclerks-api
- collection_type: open
  name: PayJoy Partner API V2 Carts Status API
  slug: open-payjoy-status-api
- collection_type: open
  name: PayJoy Partner API V2 Carts Vouchers API
  slug: open-payjoy-vouchers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/payjoy-partner-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.payjoy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.payjoy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.payjoy.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.payjoy.com/sales-integration/quickstart/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://developers.payjoy.com/sales-integration/support/faq
- group: start
  title: ''
  type: SignUp
  url: https://app.payjoy.com/admin-console/login
- group: company
  title: ''
  type: Blog
  url: https://www.payjoy.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.payjoy.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.payjoy.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/payjoy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payjoy-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/payjoy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/payjoy-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/payjoy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/payjoy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payjoy-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/payjoy-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payjoy-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/payjoy-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/payjoy-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/payjoy-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payjoy-domain-security.yml
created: '2026-07-17'
description: 'PayJoy is a fintech that provides financial access to underserved consumers in emerging markets through smartphone financing and a secured credit card that requires only a government ID. Its Partner Developer Portal exposes a REST Partner API (Sales Integration) so retail and OEM partners can integrate PayJoy point-of-sale financing: retrieve cart and sale information, list merchants and sales clerks, offer and process customer repayments, create and pay payment references, redeem and cancel vouchers, pay down payments, and pull transaction history for reconciliation. A separate E-commerce API supports online checkout and credit-application flows. Authentication is by API key; webhooks are HMAC-SHA256 signed. Founded 2015; backed by Greylock and Union Square Ventures.'
image: https://avatars.githubusercontent.com/u/15761776?v=4
layout: provider
mcp_servers:
- description: ''
  name: PayJoy MCP Server
  slug: payjoy-mcp-server
modified: '2026-07-20'
name: PayJoy
nav: Providers
network: true
overview: 'PayJoy publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Carts API, Down Payments API, Merchants API, and 5 more. Tagged areas include Company, Fintech, Payments, Lending, and Buy Now Pay Later.


  The PayJoy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PayJoy''s developer surface includes documentation, getting-started guide, support, signup flow, engineering blog, authentication, sandbox, and 17 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 62.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 46.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/payjoy/refs/heads/main/screenshots/payjoy-2026-08-07T191639.png
security:
- kind: authentication
  name: Payjoy Authentication
  slug: payjoy-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Payjoy Domain Security
  slug: payjoy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payjoy
tags:
- Company
- Fintech
- Payments
- Lending
- Buy Now Pay Later
- Point-of-Sale
- Emerging Markets
- Financial Inclusion
- Partner API
website: https://www.payjoy.com/
---
