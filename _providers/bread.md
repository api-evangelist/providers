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
api_count: 2
apis:
- description: The Bread Pay API enables merchants to integrate installment financing options into online and in-store checkout flows. Supports creating financing applications, retrieving loan statuses, managing tra
  name: Bread Pay API
  slug: bread-pay-api
- description: SplitPay is a short-term financing alternative for retail merchants, enabling customers to split purchases into manageable payments and helping retailers attract price-sensitive customers while increa
  name: Bread SplitPay API
  slug: split-pay-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bread-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getbread
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bread-financial
- group: company
  title: ''
  type: Website
  url: https://www.breadfinancial.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.breadfinancial.com/
- group: other
  title: ''
  type: BusinessSolutions
  url: https://www.breadfinancial.com/en/business-solutions.html
created: '2024-11-14'
description: Bread Financial is a technology-driven financial services company offering white-label buy now pay later (BNPL), installment financing, and branded credit card products for merchants. The platform processes $27 billion in annual sales volume for 35.6 million active customers. Bread Pay enables merchants to embed financing options directly into their checkout flow for both online and in-store purchases, including installment plans (Bread Pay) and short-term split payment options (SplitPay).
finops:
- name: Bread Finops
  service_category: API
  slug: bread-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bread.png
layout: provider
modified: '2026-04-21'
name: Bread Financial
nav: Providers
network: true
overview: 'Bread Financial publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Buy Now Pay Later, BNPL, Financing, Payments, and Credit.


  Bread Financial''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Bread Plans Pricing
  plan_count: 3
  slug: bread-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 5
  name: Bread Rate Limits
  slug: bread-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: -2.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 21.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bread/refs/heads/main/screenshots/bread-2026-07-25T203737.png
security:
- kind: domain-security
  name: Bread Domain Security
  slug: bread-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bread
tags:
- Buy Now Pay Later
- BNPL
- Financing
- Payments
- Credit
- Retail Finance
website: https://www.breadfinancial.com
---
