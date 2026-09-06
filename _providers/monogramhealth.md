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
  url: security/monogramhealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monogramhealth.com
created: '2026-07-17'
description: Monogram Health is a value-based, in-home specialty care provider for people living with chronic kidney disease, end-stage renal disease, and other complex chronic conditions. Multidisciplinary teams of physicians, nurse practitioners, nurses, dietitians, pharmacists, and social workers deliver coordinated care in patients' homes with 24/7 access, addressing both medical needs and social determinants of health to reduce hospitalizations and emergency visits. Headquartered in Nashville, Tennessee, the company partners with health plans (payer partners) and provider groups and serves over 200,000 patients annually. This is a healthcare services company with no public developer, API, or platform surface; the enrichment pass probed domain security and found no API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monogramhealth.png
layout: provider
modified: '2026-07-20'
name: Monogramhealth
nav: Providers
network: true
overview: Monogramhealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Value-Based Care, Kidney Care, and Chronic Disease.
random_paper: 3
score:
  band: minimal
  composite: 3.3
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monogramhealth/refs/heads/main/screenshots/monogramhealth-2026-08-07T184207.png
security:
- kind: domain-security
  name: Monogramhealth Domain Security
  slug: monogramhealth-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: monogramhealth
tags:
- Company
- Healthcare
- Value-Based Care
- Kidney Care
- Chronic Disease
- In-Home Care
- Nephrology
website: https://monogramhealth.com
---
