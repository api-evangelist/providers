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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Astra's REST API (v1) for embedding instant money movement — accounts, users, cards, transfers, payment instruments, and Routines — authorized via OAuth 2.0 and delivered with webhooks for asynchronou
  name: Astra API
  slug: astra-api
artifact_total: 5
asyncapis:
- description: ''
  name: Astra Webhooks
  slug: astra-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astra-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.astra.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.astra.finance/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.astra.finance/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.astra.finance/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://astrafi.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://dashboard-sandbox.astra.finance/support
- group: start
  title: ''
  type: SignUp
  url: https://dashboard-sandbox.astra.finance/login
- group: start
  title: ''
  type: Login
  url: https://dashboard.astra.finance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astrafi.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astrafi.com/privacy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.astrafi.com/
- group: auth
  title: ''
  type: Compliance
  url: https://astrafi.com/security-and-privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astra-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/astra-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/astra-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/astra-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/astra-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/astra-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/astra-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/astra-conformance.yml
created: '2026-07-17'
description: Astra (Astra Finance, Inc.) is a financial technology company providing an all-in-one instant payments API that lets product teams embed real-time money movement between bank accounts and debit cards. The platform powers instant disbursements and payouts, instant account funding, accelerated bank transfers, card-to-account movement, cross-border payments, and automated "Routines," with built-in compliance, fraud detection, and chargeback management. Developers integrate over a versioned REST API (v1) using OAuth 2.0 authorization for end-user money movement plus client-credential authorization for administrative operations, with webhooks for asynchronous updates and a full sandbox environment for testing.
image: https://astrafi.com/static/images/favicons/apple-touch-icon.png
layout: provider
modified: '2026-07-18'
name: Astra
nav: Providers
network: true
overview: 'Astra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Money Movement, and ACH.


  The Astra catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Astra''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 14 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 40.7
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 40.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astra/refs/heads/main/screenshots/astra-2026-07-25T201458.png
security:
- kind: authentication
  name: Astra Authentication
  slug: astra-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Astra Domain Security
  slug: astra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Astra Trust Center
  slug: astra-trust-center
  summary_line: SOC 2, PCI DSS, GDPR, CCPA/CPRA
slug: astra
tags:
- Company
- Payments
- Fintech
- Money Movement
- ACH
- Instant Payments
- Bank Transfers
- Disbursements
website: https://docs.astra.finance/
---
