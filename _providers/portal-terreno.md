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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portal-terreno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://portalterreno.com
created: '2026-07-17'
description: Portal Terreno is an online marketplace for land and parcels ("terrenos" and "parcelas") in Latin America, operating localized classifieds portals for Chile (portalterreno.cl) and Mexico (portalterreno.com.mx) with tens of thousands of land listings. The Next.js web platform lets buyers search, filter, and contact sellers to find land for sale, while sellers and real-estate agents publish listings. It was surfaced as a portfolio company of 500 Global and added to the API Evangelist network for enrichment. No public developer, API, documentation, or well-known discovery surface was found during the enrichment pass; the domain-security posture was probed live.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portal-terreno.png
layout: provider
modified: '2026-07-20'
name: Portal Terreno
nav: Providers
network: true
overview: Portal Terreno is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Classifieds, Marketplace, and Land.
random_paper: 0
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portal-terreno/refs/heads/main/screenshots/portal-terreno-2026-09-02T151805.png
security:
- kind: domain-security
  name: Portal Terreno Domain Security
  slug: portal-terreno-domain-security
  summary_line: TLSv1.3 · DMARC
slug: portal-terreno
tags:
- Company
- Real-Estate
- Classifieds
- Marketplace
- Land
- Property
- Chile
- Mexico
website: https://portalterreno.com
---
