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
  url: https://tuli.health/
- group: start
  title: ''
  type: Login
  url: https://portal.tuli.health
- group: operate
  title: ''
  type: Support
  url: https://tulisupport.crisp.help/en/category/general-c5u9fq/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tuli.health/terms-of-services
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tuli.health/privacy-policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tuli-domain-security.yml
created: '2026-07-17'
description: Tuli Health operates a UK-wide network of over 300 high-street pharmacies as local diagnostic hubs, making clinical services - primarily blood testing and phlebotomy - accessible in every neighbourhood so people can get care close to home. It offers healthcare providers three models - One Network (white-label phlebotomy), One Solution (end-to-end test kits, draws and lab analysis), and an Enterprise tier with custom integration. Tuli exposes an API and web portal for booking and managing tests, though public developer documentation is not yet published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tuli.png
layout: provider
modified: '2026-07-21'
name: Tuli
nav: Providers
network: true
overview: 'Tuli is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Blood Testing, and Phlebotomy.


  Tuli''s developer surface includes support and 5 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 8.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tuli/refs/heads/main/screenshots/tuli-2026-09-02T164506.png
security:
- kind: domain-security
  name: Tuli Domain Security
  slug: tuli-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tuli
tags:
- Company
- Healthcare
- Diagnostics
- Blood Testing
- Phlebotomy
- Pharmacy
- Health Tech
- United Kingdom
website: https://tuli.health/
---
