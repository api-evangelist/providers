---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 3.2
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The Stone Online transactional API for authorizing, capturing, canceling, and querying payment transactions for online and physical sales platforms. Supports credit card, debit, and voucher payments w
  name: Stone Online API
  slug: stone-online-api
- description: 'Stone''s open banking REST API providing digital account management, internal and external transfers, Pix instant payments, boleto issuance, payment links, QR code generation, contacts, receipts, KYC, '
  name: Stone OpenBank API
  slug: stone-openbank-api
- description: API for connecting point-of-sale systems to Stone payment terminals (maquininhas), enabling merchants to integrate physical payment acceptance into their business software.
  name: Stone Connect API
  slug: stone-connect-api
- description: Backoffice API for monitoring sales, installments, cancellations, and financial reconciliation data for Stone merchants.
  name: Stone Conciliation API
  slug: stone-conciliation-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stone-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stone.com.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openbank.stone.com.br/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/stone-payments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stone-co
- group: company
  title: ''
  type: Blog
  url: https://conteudo.stone.com.br/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stone.com.br/devcenter
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.openbank.stone.com.br
- group: other
  title: ''
  type: X
  url: https://x.com/sejastone
- group: commercial
  title: ''
  type: Plans
  url: plans/stone-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stone-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stone-finops.yml
created: '2026-06-13'
description: Stone is a Brazilian financial technology company offering REST APIs for payment processing, Pix instant payments, digital banking accounts, boleto issuance, credit products, payment links, and stone-terminal management for merchants. Their platform enables businesses to authorize, capture, cancel, and query transactions across online and physical sales channels.
finops:
- name: Stone Finops
  service_category: ''
  slug: stone-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stone.png
jsonld:
- class_count: 0
  name: Stone Context
  property_count: 0
  slug: stone
layout: provider
modified: '2026-06-13'
name: Stone
nav: Providers
network: true
overview: 'Stone publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Fintech, Pix, Brazil, and Digital Banking.


  The Stone catalog on APIs.io includes 1 JSON-LD context.


  Stone''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Stone Plans Pricing
  plan_count: 3
  slug: stone-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Stone Rate Limits
  slug: stone-rate-limits
score:
  band: emerging
  composite: 23.3
  delta: -3.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stone/refs/heads/main/screenshots/stone-2026-06-20T194556.png
security:
- kind: domain-security
  name: Stone Domain Security
  slug: stone-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stone
tags:
- Payments
- Fintech
- Pix
- Brazil
- Digital Banking
- Payment Processing
- Boleto
- Financial Technology
website: https://www.stone.com.br
---
