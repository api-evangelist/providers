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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apx.group
- group: company
  title: ''
  type: Blog
  url: https://apx.group/blog/
- group: operate
  title: ''
  type: Support
  url: https://apx.group/contactus/
- group: start
  title: ''
  type: Login
  url: https://apxapp.tech/#/login
created: '2026-07-17'
description: APX (APX Logistics Solutions) is a Southeast Asian less-than-truckload (LTL) digital logistics platform headquartered in Bangkok, with operations in Thailand, Malaysia, and Singapore. It positions itself as the region's first LTL digital logistics provider, offering domestic and cross-border shipping, international sea and air freight, customs brokerage, warehousing and distribution, project logistics, and heavy-lift/breakbulk services. Its proprietary technology platform provides online shipment booking, real-time tracking with ETA notifications, digital proof-of-delivery, AI-assisted route optimization, a driver app, and analytics dashboards including CO2/ESG reporting. APX is a portfolio company of 500 Global and was added to the API Evangelist network as a stub for enrichment. As of this enrichment pass APX publishes no first-party public developer API, SDKs, or developer portal; shipment tracking is currently integrable only via third-party aggregators.
image: https://apx.group/wp-content/uploads/2024/08/cropped-APX-master-logo-scaled-1.webp
layout: provider
modified: '2026-07-18'
name: APX
nav: Providers
network: true
overview: 'APX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Shipping, Freight, and Supply Chain.


  APX''s developer surface includes engineering blog, support, and 3 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 7.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apx/refs/heads/main/screenshots/apx-2026-07-25T200948.png
security:
- kind: domain-security
  name: Apx Domain Security
  slug: apx-domain-security
  summary_line: TLSv1.2 · DMARC
slug: apx
tags:
- Company
- Logistics
- Shipping
- Freight
- Supply Chain
- Southeast Asia
- Transportation
- Customs
- Warehousing
website: https://apx.group
---
