---
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: REST API for food & nutrition data — search, barcode lookup, food-by-id, popular foods, categories, and health probe. Bearer auth optional; read endpoints work anonymously.
  name: DietlyAPI
  slug: dietlyapi
artifact_total: 1
created: '2026-07-17'
description: Food & nutrition data REST API with 4.2M+ foods, calories, macros, 17 micronutrients, barcode lookup, and confidence-ranked full-text search. Data primarily from Open Food Facts (ODbL), EU-hosted, with key-optional read access.
layout: provider
modified: '2026-07-17'
name: DietlyAPI
nav: Providers
network: true
overview: 'DietlyAPI publishes 1 API on the [APIs.io](https://apis.io/) network: DietlyAPI. Tagged areas include Food, Nutrition, Barcodes, open-food-facts, and Health.'
random_paper: 20
score:
  band: minimal
  composite: 10.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dietlyapi/refs/heads/main/screenshots/dietlyapi-2026-07-25T211947.png
slug: dietlyapi
tags:
- Food
- Nutrition
- Barcodes
- open-food-facts
- Health
- Open Data
---
