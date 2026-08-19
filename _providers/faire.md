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
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: REST API for Faire brands to manage products, inventory, orders, shipments, and returns.
  name: Faire External API v2 (Brand)
  slug: external-api-v2-brand
- description: REST API endpoints for retailers to browse products, place orders, and manage their account on Faire.
  name: Faire External API v2 (Retailer)
  slug: external-api-v2-retailer
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/faire-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/faire-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Faire
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fairewholesale
- group: company
  title: ''
  type: Website
  url: https://www.faire.com/
- group: other
  title: ''
  type: Developer
  url: https://developers.faire.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/faire-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/faire-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/faire-finops.yml
created: '2026-05-08'
description: 'Faire is a wholesale marketplace connecting independent retailers with brands. The Faire External API v2 supports both sides of the marketplace: brand-side endpoints for products, orders, inventory, and shipments, and retailer-side endpoints for browsing and ordering.'
finops:
- name: Faire Finops
  service_category: Marketplace
  slug: faire-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/faire.png
layout: provider
modified: '2026-05-08'
name: Faire
nav: Providers
network: true
overview: Faire publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Wholesale, Retail, and Ecommerce.
plans:
- name: Faire Plans Pricing
  plan_count: 2
  slug: faire-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 1
  name: Faire Rate Limits
  slug: faire-rate-limits
score:
  band: minimal
  composite: 8.7
  delta: -0.3
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Faire Domain Security
  slug: faire-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Faire Vulnerability Disclosure
  slug: faire-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: faire
tags:
- Marketplace
- Wholesale
- Retail
- Ecommerce
website: https://www.faire.com/
---
