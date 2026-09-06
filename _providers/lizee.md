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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Lizee's production operations API powering its rental, resale, and logistics platforms. Confirmed live via the company status page (components "API v1" and "e-commerce API & Admin") and the production
  name: Lizee API v1
  slug: lizee-api-v1
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://lizee.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lizee.io
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lizee-lifecycle.yml
created: '2026-07-17'
description: Lizee is a Paris-based Retail-as-a-Service platform that helps brands and retailers launch and operate circular commerce programs — rental, resale, and second-hand — end to end. Its stack pairs a rental platform, a resale/e-commerce platform, and a logistics platform (returns, refurbishment, reverse logistics) behind an operations API so a brand can offer rent or buy-back experiences on top of its existing catalog. Lizee runs a production API (api.lizee.io) and publishes a public Atlassian Statuspage, though it does not expose a public developer portal, OpenAPI definition, or SDKs — the API surface is partner and integration facing. Lizee was added to the API Evangelist network as a portfolio company of Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lizee.png
layout: provider
modified: '2026-07-20'
name: Lizee
nav: Providers
network: true
overview: Lizee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Rentals, Resale, and Secondhand.
random_paper: 12
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 8.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lizee/refs/heads/main/screenshots/lizee-2026-07-25T225412.png
slug: lizee
tags:
- Company
- Retail
- Rentals
- Resale
- Secondhand
- Circular Economy
- Logistics
- E-Commerce
- Reverse Logistics
website: https://lizee.io
---
