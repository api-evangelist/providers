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
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://doos.sa
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/doos-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doos-domain-security.yml
created: '2026-07-17'
description: Doos is a Saudi-based quick-commerce (q-commerce) platform and mobile app that delivers groceries, fresh produce, beauty, gifting, pharmacy, and lifestyle products in minutes across Saudi Arabia. Founded in 2023 by Tala Al Sahsah, it operates cloud/dark stores in Jeddah and Riyadh with localised assortments, prices, and promotions by city and delivery zone, offering a bilingual (Arabic/English) shopping experience. Doos is backed by 500 Global and received a strategic investment from Jahez to accelerate its expansion in the Kingdom's growing quick-commerce sector. This is a consumer-facing storefront; no public developer program or API has been identified at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doos.png
layout: provider
modified: '2026-07-18'
name: Doos
nav: Providers
network: true
overview: Doos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quick Commerce, Q-Commerce, Grocery Delivery, and E-Commerce.
random_paper: 17
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doos/refs/heads/main/screenshots/doos-2026-07-25T212306.png
security:
- kind: domain-security
  name: Doos Domain Security
  slug: doos-domain-security
  summary_line: TLSv1.3
slug: doos
tags:
- Company
- Quick Commerce
- Q-Commerce
- Grocery Delivery
- E-Commerce
- Retail
- Consumer
- Saudi Arabia
- MENA
website: https://doos.sa
---
