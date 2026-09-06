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
- description: MHub's REST API for its property-sales platform. The API is served from api.mhub.my and is authentication-gated (all probed endpoints return HTTP 401); no public OpenAPI/Swagger definition was availab
  name: MHub API
  slug: mhub-api
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://mhub.my
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mhub.my
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mhub.my
- group: company
  title: ''
  type: Blog
  url: https://mhub.my/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://mhub.my/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mhub-changelog.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://mhub.my/packages
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mhub-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mhub-llms.txt
created: '2026-07-17'
description: MHub is a Malaysian property-technology (proptech) platform operated by TRB Ventures Sdn Bhd and backed by 500 Global. It gives real-estate developers an integrated system to manage the entire new-property sales cycle — from lead generation, launch, and online booking (Showroom, CRM, SalesCandy) through automated billing and collections (Credit Control), accounting and financial reporting, statutory compliance (HIMS/KPKT registry synchronization and LHDN-compliant e-invoicing), commission control, and handover/defect management. MHub runs a developer portal at developer.mhub.my and an authentication-gated REST API at api.mhub.my for platform integrations.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mhub.png
layout: provider
modified: '2026-07-20'
name: MHub
nav: Providers
network: true
overview: 'MHub publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Property Technology, PropTech, and Malaysia.


  MHub''s developer surface includes documentation, engineering blog, changelog, pricing, and 5 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 12.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 12.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mhub/refs/heads/main/screenshots/mhub-2026-08-07T172813.png
security:
- kind: domain-security
  name: Mhub Domain Security
  slug: mhub-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mhub
tags:
- Company
- Real-Estate
- Property Technology
- PropTech
- Malaysia
- Sales
- CRM
- Accounting
- E-Invoicing
- Software-as-a-Service
website: https://mhub.my
---
