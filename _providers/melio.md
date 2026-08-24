---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'REST API for managing bills, vendors, payment methods, and scheduling payments. Supports ACH transfers, check payments, wire transfers, and international payments. Includes webhook support, a sandbox '
  name: Melio Payments API
  slug: melio-payments-api
artifact_total: 7
common:
- group: other
  title: ''
  type: OpenIDConnect
  url: https://meliopayments.com/.well-known/oauth-authorization-server
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/melio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/melio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meliopayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://meliopayments.com/partners/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/melio-payments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meliopayments/
- group: company
  title: ''
  type: Blog
  url: https://meliopayments.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://meliopayments.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://meliopayments.com/security/
- group: other
  title: ''
  type: X
  url: https://x.com/MelioPayments
- group: commercial
  title: ''
  type: Plans
  url: plans/melio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/melio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/melio-finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meliopayments.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meliopayments.com/legal/privacy-policy
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.melio.com/hc/en-us
created: '2026-06-13'
description: Melio is a B2B payments platform for small businesses that provides a REST API for managing bills, vendors, payment methods, scheduling payments, and syncing with accounting software including QuickBooks, Xero, and NetSuite. Melio enables software companies to embed bill pay, vendor payments, and invoicing directly inside their products with ACH and card options. Founded in 2018, Melio has processed over $100B in payments for 100,000+ business users and 2M+ vendors.
finops:
- name: Melio Finops
  service_category: ''
  slug: melio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/melio.png
jsonld:
- class_count: 19
  name: Melio Context
  property_count: 1
  slug: melio-context
layout: provider
modified: '2026-06-13'
name: Melio
nav: Providers
network: true
overview: 'Melio publishes 1 API on the [APIs.io](https://apis.io/) network: Payments API. Tagged areas include B2B Payments, Accounts Payable, Accounts Receivable, Bill Pay, and Vendor Payments.


  The Melio catalog on APIs.io includes 1 JSON-LD context.


  Melio''s developer surface includes documentation, engineering blog, pricing, and 14 more developer resources.'
plans:
- name: Melio Plans Pricing
  plan_count: 5
  slug: melio-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Melio Rate Limits
  slug: melio-rate-limits
score:
  band: developing
  composite: 40.1
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 39.4
    developer_ergonomics: 16.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/melio/refs/heads/main/screenshots/melio-2026-06-20T185133.png
security:
- kind: domain-security
  name: Melio Domain Security
  slug: melio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Melio Vulnerability Disclosure
  slug: melio-vulnerability-disclosure
  summary_line: disclosure policy published
slug: melio
tags:
- B2B Payments
- Accounts Payable
- Accounts Receivable
- Bill Pay
- Vendor Payments
- ACH
- Fintech
- Small Business
- Embedded Finance
- Payment Processing
website: https://meliopayments.com/
---
