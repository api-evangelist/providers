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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Florist One Agentic Access
  operation_count: 12
  slug: florist-one-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 5
apis:
- description: Florist One provides a free REST API for searching available flower products, retrieving product details and imagery, placing orders for delivery through the Florist One network, and checking order st
  name: Florist One API
  slug: florist-one-api
- description: The Affiliate API from Florist One — 1 operation(s) for affiliate.
  name: Florist One Affiliate API
  slug: florist-one-affiliate-api
- description: The FlowerShop API from Florist One — 5 operation(s) for flowershop.
  name: Florist One FlowerShop API
  slug: florist-one-flowershop-api
- description: The GiftBaskets API from Florist One — 3 operation(s) for giftbaskets.
  name: Florist One GiftBaskets API
  slug: florist-one-giftbaskets-api
- description: The ShoppingCart API from Florist One — 1 operation(s) for shoppingcart.
  name: Florist One ShoppingCart API
  slug: florist-one-shoppingcart-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Florist One REST Affiliate API
  slug: open-florist-one-affiliate-api
- collection_type: open
  name: Florist One REST Affiliate FlowerShop API
  slug: open-florist-one-flowershop-api
- collection_type: open
  name: Florist One REST Affiliate GiftBaskets API
  slug: open-florist-one-giftbaskets-api
- collection_type: open
  name: Florist One REST Affiliate ShoppingCart API
  slug: open-florist-one-shoppingcart-api
- collection_type: open
  name: Florist One REST API
  slug: open-florist-one
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/florist-one-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/florist-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/florist-one-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FloristOne
- group: company
  title: ''
  type: Website
  url: https://www.floristone.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.floristone.com/api/
- group: other
  title: ''
  type: TechnicalInformation
  url: https://www.floristone.com/api/technical-information/
- group: operate
  title: ''
  type: FAQ
  url: https://www.floristone.com/api/flowers-api-faq/
- group: operate
  title: ''
  type: Contact
  url: https://www.floristone.com/api/api-contact/
created: '2025-02-24'
description: Florist One is an online flower delivery service that specializes in creating and delivering floral arrangements through a network of local florists across the United States and Canada. Florist One offers a free REST web service that lets developers integrate flower products, ordering, and delivery into their own applications. The API is documented for use from any common web language including Java, PHP, ASP.NET, JavaScript, Node, Python, Perl, Ruby, and ColdFusion.
finops:
- name: Florist One Finops
  service_category: API
  slug: florist-one-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/florist-one.png
layout: provider
modified: '2026-04-28'
name: Florist One
nav: Providers
network: true
overview: 'Florist One publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Affiliate API, FlowerShop API, GiftBaskets API, and 1 more. Tagged areas include Delivery, Ecommerce, Florists, Flowers, and Gifts.


  Florist One''s developer surface includes authentication, documentation, FAQ, and 6 more developer resources.'
plans:
- name: Florist One Plans Pricing
  plan_count: 3
  slug: florist-one-plans-pricing
random_paper: 95
rate_limits:
- limit_count: 5
  name: Florist One Rate Limits
  slug: florist-one-rate-limits
score:
  band: thin
  composite: 29.3
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 52.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 29.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Florist One Authentication
  slug: florist-one-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Florist One Domain Security
  slug: florist-one-domain-security
  summary_line: TLSv1.3 · DMARC
slug: florist-one
tags:
- Delivery
- Ecommerce
- Florists
- Flowers
- Gifts
website: https://www.floristone.com/
---
