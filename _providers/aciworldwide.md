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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: A single unified RESTful API for accepting and managing electronic payments — payments, checkouts, tokenization/registrations, back-office operations, 3-D Secure, risk/fraud, recurring payments, and w
  name: ACI Open Payment Platform (PAY.ON / OPPWA) REST API
  slug: aci-open-payment-platform-payon-oppwa-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Aciworldwide Webhooks
  slug: aciworldwide-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://aciworldwide.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aciww-production.apigee.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aciworldwide.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aciworldwide.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aciworldwide.com/tutorials
- group: operate
  title: ''
  type: Support
  url: https://www.aciworldwide.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.aciworldwide.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://aciww-production.apigee.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aciworldwide.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aciworldwide.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.aciworldwide.com/pci-dss-v4
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aciworldwide-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aciworldwide-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/aciworldwide-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/aciworldwide-result-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/aciworldwide-decline-codes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/aciworldwide-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/aciworldwide-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/aciworldwide-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aciworldwide-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/aciworldwide-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/aciworldwide-packages.yml
- group: design
  title: ''
  type: Components
  url: components/aciworldwide-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/aciworldwide-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/aciworldwide-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aciworldwide-llms.txt
created: '2026-07-17'
description: 'ACI Worldwide is a global real-time payments software company (NASDAQ: ACIW) whose Open Payment Platform — the PAY.ON / OPPWA gateway — exposes a single unified RESTful API for accepting and managing electronic payments worldwide. Merchants and payment intermediaries integrate card and alternative payment methods through server-to-server calls, the hosted COPYandPAY widget, mobile SDKs, and Pay by Link. The API covers payments, checkouts, tokenization and registrations, back-office capture/refund/reversal operations, 3-D Secure, fraud and risk management, recurring/scheduled payments, webhooks for transaction notifications, and reporting. Test transactions run against eu-test.oppwa.com and go live on eu-prod.oppwa.com. This profile was added to the API Evangelist network as a portfolio lead and enriched by the pipeline.'
image: https://www.aciworldwide.com/wp-content/uploads/2024/07/ACI-Worldwide-Blue-No-Tagline.png
layout: provider
modified: '2026-07-18'
name: Aciworldwide
nav: Providers
network: true
overview: 'Aciworldwide publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Gateway, Real-Time Payments, and eCommerce.


  The Aciworldwide catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aciworldwide''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
random_paper: 35
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 7.9
  previous_composite: 48.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aciworldwide/refs/heads/main/screenshots/aciworldwide-2026-07-25T181500.png
security:
- kind: authentication
  name: Aciworldwide Authentication
  slug: aciworldwide-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Aciworldwide Domain Security
  slug: aciworldwide-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Aciworldwide Trust Center
  slug: aciworldwide-trust-center
  summary_line: PCI DSS v4.0, SSAE 18 (SOC)
slug: aciworldwide
tags:
- Company
- Payments
- Payment Gateway
- Real-Time Payments
- eCommerce
- Fraud Management
- Tokenization
- Financial Services
website: https://aciworldwide.com
---
