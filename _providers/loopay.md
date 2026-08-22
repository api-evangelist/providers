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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Loopay Agentic Access
  operation_count: 31
  slug: loopay-agentic-access
  summary_line: 31 operations · 9 acting
api_count: 15
apis:
- description: The Affiliate API from Loopay — 4 operation(s) for affiliate.
  name: Loopay Affiliate API
  slug: loopay-affiliate-api
- description: The Bank API from Loopay — 1 operation(s) for bank.
  name: Loopay Bank API
  slug: loopay-bank-api
- description: The Company API from Loopay — 1 operation(s) for company.
  name: Loopay Company API
  slug: loopay-company-api
- description: The CompanyProduct API from Loopay — 1 operation(s) for companyproduct.
  name: Loopay CompanyProduct API
  slug: loopay-companyproduct-api
- description: The Country API from Loopay — 1 operation(s) for country.
  name: Loopay Country API
  slug: loopay-country-api
- description: The Currency API from Loopay — 1 operation(s) for currency.
  name: Loopay Currency API
  slug: loopay-currency-api
- description: The DocumentType API from Loopay — 1 operation(s) for documenttype.
  name: Loopay DocumentType API
  slug: loopay-documenttype-api
- description: The Movements API from Loopay — 1 operation(s) for movements.
  name: Loopay Movements API
  slug: loopay-movements-api
- description: The PaidMethods API from Loopay — 1 operation(s) for paidmethods.
  name: Loopay PaidMethods API
  slug: loopay-paidmethods-api
- description: The PayIn API from Loopay — 2 operation(s) for payin.
  name: Loopay PayIn API
  slug: loopay-payin-api
- description: The Payout API from Loopay — 6 operation(s) for payout.
  name: Loopay Payout API
  slug: loopay-payout-api
- description: The PhysicalPoint API from Loopay — 1 operation(s) for physicalpoint.
  name: Loopay PhysicalPoint API
  slug: loopay-physicalpoint-api
- description: The SourcesOfPayment API from Loopay — 5 operation(s) for sourcesofpayment.
  name: Loopay SourcesOfPayment API
  slug: loopay-sourcesofpayment-api
- description: The SourcesOfPaymentAdmin API from Loopay — 3 operation(s) for sourcesofpaymentadmin.
  name: Loopay SourcesOfPaymentAdmin API
  slug: loopay-sourcesofpaymentadmin-api
- description: The User API from Loopay — 2 operation(s) for user.
  name: Loopay User API
  slug: loopay-user-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: loopay-api Affiliate API
  slug: open-loopay-affiliate-api
- collection_type: open
  name: loopay-api Affiliate Bank API
  slug: open-loopay-bank-api
- collection_type: open
  name: loopay-api Affiliate Company API
  slug: open-loopay-company-api
- collection_type: open
  name: loopay-api Affiliate CompanyProduct API
  slug: open-loopay-companyproduct-api
- collection_type: open
  name: loopay-api Affiliate Country API
  slug: open-loopay-country-api
- collection_type: open
  name: loopay-api Affiliate Currency API
  slug: open-loopay-currency-api
- collection_type: open
  name: loopay-api Affiliate DocumentType API
  slug: open-loopay-documenttype-api
- collection_type: open
  name: loopay-api Affiliate Movements API
  slug: open-loopay-movements-api
- collection_type: open
  name: loopay-api Affiliate PaidMethods API
  slug: open-loopay-paidmethods-api
- collection_type: open
  name: loopay-api Affiliate PayIn API
  slug: open-loopay-payin-api
- collection_type: open
  name: loopay-api Affiliate Payout API
  slug: open-loopay-payout-api
- collection_type: open
  name: loopay-api Affiliate PhysicalPoint API
  slug: open-loopay-physicalpoint-api
- collection_type: open
  name: loopay-api Affiliate SourcesOfPayment API
  slug: open-loopay-sourcesofpayment-api
- collection_type: open
  name: loopay-api Affiliate SourcesOfPaymentAdmin API
  slug: open-loopay-sourcesofpaymentadmin-api
- collection_type: open
  name: loopay-api Affiliate User API
  slug: open-loopay-user-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.loopay.com/explorer
- group: docs
  title: ''
  type: Documentation
  url: https://api.loopay.com/explorer
- group: docs
  title: ''
  type: APIReference
  url: https://api.loopay.com/explorer
- group: auth
  title: ''
  type: Authentication
  url: authentication/loopay-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loopay-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loopay-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/loopay-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loopay-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/loopay-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loopay-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loopay-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/loopay-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/loopay-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loopay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loopay-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://loopay.com/blog-fintech-pagos-latinoamerica/
- group: operate
  title: ''
  type: Support
  url: https://loopay.com/contacto/
- group: start
  title: ''
  type: SignUp
  url: https://app.loopay.com/
- group: start
  title: ''
  type: Login
  url: https://app.loopay.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loopay.com/terminos-y-condiciones/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://loopay.com/politica-de-seguridad/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/somosloopay/
- group: company
  title: ''
  type: Website
  url: https://loopay.com
created: '2026-07-17'
description: Loopay is a Latin American B2B fintech infrastructure company headquartered in Bogotá, Colombia and backed by 500 Global. It provides cross-border and local business payments, international collections, mass payouts, multi-currency Banking-as-a-Service accounts, automated bank reconciliation, and treasury management for companies operating across Colombia, Peru, Mexico, and Ecuador. Loopay exposes a token-authenticated REST API (OpenAPI 3.0, 31 operations) that lets platforms create and track payouts, manage sources of payment and pay-ins, group affiliates, and read balances and ledger movements — settling supplier and beneficiary payments in under 24 hours.
image: https://loopay.com/wp-content/uploads/2023/09/Loopay-web-imgs-24-150x139.png
layout: provider
mcp_servers:
- description: ''
  name: loopay-mcp.yml
  slug: loopay-mcpyml
modified: '2026-07-20'
name: Loopay
nav: Providers
network: true
overview: 'Loopay publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Affiliate API, Bank API, Company API, and 12 more. Tagged areas include Company, Payments, Fintech, Banking as a Service, and Cross-Border Payments.


  Loopay''s developer surface includes documentation, API reference, authentication, sandbox, engineering blog, support, signup flow, and 17 more developer resources.'
random_paper: 9
score:
  band: thin
  composite: 36.5
  delta: -1.3
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 16.7
    contract_quality: 47.8
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loopay/refs/heads/main/screenshots/loopay-2026-07-25T225527.png
security:
- kind: authentication
  name: Loopay Authentication
  slug: loopay-authentication
  summary_line: token · 1 scheme
- kind: domain-security
  name: Loopay Domain Security
  slug: loopay-domain-security
  summary_line: TLSv1.3
slug: loopay
tags:
- Company
- Payments
- Fintech
- Banking as a Service
- Cross-Border Payments
- Payouts
- Treasury
- Latin America
website: https://loopay.com
---
