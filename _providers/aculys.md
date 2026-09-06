---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://aculys.com/en/'', ''status'': 301, ''note'': ''declared website redirects to https://www.viatris.jp/ — a different registrable domain (aculys.com -> viatris.jp), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/aculys-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aculys.com/en/
- group: company
  title: ''
  type: Blog
  url: https://aculys.com/en/news/
- group: company
  title: ''
  type: About
  url: https://aculys.com/en/company/
- group: other
  title: ''
  type: Products
  url: https://aculys.com/en/our-products/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aculys.com/en/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aculys.com/en/terms-and-conditions
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://aculys.com/en/security-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aculys/about/
created: '2026-07-17'
description: Aculys Pharma, Inc. is a Japanese clinical-stage biopharmaceutical company focused on neurological and psychiatric diseases where there is high unmet medical need. The company works to eliminate Japan's drug lag and drug loss by bringing innovative medicines already approved in Western markets to Japanese patients as early as possible. Its lead product is Spydia (diazepam nasal spray), Japan's first domestically developed intranasal anti-seizure agent, approved in June 2025 and administrable outside medical facilities. Originally funded by SoftBank Vision Fund (Series C, March 2025), Aculys was acquired by and became part of the Viatris Group in October 2025. Aculys publishes no public developer program, API, or technical documentation surface; this profile is maintained for network completeness and identity.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aculys.png
layout: provider
modified: '2026-07-17'
name: Aculys
nav: Providers
network: true
overview: 'Aculys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Pharmaceuticals, Biotech, and Neurology.


  Aculys'' developer surface includes engineering blog and 8 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 4.7
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 4.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aculys/refs/heads/main/screenshots/aculys-2026-07-25T181541.png
security:
- kind: domain-security
  name: Aculys Domain Security
  slug: aculys-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aculys
tags:
- Company
- Health Tech
- Pharmaceuticals
- Biotech
- Neurology
- Japan
website: https://aculys.com/en/
---
