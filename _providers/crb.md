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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The Cross River Operating System (COS) API is Cross River's API-driven bank core, exposing Accounts and Payments products (ACH, RTP, FedNow, wires, international payments, cards, subledgers, and lendi
  name: Cross River Operating System (COS) API
  slug: cross-river-operating-system-cos-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crossriver.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.crossriver.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crossriver.com/concepts
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crossriver.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crossriver.com/get-started/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/crb-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/crb-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.crossriver.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/crb-changelog.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.crossriver.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.crossriver.com/insights
- group: start
  title: ''
  type: SignUp
  url: https://crossriver.service-now.com/csm?id=cos_sandbox_request_form
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crossriver.com/legal/privacy-policy
- group: design
  title: ''
  type: Conventions
  url: conventions/crb-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crb-llms.txt
created: '2026-07-17'
description: CRB (Cross River Bank) is a New Jersey-chartered, FDIC-insured bank and financial technology infrastructure provider founded in 2008 and headquartered in Fort Lee, New Jersey. Cross River pairs a regulated bank with an API-driven core it calls the Cross River Operating System (COS), letting fintech companies, neobanks, lenders, and platforms embed banking, payments, cards, and lending products directly into their applications. Its developer platform exposes Accounts and Payments APIs spanning ACH, RTP, FedNow, wires, international payments, push-to-card, card issuing and processing, subledgers, lending origination, and onchain/stablecoin rails, secured with OAuth2 client credentials and delivered with an isolated sandbox, Postman collection, webhooks, and a dated changelog. Cross River is known for powering leading fintech partners including Stripe, Coinbase, Affirm, Upgrade, and Intuit, and was surfaced in the API Evangelist network as a Battery Ventures portfolio company.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crb.png
layout: provider
modified: '2026-07-18'
name: CRB
nav: Providers
network: true
overview: 'CRB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Banking as a Service, Embedded Finance, and Payments.


  CRB''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, changelog, support, and 9 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 25.3
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 25.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 25.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crb/refs/heads/main/screenshots/crb-2026-07-25T210659.png
security:
- kind: authentication
  name: Crb Authentication
  slug: crb-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Crb Domain Security
  slug: crb-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: crb
tags:
- Company
- Banking
- Banking as a Service
- Embedded Finance
- Payments
- Fintech
- Lending
- Cards
- ACH
website: https://www.crossriver.com/
---
