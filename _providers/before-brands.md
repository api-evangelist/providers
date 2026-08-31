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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://beforebrands.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/before-brands-inc.
coverage:
  checked: '2026-08-06'
  detail: Before Brands was absorbed into Nestle Health Science — beforebrands.com now delegates to nestle.com nameservers, resolves to the sitedetour.com parking host and returns 404, while spoonfulone.com 301s to nestlehealthscience.com whose SpoonfulOne brand page itself 301s to a generic brand index, so there is no company surface left to profile.
  evidence:
  - status: 404
    url: http://beforebrands.com/
  - status: 301
    url: https://spoonfulone.com/
  - status: 301
    url: https://www.nestlehealthscience.com/brands/spoonfulone
  - status: 404
    url: http://beforebrands.com/openapi.json
  - status: 404
    url: http://beforebrands.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/beforebrands
  reason: defunct
  state: none
created: '2026-08-06'
description: 'Before Brands, Inc. was a Menlo Park, California science-based food and nutrition company founded on Stanford allergy research by Dr. Kari Nadeau, best known for SpoonfulOne — a consumer early-allergen-introduction product line that blended sixteen commonly allergenic proteins into daily servings for infants and toddlers. Nestle Health Science took a minority stake plus ex-US licensing rights in 2019 and later absorbed the business outright. It was a consumer packaged goods company, not a software company: it never operated a developer program, published no API, SDK or webhook surface, and its own domain is now controlled by Nestle and no longer serves a site.'
layout: provider
modified: '2026-08-06'
name: Before Brands
nav: Providers
network: true
overview: Before Brands is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Nutrition, and Health.
random_paper: 4
score:
  band: minimal
  composite: 1.8
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
      reason: venue_as_website
    - owner: catalog
      reason: never_enriched
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: before-brands
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Nutrition
- Health
- Allergy
- Infant Nutrition
- Acquired
website: https://beforebrands.com
---
