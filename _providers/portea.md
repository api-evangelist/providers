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
  url: https://www.portea.com
- group: company
  title: ''
  type: Blog
  url: https://www.portea.com/blogs/
- group: company
  title: ''
  type: About
  url: https://www.portea.com/about-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.portea.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.portea.com/terms-conditions/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/portea-domain-security.yml
created: '2026-07-17'
description: Portea Medical is India's leading home healthcare provider, delivering clinical care to patients at home across 40+ cities. Services include physiotherapy, nursing care, doctor consultations, medical equipment rental, trained attendants, diagnostic and lab tests, counselling, and specialized programs for eldercare, mother and baby care, diabetes, critical care, and vaccination. Portea was surfaced as a portfolio company of Accel and added to the API Evangelist network. As a consumer home-healthcare operator it publishes no public developer API, OpenAPI, or developer portal at this time; this profile captures its identity and a live domain-security probe.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/portea.png
layout: provider
modified: '2026-07-20'
name: Portea
nav: Providers
network: true
overview: 'Portea is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Healthcare, Home Healthcare, and Telemedicine.


  Portea''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/portea/refs/heads/main/screenshots/portea-2026-09-02T151807.png
security:
- kind: domain-security
  name: Portea Domain Security
  slug: portea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: portea
tags:
- Company
- Consumer
- Healthcare
- Home Healthcare
- Telemedicine
- Diagnostics
- India
website: https://www.portea.com
---
