---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 12.9
  scored_at: '2026-09-02'
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
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 1
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
