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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Merchant-facing payment API for GCash mini programs — cashier payment, payment inquiry, refund and refund inquiry, plus OAuth2 user authorization (authCode -> applyToken). Signed requests (Client-Id +
  name: GCash Mini Program Open API
  slug: gcash-mini-program-open-api
artifact_total: 6
asyncapis:
- description: ''
  name: Gcash Payments Webhooks
  slug: gcash-payments-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://new.gcash.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apiportal.gcash.com
- group: docs
  title: ''
  type: Documentation
  url: https://miniprogram.gcash.com/docs/miniprogram_gcash/mpdev/openapi_overview
- group: docs
  title: ''
  type: APIReference
  url: https://miniprogram.gcash.com/docs/miniprogram_gcash/mpdev/api_api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://miniprogram.gcash.com/docs/miniprogram_gcash/mpdev/developer-guide
- group: operate
  title: ''
  type: Support
  url: https://gcash.com/business/api-portal-faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gcash.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gcash.com/privacy-notice
- group: auth
  title: ''
  type: Authentication
  url: authentication/gcash-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gcash-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/gcash-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gcash-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/gcash-payments-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gcash-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gcash-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gcash-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gcash-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gcash-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gcash-security.txt
- group: auth
  title: ''
  type: Security
  url: https://gcash.com/vulnerability-disclosure-program/policy
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gcash-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gcash-domain-security.yml
created: '2026-07-17'
description: 'GCash (operated by Mynt / G-Xchange, Inc.) is the Philippines'' largest mobile wallet and e-money platform, offering payments, transfers, QR checkout, bills payment, savings, lending and insurance to tens of millions of users. For developers and businesses it exposes a partner-gated API surface: the GCash API Portal (discover and subscribe to API products such as In-Store QR, Webpay, GLife and Funds Disbursement) and the GCash Mini Program Open API, which lets merchants build in-app mini programs with cashier payments, refunds and user authorization. API requests are secured with per-request RSA256/ECC224 signatures plus an OAuth2 authorization-code user flow, with idempotent payment operations and asynchronous webhook notifications. This profile was seeded as a portfolio lead and enriched from GCash''s public developer documentation.'
image: https://logo.clearbit.com/gcash.com
layout: provider
mcp_servers:
- description: ''
  name: gcash-mcp.yml
  slug: gcash-mcpyml
modified: '2026-07-19'
name: GCash
nav: Providers
network: true
overview: 'GCash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Mobile Wallet, E-Money, and Fintech.


  The GCash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GCash''s developer surface includes documentation, API reference, getting-started guide, support, authentication, sandbox, and 16 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 40.9
  delta: 1.4
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 79.6
    governance: 3.1
    operational_transparency: 18.4
  previous_composite: 39.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gcash/refs/heads/main/screenshots/gcash-2026-07-25T215519.png
security:
- kind: authentication
  name: Gcash Authentication
  slug: gcash-authentication
  summary_line: signature/oauth2 · 3 schemes
- kind: domain-security
  name: Gcash Domain Security
  slug: gcash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gcash Vulnerability Disclosure
  slug: gcash-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gcash
tags:
- Company
- Payments
- Mobile Wallet
- E-Money
- Fintech
- Digital Payments
- Philippines
- QR Payments
website: https://new.gcash.com/
---
