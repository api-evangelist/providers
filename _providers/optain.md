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
  url: security/optain-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.optainhealth.com/us/
- group: company
  title: ''
  type: About
  url: https://www.optainhealth.com/about/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optainhealth.com/privacy
created: '2026-07-17'
description: Optain (Optain Health) is a healthcare technology company delivering AI-powered retinal imaging and oculomics for early, non-invasive detection of chronic disease at the point of care. Its platform pairs the FDA 510(k)-cleared Resolve robotic fundus camera and Eyetelligence Assure Software as a Medical Device (SaMD) with teleophthalmology grading to screen for diabetic retinopathy, glaucoma, age-related macular degeneration, hypertensive retinopathy and cardiovascular risk in seconds, without dilation. Rooted in Australian-founded Eyetelligence (2019) and research from the Centre for Eye Research Australia, Optain integrates with major EHR systems and returns ICD-10-coded reports, typically same day. Backed by Insight Partners. No public developer API surface is currently published.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optain.png
layout: provider
modified: '2026-07-20'
name: Optain
nav: Providers
network: true
overview: Optain is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Medical Imaging, and Ophthalmology.
random_paper: 0
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/optain/refs/heads/main/screenshots/optain-2026-08-07T190754.png
security:
- kind: domain-security
  name: Optain Domain Security
  slug: optain-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: optain
tags:
- Company
- Healthcare
- Artificial Intelligence
- Medical Imaging
- Ophthalmology
- Retinal Screening
- Oculomics
- Diagnostics
- Medical Device
website: https://www.optainhealth.com/us/
---
