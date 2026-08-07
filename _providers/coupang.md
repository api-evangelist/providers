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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Coupang Open API is a RESTful seller (vendor) API for managing the full marketplace lifecycle including product catalog creation, order processing, return and cancellation handling, settlement que
  name: Coupang Open API
  slug: coupang-open-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coupang-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coupang-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coupang
- group: company
  title: ''
  type: Website
  url: https://www.coupang.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.coupangcorp.com/
- group: start
  title: ''
  type: SellerPortal
  url: https://wing.coupang.com/
- group: company
  title: ''
  type: About
  url: https://www.aboutcoupang.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coupang.com/np/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coupang.com/np/policies/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coupang
created: '2024-01-01'
description: Coupang is a South Korean e-commerce company offering rapid delivery of a wide range of products including groceries, electronics, fashion, and household goods through its mobile app and website. Coupang exposes an Open API platform for marketplace sellers (vendors) to integrate product catalog, order, return, cancellation, settlement, and inquiry workflows.
finops:
- name: Coupang Finops
  service_category: API
  slug: coupang-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coupang.png
layout: provider
modified: '2026-04-28'
name: Coupang
nav: Providers
network: true
overview: Coupang publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cancellations, E-commerce, Korea, Marketplace, and Open API.
plans:
- name: Coupang Plans Pricing
  plan_count: 3
  slug: coupang-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 5
  name: Coupang Rate Limits
  slug: coupang-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coupang/refs/heads/main/screenshots/coupang-2026-06-20T175107.png
security:
- kind: domain-security
  name: Coupang Domain Security
  slug: coupang-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coupang Vulnerability Disclosure
  slug: coupang-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coupang
tags:
- Cancellations
- E-commerce
- Korea
- Marketplace
- Open API
- Orders
- Products
- Returns
- Sellers
- Settlement
- Vendors
website: https://www.coupang.com
---
