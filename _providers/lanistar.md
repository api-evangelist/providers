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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: CompanyRegistration
  url: https://find-and-update.company-information.service.gov.uk/company/12091938
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/lanistar-stock
created: '2026-08-04'
description: 'Lanistar was a London-based consumer fintech founded in 2019 by Gurhan Kiziloz, known for a heavily influencer-marketed "polymorphic" Mastercard debit card with an on-card keypad and display that generated single-use PIN and CVV2 codes. Lanistar Limited operated as an EMD agent of Modulr FS Limited under FCA authorisation, with cards issued by AF Payments Limited, and pivoted its consumer launch to Brazil where it offered a mobile account, Pix transfers and in-app crypto buying and selling. The company never operated a developer program: no public API, developer portal, OpenAPI or other machine-readable contract, SDK, or public GitHub repository was ever published. Lanistar Limited (company number 12091938) was placed into compulsory liquidation by a court winding-up order filed 14 April 2025, and its public surface has since gone dark — lanistar.com and lanistar.app no longer resolve to any web host, the lanistar.co.uk domain is listed for sale by a domain broker, and the
  com.lanistar Google Play listing has been removed. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-04'
name: Lanistar
nav: Providers
network: true
overview: Lanistar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Financial-Services, Fintech, and Banking.
random_paper: 1
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - latin-america
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lanistar/refs/heads/main/screenshots/lanistar-2026-08-07T171446.png
slug: lanistar
tags:
- Company
- Defunct
- Financial-Services
- Fintech
- Banking
- Payments
- Debit Cards
- Neobank
- United Kingdom
- Brazil
---
