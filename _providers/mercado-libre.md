---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 3
apis:
- description: Core REST API for the Mercado Libre marketplace covering items, categories, search, orders, questions, messages, users, sites, currencies, and shipping. Auth via OAuth 2.0 (authorization code).
  name: Mercado Libre Platform API
  slug: platform
- description: Mercado Pago payments REST API for checkout, payments, subscriptions, refunds, chargebacks, and merchant accounts across Latin America. OAuth 2.0 + access token authentication.
  name: Mercado Pago API
  slug: mercado-pago
- description: Mercado Envios shipping APIs covering shipment creation, tracking, labels, pickup, and logistics integrations for sellers.
  name: Mercado Envios API
  slug: shipping
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercado-libre-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mercadolibre
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercadolibre
- group: company
  title: ''
  type: Website
  url: https://www.mercadolibre.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.mercadolibre.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/mercado-libre-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mercado-libre-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mercado-libre-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.mercadolibre.com/llms.txt
created: '2026-05-08'
description: Mercado Libre is the largest e-commerce marketplace in Latin America with adjacent fintech (Mercado Pago), logistics (Mercado Envios), and ads businesses. The developer platform exposes REST APIs for items, orders, shipments, users, payments, and seller tooling.
finops:
- name: Mercado Libre Finops
  service_category: E-Commerce
  slug: mercado-libre-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercado-libre.png
layout: provider
modified: '2026-05-08'
name: Mercado Libre
nav: Providers
network: true
overview: Mercado Libre publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include E-Commerce, Marketplace, Latin America, Payments, and Mercado Pago.
plans:
- name: Mercado Libre Plans Pricing
  plan_count: 2
  slug: mercado-libre-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Mercado Libre Rate Limits
  slug: mercado-libre-rate-limits
score:
  band: minimal
  composite: 8.0
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mercado-libre/refs/heads/main/screenshots/mercado-libre-2026-06-20T185150.png
security:
- kind: domain-security
  name: Mercado Libre Domain Security
  slug: mercado-libre-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mercado-libre
tags:
- E-Commerce
- Marketplace
- Latin America
- Payments
- Mercado Pago
- Logistics
- Shipping
website: https://www.mercadolibre.com/
---
