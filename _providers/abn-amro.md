---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Tikkie API lets Tikkie Business customers programmatically create payment requests, send them to end-payers, and receive notifications when payments complete. Authentication uses an API token (Bus
  name: Tikkie API
  slug: tikkie
- description: PSD2-compliant Payment Initiation Service (PIS) API allowing licensed Third Party Providers (TPPs) to initiate SEPA payments from an ABN AMRO retail or business customer account and retrieve status. R
  name: Payment Initiation (PSD2) API
  slug: payment-initiation-psd2
- description: Corporate / business-account payment API used by ABN AMRO commercial customers to initiate payments from their own corporate accounts and retrieve transaction status. Uses OAuth 2.0 client-credentials
  name: Business Account Payment API
  slug: business-account-payment
artifact_total: 21
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/abn-amro-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abn-amro-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ABNAMRO
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abn-amro
- group: company
  title: ''
  type: Website
  url: https://www.abnamro.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.abnamro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.abnamro.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.abnamro.com/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.abnamro.com/content/terms-and-conditions
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: A Dutch banking and financial services group serving retail, private, and corporate clients across Europe. ABN AMRO publishes a public developer portal exposing PSD2 Open Banking, Tikkie payment-request, and corporate payment APIs.
features:
- description: Create Tikkie payment requests and receive callbacks when an end-payer settles them.
  name: Payment Requests
- description: Initiate SEPA Credit Transfer and SEPA Instant payments under PSD2 PIS for both retail and business accounts.
  name: PSD2 Payment Initiation
- description: Submit own-account corporate payments and retrieve detailed transaction status.
  name: Corporate Payments
- description: Authorization Code (with PKCE) and Client Credentials flows for licensed TPPs and direct business clients.
  name: OAuth 2.0 Authorization
- description: PSD2 production access uses qualified eIDAS certificates (QWAC + QSeal) for transport and signing.
  name: eIDAS Certificate Onboarding
- description: Public sandbox with test certificates and synthetic accounts for all PSD2 and business-payment APIs.
  name: Sandbox
finops:
- name: Abn Amro Finops
  service_category: Financial Services / Open Banking
  slug: abn-amro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abn-amro.png
integrations:
- description: ABN AMRO subsidiary providing the Tikkie consumer and business payment-request product.
  name: Tikkie
- description: Common European PSD2 specification used by ABN AMRO and most Dutch and German banks.
  name: Berlin Group XS2A
- description: PSD2 aggregators (e.g., Tink, TrueLayer, Plaid Europe) connect to ABN AMRO via the PSD2 endpoints.
  name: Open Banking Aggregators
layout: provider
modified: '2026-05-16'
name: ABN AMRO
nav: Providers
network: true
overview: 'ABN AMRO publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Banks, European Banking, Open Banking, and PSD2.


  ABN AMRO''s developer surface includes developer portal, documentation, getting-started guide, authentication, and 5 more developer resources.'
plans:
- name: Abn Amro Plans Pricing
  plan_count: 3
  slug: abn-amro-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 2
  name: Abn Amro Rate Limits
  slug: abn-amro-rate-limits
score:
  band: thin
  composite: 30.0
  delta: -5.6
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 34.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/abn-amro/refs/heads/main/screenshots/abn-amro-2026-06-20T163250.png
security:
- kind: domain-security
  name: Abn Amro Domain Security
  slug: abn-amro-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Abn Amro Vulnerability Disclosure
  slug: abn-amro-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: abn-amro
tags:
- Financial
- Banks
- European Banking
- Open Banking
- PSD2
- Payments
use_cases:
- description: Use Tikkie to send a one-off or recurring payment request to a customer over a link instead of card-present checkout.
  name: Merchant Payment Collection
- description: Use PSD2 Payment Initiation as a low-cost alternative to card rails for e-commerce checkout in the Netherlands and EU.
  name: Account-to-Account Checkout
- description: Automate payroll, supplier payments, and treasury transfers from ABN AMRO business accounts.
  name: Corporate Treasury Automation
- description: PSD2 TPPs (PISP role) routing customer-authorized payments through ABN AMRO as one of the Dutch banks they cover.
  name: TPP Aggregation
website: https://www.abnamro.com/
---
