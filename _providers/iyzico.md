---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for accepting card payments (NON-3DS and 3D Secure), hosted CheckoutForm and Pay with iyzico flows, iyzico Link, subscriptions, marketplace submerchant payments and payouts, card storage/toke
  name: iyzico Payment API
  slug: iyzico-payment-api
artifact_total: 6
asyncapis:
- description: ''
  name: Iyzico Webhooks
  slug: iyzico-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iyzico.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iyzico.com/en/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.iyzico.com/en/getting-started/preliminaries/api-reference-beta
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iyzico.com/en/getting-started/welcome
- group: company
  title: ''
  type: Website
  url: https://www.iyzico.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.iyzico.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://www.iyzico.com/en/support/help-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.iyzico.com/en/support/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iyzico
- group: start
  title: ''
  type: SignUp
  url: https://merchant.iyzipay.com/auth/register
- group: start
  title: ''
  type: Login
  url: https://merchant.iyzipay.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iyzico.com/en/general-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iyzico.com/en/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/iyzico/iyzico/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://iyzico.statuspage.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iyzico-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/iyzico-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/iyzico-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iyzico-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/iyzico-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iyzico-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/iyzico-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/iyzico-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/iyzico-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iyzico-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/iyzico-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iyzico-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iyzico-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/iyzico-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/iyzico-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iyzico-domain-security.yml
created: '2026-07-17'
description: iyzico is a Turkish payment service provider (part of PayU / Prosus) that gives online businesses a single API and hosted payment surface to accept cards and alternative payment methods across Turkey and cross-border. Its developer platform (docs.iyzico.com, api.iyzipay.com) covers NON-3DS and 3D Secure card payments, the hosted CheckoutForm and Pay with iyzico flows, iyzico Link, subscriptions/recurring billing, a marketplace/submerchant model with payouts, card storage/tokenization, installment and BIN services, reporting, and server-to-server webhooks. Authentication uses an HMACSHA256-signed IYZWSv2 scheme with an apiKey/secretKey pair, and a full sandbox (sandbox-api.iyzipay.com) with published test cards mirrors production. First party SDKs are published for PHP, Python, Node.js, Java, Ruby and .NET plus e-commerce plugins (WooCommerce, Magento 2, PrestaShop, OpenCart).
image: https://www.iyzico.com/en/
layout: provider
mcp_servers:
- description: ''
  name: iyzico-mcp.yml
  slug: iyzico-mcpyml
modified: '2026-07-19'
name: Iyzico
nav: Providers
network: true
overview: 'Iyzico publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, FinTech, Payment Gateway, and Card Payments.


  The Iyzico catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Iyzico''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 24 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 0
  name: Iyzico Rate Limits
  slug: iyzico-rate-limits
score:
  band: developing
  composite: 47.1
  delta: 3.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 71.7
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 36.8
  previous_composite: 44.0
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
screenshot: https://raw.githubusercontent.com/api-evangelist/iyzico/refs/heads/main/screenshots/iyzico-2026-07-25T223026.png
security:
- kind: authentication
  name: Iyzico Authentication
  slug: iyzico-authentication
  summary_line: custom-hmac · 1 scheme
- kind: domain-security
  name: Iyzico Domain Security
  slug: iyzico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iyzico
tags:
- Company
- Payments
- FinTech
- Payment Gateway
- Card Payments
- Checkout
- Subscriptions
- Marketplace
- Turkey
- 3D Secure
website: https://www.iyzico.com/en/
---
