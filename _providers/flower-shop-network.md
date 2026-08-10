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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Flower Shop Network Agentic Access
  operation_count: 11
  slug: flower-shop-network-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 4
apis:
- description: Token issuance and validation
  name: Flower Shop Network Authentication API
  slug: flower-shop-network-authentication-api
- description: Florist directory lookup
  name: Flower Shop Network Florists API
  slug: flower-shop-network-florists-api
- description: Wire order receipt, acceptance, sending, and delivery
  name: Flower Shop Network Orders API
  slug: flower-shop-network-orders-api
- description: Product catalog access
  name: Flower Shop Network Products API
  slug: flower-shop-network-products-api
artifact_total: 10
collections:
- collection_type: open
  name: Flower Shop Network JSON API
  slug: open-flower-shop-network
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flower-shop-network-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flower-shop-network-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flower-shop-network
- group: company
  title: ''
  type: Website
  url: https://www.flowershopnetwork.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.flowershopnetwork.com/
- group: company
  title: ''
  type: Blog
  url: https://www.flowershopnetwork.com/blog/feed/
created: '2025-02-24'
description: Flower Shop Network is a platform that connects customers with local florists across the country. They provide an online marketplace where users can browse and purchase a wide variety of floral arrangements for all occasions, and expose a JSON API for partner POS systems to authenticate, look up products and florists, and exchange wire orders across the FSN florist network.
finops:
- name: Flower Shop Network Finops
  service_category: API
  slug: flower-shop-network-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flower-shop-network.png
layout: provider
modified: '2026-05-19'
name: Flower Shop Network
nav: Providers
network: true
overview: 'Flower Shop Network publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Florists API, Orders API, and 1 more. Tagged areas include Florists, Flowers, Wire Orders, and Point of Sale.


  Flower Shop Network''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Flower Shop Network Plans Pricing
  plan_count: 3
  slug: flower-shop-network-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 5
  name: Flower Shop Network Rate Limits
  slug: flower-shop-network-rate-limits
score:
  band: thin
  composite: 32.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 47.3
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flower-shop-network/refs/heads/main/screenshots/flower-shop-network-2026-06-20T181329.png
security:
- kind: domain-security
  name: Flower Shop Network Domain Security
  slug: flower-shop-network-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: flower-shop-network
tags:
- Florists
- Flowers
- Wire Orders
- Point of Sale
website: https://www.flowershopnetwork.com/
---
