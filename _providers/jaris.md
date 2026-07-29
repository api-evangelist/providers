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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://jaris.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://jaris.io/developer-overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.jaris.com
- group: start
  title: ''
  type: GettingStarted
  url: https://jaris.io/developer-overview
- group: start
  title: ''
  type: Login
  url: https://partner.jaris.com/
- group: company
  title: ''
  type: Blog
  url: https://jaris.io/news/
- group: operate
  title: ''
  type: Support
  url: https://jaris.io/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://jaris.io/platform/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jaris.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jaris.io/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jaris.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.jaris.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/jaris-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jaris-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jaris-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jaris-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jaris-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jaris-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jaris-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://jaris.io/.well-known/security.txt
created: '2026-07-17'
description: Jaris is an embedded-finance infrastructure company that lets payment processors, ISOs, payment service providers, and SaaS platforms embed and launch a suite of financial products through a single integration. Jaris is not a bank; deposits are held and loans are issued through First Internet Bank of Indiana (FDIC member). Its three integrated offerings are Business Loans with same-day funding, Instant Payouts giving merchants early access to earned revenue, and Banking Services (deposit accounts). Supporting capabilities include intelligent merchant onboarding with automated KYB/KYC, managed settlements with real-time control across payment processors, and white-labeled embeddable UI components (Jaris Connect / Jaris UI). Developers integrate via an API-key model generated in the Jaris Dashboard, embedding a brandable UI in a few lines of JavaScript. The public developer reference is hosted on a password-gated ReadMe portal, so no machine-readable OpenAPI is available.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jaris.png
layout: provider
modified: '2026-07-19'
name: Jaris
nav: Providers
network: true
overview: 'Jaris is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Embedded Finance, Fintech, Payments, and Lending.


  Jaris'' developer surface includes documentation, getting-started guide, engineering blog, support, pricing, authentication, and 14 more developer resources.'
random_paper: 75
score:
  band: thin
  composite: 32.7
  delta: -2.8
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jaris/refs/heads/main/screenshots/jaris-2026-07-25T223054.png
security:
- kind: authentication
  name: Jaris Authentication
  slug: jaris-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Jaris Domain Security
  slug: jaris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jaris Vulnerability Disclosure
  slug: jaris-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jaris Trust Center
  slug: jaris-trust-center
  summary_line: trust center published
slug: jaris
tags:
- Company
- Embedded Finance
- Fintech
- Payments
- Lending
- Banking as a Service
- Instant Payouts
- Merchant Onboarding
- KYB
- Settlements
website: https://jaris.io/
---
