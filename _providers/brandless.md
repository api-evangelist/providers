---
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://brandless.com
coverage:
  checked: '2026-08-08'
  detail: Brandless sold physical consumer packaged goods through a Shopify storefront and never ran a developer program; its own domain brandless.com now returns SERVFAIL (the delegated Cloudflare nameservers answer REFUSED) and the last archived captures show a domain-parking lander, so there is no host left to probe for a spec, .well-known document or agent card.
  evidence:
  - status: 0
    url: https://brandless.com/
  - status: 0
    url: https://www.brandless.com/
  - status: 200
    url: http://web.archive.org/web/20260118162303/http://brandless.com/
  - status: 200
    url: https://brandless.shop/
  - status: 403
    url: https://forgeglobal.com/brandless_stock/
  reason: defunct
  state: none
created: '2026-08-08'
description: Brandless is an American direct-to-consumer e-commerce retailer of own-label food, beauty, personal care and household goods, founded in 2016 by Tina Sharkey and Ido Leffler and launched in July 2017. SoftBank-backed, it ceased operations on 10 February 2020; its assets were bought in June 2020 by Clarke Capital Partners and Ikonifi and the brand relaunched that summer under Utah-based ownership, later led by Cydni Tetro and then Tiffany Vail. The storefront ran on Shopify and sold physical consumer packaged goods only — Brandless never operated a developer program, public API, SDK or webhook surface of its own. As of this profile the brandless.com domain no longer resolves and the site is parked, so there is no live company surface to profile.
layout: provider
modified: '2026-08-08'
name: Brandless
nav: Providers
network: true
overview: Brandless is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Consumer Packaged Goods, and Direct to Consumer.
random_paper: 13
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 4.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
slug: brandless
tags:
- Company
- E-Commerce
- Retail
- Consumer Packaged Goods
- Direct to Consumer
- Household Products
- Personal Care
website: https://brandless.com
---
