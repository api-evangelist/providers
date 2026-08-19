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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'Compliant, real-time cross-border payments and USD account infrastructure: beneficiaries and KYC/KYB, USD and multi-currency virtual accounts, transaction/payment simulation and execution, batch and s'
  name: Caliza Core API
  slug: caliza-core-api
artifact_total: 7
asyncapis:
- description: ''
  name: Caliza Webhooks
  slug: caliza-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.caliza.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.caliza.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.caliza.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.caliza.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.caliza.com/docs/authenticate
- group: company
  title: ''
  type: Blog
  url: https://www.caliza.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.caliza.com/faq
- group: start
  title: ''
  type: SignUp
  url: https://www.caliza.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.caliza.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.caliza.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdn.prod.website-files.com/677ed676bd7257ea423799b4/69177a9c7494e512590531d7_Caliza%20US%20Website%20Terms%20-%2007.17.2025.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/677ed676bd7257ea423799b4/698a6522f0a64bd8dedb0942_Caliza%20US%20Privacy%20Policy%20-%20Final%2002.06.2026.docx.pdf
- group: auth
  title: ''
  type: Authentication
  url: authentication/caliza-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/caliza-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/caliza-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caliza-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caliza-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caliza-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/caliza-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/caliza-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/caliza-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caliza-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/caliza-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caliza-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/caliza-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Caliza is a financial infrastructure company providing compliant, real-time cross-border payments and USD account infrastructure for global businesses. The Caliza Core API lets integrators create individual and business beneficiaries (with KYC/KYB verification), issue named USD digital-dollar and multi-currency virtual accounts, simulate and execute transactions and payments across fiat and stablecoin rails (ACH, WIRE, SWIFT, RTP, PIX, SPEI, and blockchain networks including Ethereum, Polygon, Tron, Stellar, Base and Solana), run batch and sweep payouts, lock FX rates, manage recipients, and receive HMAC-signed webhook notifications for the full transaction and beneficiary lifecycle. Authentication is OAuth 2.0 (OpenID Connect / Keycloak) and a full sandbox environment with mock deposit simulators is provided. Caliza is backed by Initialized Capital and QED Investors.
image: https://cdn.prod.website-files.com/677ed676bd7257ea423799b4/6787817b276b304d33d8dd2f_caliza-logo.png
layout: provider
mcp_servers:
- description: ''
  name: caliza-mcp.yml
  slug: caliza-mcpyml
modified: '2026-07-18'
name: Caliza
nav: Providers
network: true
overview: 'Caliza publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Cross-Border Payments, and Stablecoins.


  The Caliza catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Caliza''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 32
scopes:
- name: Caliza Scopes
  scope_count: 10
  slug: caliza-scopes
  summary_line: 10 scopes · password
score:
  band: developing
  composite: 48.2
  delta: -1.2
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 53.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 19.7
  previous_composite: 49.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/caliza/refs/heads/main/screenshots/caliza-2026-07-25T204235.png
security:
- kind: authentication
  name: Caliza Authentication
  slug: caliza-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Caliza Domain Security
  slug: caliza-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Caliza Trust Center
  slug: caliza-trust-center
  summary_line: trust center published
slug: caliza
tags:
- Company
- Fintech
- Payments
- Cross-Border Payments
- Stablecoins
- Remittances
- Foreign Exchange
- Virtual Accounts
- Payouts
- KYC
- Latin America
website: https://www.caliza.com/
---
