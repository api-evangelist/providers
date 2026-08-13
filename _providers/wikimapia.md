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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Wikimapia REST API provides access to crowdsourced geographic data including places, categories, streets, and languages. Supports place search by bounding box, coordinates, or full-text query; pla
  name: Wikimapia REST API
  slug: rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wikimapia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wikimapia.org/
- group: docs
  title: ''
  type: Documentation
  url: https://wikimapia.org/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Wikimapia
- group: company
  title: ''
  type: Blog
  url: https://wikimapia.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://wikimapia.org/api/?action=my_keys
- group: other
  title: ''
  type: X
  url: https://x.com/wikimapia
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/wikimapia/refs/heads/main/plans/wikimapia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/wikimapia/refs/heads/main/rate-limits/wikimapia-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/wikimapia/refs/heads/main/finops/wikimapia-finops.yml
created: '2026-06-13'
description: Wikimapia is a collaborative geographic wiki that layers crowdsourced place information onto satellite imagery. Launched in 2006, the platform covers over 32 million geographic objects contributed by its community. The REST API provides programmatic access to places, categories, streets, and geographic searches using API-key authentication. Responses are available in JSON and KML formats. The API supports bounding-box queries, coordinate-based nearest-place lookups, full-text search, and detailed place retrieval including geometry, photos, comments, and community-tagged categories.
finops:
- name: Wikimapia Finops
  service_category: Geospatial / Crowdsourced Mapping Data
  slug: wikimapia-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wikimapia.png
layout: provider
modified: '2026-06-13'
name: Wikimapia
nav: Providers
network: true
overview: 'Wikimapia publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, Mapping, Crowdsourced, Places, and Geographic Data.


  Wikimapia''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Wikimapia Plans Pricing
  plan_count: 2
  slug: wikimapia-plans-pricing
random_paper: 116
rate_limits:
- limit_count: 2
  name: Wikimapia Rate Limits
  slug: wikimapia-rate-limits
score:
  band: emerging
  composite: 20.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.3
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wikimapia/refs/heads/main/screenshots/wikimapia-2026-06-20T201453.png
security:
- kind: domain-security
  name: Wikimapia Domain Security
  slug: wikimapia-domain-security
  summary_line: TLSv1.2
slug: wikimapia
tags:
- Geospatial
- Mapping
- Crowdsourced
- Places
- Geographic Data
website: https://wikimapia.org/
---
