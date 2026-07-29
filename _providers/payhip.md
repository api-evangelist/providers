---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Payhip Agentic Access
  operation_count: 8
  slug: payhip-agentic-access
  summary_line: 8 operations · 5 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Create, list, and retrieve discount coupons.
  name: Payhip Coupons API
  slug: payhip-coupons-api
- description: Verify and manage software license keys issued for Payhip products.
  name: Payhip License Keys API
  slug: payhip-license-keys-api
artifact_total: 9
collections:
- collection_type: open
  name: Payhip API
  slug: open-payhip
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/payhip-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payhip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/payhip-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/payhip
- group: company
  title: ''
  type: Website
  url: https://payhip.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.payhip.com/category/48-developer
- group: docs
  title: ''
  type: APIReference
  url: https://payhip.com/api-reference
- group: commercial
  title: ''
  type: Plans
  url: plans/payhip-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/payhip-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/payhip-finops.yml
created: '2026-07-05'
description: Payhip is an all-in-one e-commerce platform that lets creators sell digital downloads, online courses, memberships, coupons, and physical products directly to their audience, with hosted storefronts and checkout. Its public REST API (base https://payhip.com/api/v2) currently exposes programmatic management of Coupons and verification/management of software License Keys, authenticated with an API key or a per-product secret key. Order, customer, and transaction data is delivered to applications through signed webhooks (paid, refunded, subscription.created, subscription.deleted) rather than through pollable REST resources.
finops:
- name: Payhip Finops
  service_category: E-commerce Platform
  slug: payhip-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/payhip.png
layout: provider
modified: '2026-07-05'
name: Payhip
nav: Providers
network: true
overview: 'Payhip publishes 2 APIs on the [APIs.io](https://apis.io/) network: Coupons API and License Keys API. Tagged areas include E-commerce, Digital Products, Memberships, Creators, and Coupons.


  Payhip''s developer surface includes authentication, documentation, API reference, and 7 more developer resources.'
plans:
- name: Payhip Plans Pricing
  plan_count: 3
  slug: payhip-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Payhip Rate Limits
  slug: payhip-rate-limits
score:
  band: thin
  composite: 35.3
  delta: -2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.9
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Payhip Authentication
  slug: payhip-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Payhip Domain Security
  slug: payhip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payhip
tags:
- E-commerce
- Digital Products
- Memberships
- Creators
- Coupons
- License Keys
- Webhooks
- Payments
website: https://payhip.com
---
