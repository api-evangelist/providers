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
  url: security/push-doctor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pushdoctor.co.uk/
- group: operate
  title: ''
  type: Support
  url: https://www.pushdoctor.co.uk/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pushdoctor.co.uk/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pushdoctor.co.uk/terms
created: '2026-07-17'
description: Push Doctor is a UK telehealth company offering video consultations with licensed UK GPs via smartphone, describing itself as the UK's first platform to provide video doctor consultations on mobile. It serves both NHS patients and private paying customers, covering online GP appointments, digital prescriptions, referrals and follow-up care. Headquartered in Manchester and backed by Partech, Push Doctor operates as a consumer-facing telemedicine service; no public developer API, developer portal, or SDK surface was found during enrichment probes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/push-doctor.png
layout: provider
modified: '2026-07-20'
name: Push Doctor
nav: Providers
network: true
overview: 'Push Doctor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Telehealth, Telemedicine, and Online GP.


  Push Doctor''s developer surface includes support and 4 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 2
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
  previous_composite: 10.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/push-doctor/refs/heads/main/screenshots/push-doctor-2026-09-02T152345.png
security:
- kind: domain-security
  name: Push Doctor Domain Security
  slug: push-doctor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: push-doctor
tags:
- Company
- Healthcare
- Telehealth
- Telemedicine
- Online GP
- Digital Health
- Video Consultation
- United Kingdom
website: https://www.pushdoctor.co.uk/
---
