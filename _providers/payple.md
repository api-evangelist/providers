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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Payple REST payment API (v2) for card, bank-account, recurring/billing-key, link, verification, and payout (Hub) operations, plus the hosted payment window.
  name: Payple Payment API
  slug: payple-payment-api
artifact_total: 4
asyncapis:
- description: ''
  name: Payple Webhooks
  slug: payple-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://payple.kr
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.payple.kr
- group: docs
  title: ''
  type: Documentation
  url: https://developer.payple.kr
- group: docs
  title: ''
  type: APIReference
  url: https://developer.payple.kr/parameters/domestic-card/app
- group: operate
  title: ''
  type: Support
  url: https://developer.payple.kr/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PAYPLECORP
- group: company
  title: ''
  type: Blog
  url: https://github.com/PAYPLECORP/Blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/PAYPLECORP/policies
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://github.com/PAYPLECORP/policies
- group: start
  title: ''
  type: Login
  url: https://accounts.payple.kr
- group: build
  title: ''
  type: Packages
  url: packages/payple-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/payple-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payple-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/payple-response-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/payple-decline-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/payple-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/payple-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/payple-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/payple-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payple-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/payple-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/payple-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/payple-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payple-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payple-llms.txt
created: '2026-07-17'
description: Payple (페이플) is a South Korean payment gateway (PG) and fintech provider that lets merchants accept online payments across domestic and international cards, real-time bank-account payments, recurring / billing-key charges, link payments, identity verification, and settlement / payout (Hub) services. Integration is offered through a hosted payment window initialized in the browser with a public client key, plus a server-side REST API (v2) authorized with partner credentials (PCD_CST_ID / PCD_CUST_KEY). Payple is a registered Korean electronic financial business with an Innovative Financial Service (혁신금융서비스) designation, and it publishes official language sample source, policy documents, and a developer center. This profile was enriched by the API Evangelist pipeline from the Payple developer center and the PAYPLECORP GitHub organization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payple.png
layout: provider
modified: '2026-07-20'
name: Payple
nav: Providers
network: true
overview: 'Payple publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Gateway, Fintech, and Korea.


  The Payple catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Payple''s developer surface includes documentation, API reference, support, engineering blog, authentication, sandbox, and 19 more developer resources.'
random_paper: 77
score:
  band: developing
  composite: 43.6
  delta: 3.3
  facets:
    commercial_clarity: 42.1
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 13.2
  previous_composite: 40.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Payple Authentication
  slug: payple-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Payple Domain Security
  slug: payple-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payple
tags:
- Company
- Payments
- Payment Gateway
- Fintech
- Korea
- Recurring Payments
- Billing
- Cards
- Bank Transfer
website: https://payple.kr
---
