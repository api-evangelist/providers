---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: RESTful Open API for managing TikTok Shop seller accounts, products, orders, fulfillment, returns and refunds, logistics, finance, and promotions. Authentication uses OAuth 2.0 with App ID and app sec
  name: TikTok Shop Open API
  slug: open-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiktok-shop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shop.tiktok.com
- group: docs
  title: ''
  type: Documentation
  url: https://partner.tiktokshop.com/docv2/page/main
- group: start
  title: ''
  type: DeveloperPortal
  url: https://partner.tiktokshop.com
- group: start
  title: ''
  type: Signup
  url: https://seller-us.tiktok.com/account/register
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tiktok-shop-open
- group: operate
  title: ''
  type: Support
  url: https://seller-us.tiktok.com/university/help
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/tiktok-shop/
created: '2026-05-11'
description: TikTok Shop is TikTok's integrated e-commerce platform that lets sellers, creators, and partners list products, manage inventory and fulfillment, and sell directly within TikTok's live streams, short videos, and shop tabs. The TikTok Shop Open API (open-api.tiktokglobalshop.com) is a RESTful API that uses OAuth 2.0 authentication and enables developers to programmatically manage products, orders, fulfillment, returns, finance, promotions, and seller authorization across TikTok Shop's global marketplaces.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiktok-shop.png
layout: provider
modified: '2026-05-11'
name: TikTok Shop API
nav: Providers
network: true
overview: 'TikTok Shop API publishes 1 API on the [APIs.io](https://apis.io/) network: TikTok Shop Open API. Tagged areas include E-Commerce, Marketplace, Social Commerce, Order Management, and Product Catalog.


  TikTok Shop API''s developer surface includes documentation, signup flow, support, and 5 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiktok-shop/refs/heads/main/screenshots/tiktok-shop-2026-06-20T195350.png
security:
- kind: domain-security
  name: Tiktok Shop Domain Security
  slug: tiktok-shop-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tiktok-shop
tags:
- E-Commerce
- Marketplace
- Social Commerce
- Order Management
- Product Catalog
- Fulfillment
website: https://shop.tiktok.com
---
